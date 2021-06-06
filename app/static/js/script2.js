destinations = [
  {
    destination: "10.971599,76.594566",
  },
  {
    destination: "11.971599,77.594566",
  },
  {
    destination: "10.971599,77.594566",
  },
];
var map2 = document.getElementById("map2");
map2.innerHTML = `<iframe width="600" height="450" style="border:0" loading="lazy" allowfullscreen src="https://www.google.com/maps/embed/v1/directions?key=AIzaSyCr34QOcCBOKwVzqaHGIara51YJGOa4Hys&origin=12.971599,77.594566&destination=${destinations[2][0]}&waypoints=${destinations[1][0]}|${destinations[0][0]}&avoid=tolls&mode=driving"></iframe>`;
