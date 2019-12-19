var i = 0;
var txt = 'A powerful text search engine.';
var speed = 50;

window.onload = typeWriter();

function typeWriter() {
  if (i < txt.length) {
    document.getElementById("demo").innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
  }
}