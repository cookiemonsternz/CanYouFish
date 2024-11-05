
var video = document.querySelector("#videoElement");

if (navigator.mediaDevices.getUserMedia) {
  navigator.mediaDevices.getUserMedia({ video: true })
    .then(function (stream) {
      video.srcObject = stream;
    })
    .catch(function (err0r) {
      console.log("Something went wrong!");
    });
}

function takeSnapshot() {
  var canvas = document.getElementById('canvas');
  var context = canvas.getContext('2d');
  var video = document.getElementById('videoElement');
  //console.log(`Taking snapshot: ${video.videoWidth} x ${video.videoHeight}`);
  // ajax call to send image to server
  canvas.width = 100;
  canvas.height = 100;
  context.drawImage(video, 0, 0, width = 100, height = 100);
  var dataURL = canvas.toDataURL('image/png');
  console.log(dataURL);
  $.ajax({
    type: "POST",
    url: "/",
    data: {
      imgBase64: dataURL
    },
    success: function (data) {
      console.log(data);
      window.location.href = data;
    }
  })
}