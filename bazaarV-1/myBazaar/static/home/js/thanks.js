var anchor = document.querySelector('#bgcolor');

// the function below will generate some random color
function getRandomColor(){
  var letters ='0123456789ABCDEF'
  var color ='#'
  for (var i = 0; i < 6; i++) {
    // the code below will generate random integer in between 0 to 16
    var r = Math.floor(Math.random()*16)
    color = color+letters[r]
    }
  return color;
  }

setInterval(function(){anchor.style.background=getRandomColor()},1000)
