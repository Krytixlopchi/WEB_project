var count = 0;
setInterval(function () {
  document.getElementById("banner").style.backgroundPosition =
    "-" + ++count + "px";
}, 50);
