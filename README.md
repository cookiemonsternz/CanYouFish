# Can You Fish?
![image](https://github.com/user-attachments/assets/f94e5c77-4c5e-40fe-b761-3539e7b3c019)

_Can You Fish_ is a vital tool in the ever changing landscape of **human identity**. Every day, thousands, even millions of people face the ever present question. 
***
### ***Is fish?***
***
This tool was developed to answer this question, once and for all. _Can You Fish_ is the perfect blend between simplicity, accuracy, and comfort, 
providing you with identity security whenever you need it most.
***
## Development Process

I developed _Can You Fish_ as an excercise in creation and deployment of keras models. I quickly trained a binary classifier cnn based on a variety of images
of fish and people using the datasets linked at the bottom of the page. Following this, I built a simple flask app to contain it (A framework I have never previously used)
and then attempted to deploy it. 

My first attempt was to deploy using Google Cloud App Engine, but I didn't have a credit card with which to initiate a 
free trial. I then tried to deploy using Microsoft Azure, but found it extremely difficult. I tried three other hosting solutions, each with varying challenges,
from rebuilding my model in older versions of python to locally hosting xmhttp servers. 

Eventually, however, I gave up.

I had at this point spent nearly 8 hours beyond the logged time trying to deploy this app and was considering having the demo as a video :(

It was at this point that I once again tried Azure, and somehow it magically half-worked. 
Following another few hours of bugfixing and waiting 20 mins to update the code on Azure, I finally had my finished app.

## Building locally

Clone the repo to a local folder

install the requirements -
```
Pip install -r requirements.txt
```

Build and run flask app - 
In powershell terminal, navigate to root folder containing train.py, etc. 
Run the following command
```
python -m flask --app webapp/app run --debug
```

### Tailwind
Install tailwind -
```
npm install -D tailwindcss
```
Initialize tailwind - 
```
npx tailwindcss init
```
Run tailwind - 
```
npx tailwindcss -i ./webapp/static/main.css -o ./webapp/static/styles/output.css --watch
```

You should now be able to edit the classes in html and have the css update.
