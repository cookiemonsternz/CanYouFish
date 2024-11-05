from flask import Flask, render_template, send_from_directory, request, redirect, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import img_to_array
from tensorflow.keras.activations import sigmoid
from PIL import Image
import numpy as np
import base64
from io import BytesIO


app = Flask(__name__)

global model
confidence = 0

@app.route('/', methods=['GET', 'POST'])
def init():
    global model
    global confidence
    if request.method == 'POST':
        print('POST')
        print(request.form)
        # Prepare the data
        data = prepare_data(request.form)
        data = np.expand_dims(data, axis=0)
        result = model(data)
        #print(data)
        print(f'result : ${result}')
        prediction = (sigmoid(result[0][0]))
        print(f'prediction : {prediction}%')
        #return render_template('isFish.html')
        # convert prediction to confidence rating
        if prediction < 0.5:
            confidence = str(round((1 - float(prediction)) * 100, 2))
            print(f'fish : {confidence}')
            # go to /isFish
            return (url_for('isFish'))
            #return render_template('isFish.html')
        else:
            confidence = str(round(float(prediction*100), 2))
            print(f'not fish : {confidence}')
            # go to /isNotFish
            return (url_for('isNotFish'))
            #return render_template('isNotFish.html')
    model = load_model('./static/model/model.keras', compile=False)
    #model = load_model('C:/Users/chrsitpher/Documents/.Projects/CanYouFish/webapp/static/model/model.h5')
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    #model.summary()
    return render_template('index.html')

@app.route('/isFish')
def isFish():
    global confidence
    #return render_template('isNotFish.html')
    #print(f'confidence : {confidence}')
    return render_template('isFish.html', prediction=confidence)   

@app.route('/isNotFish')
def isNotFish():
    global confidence
    #print(f'confidence : {confidence}')
    return render_template('isNotFish.html', prediction=confidence)

@app.route('/cdn/<path:filename>')
def custom_static(filename):
    return send_from_directory('/static', filename)

def prepare_data(data):
    data = data['imgBase64']
    data = data.split(',')[1] # Remove the data:image/png;base64,
    image_data = base64.b64decode(data)
    image = Image.open(BytesIO(image_data))
    image.show()
    image = image.resize((100,100))
    image = image.convert('RGB')
    return img_to_array(image)