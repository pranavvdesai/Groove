mapboxgl.accessToken =
  "pk.eyJ1Ijoic2hhcmF0aDI2NzAyIiwiYSI6ImNrbmFiZzV3NzBtYmgycWxjcWhmODFzc3AifQ.JLDx8LciuIgkg9XvnI4fYQ";

navigator.geolocation.getCurrentPosition(successLocation, errorLocation, {
  enableHighAccuracy: true,
});

function successLocation(position) {
  setupMap([position.coords.longitude, position.coords.latitude]);
  //marker()
}
function errorLocation() {
  setupMap(77.594566, 12.971599);
}
function setupMap(center) {
  const map = new mapboxgl.Map({
    container: "map",
    style: "mapbox://styles/mapbox/streets-v11",
    center: center,
    zoom: 4,
  });

  var directions = new MapboxDirections({
    accessToken: mapboxgl.accessToken,
    unit: "metric",
    profile: "mapbox/driving",
  });
  //console.log(MapboxDirections)
  map.addControl(directions, "top-left");

  const nav = new mapboxgl.NavigationControl();
  map.addControl(nav, "bottom-right");

  var marker1 = new mapboxgl.Marker({
    color: "#0000FF",
    draggable: false,
  })
    .setLngLat(center)
    .addTo(map);

  var marker2 = new mapboxgl.Marker({
    color: "#FF0000",
    draggable: true,
  })
    .setLngLat([78.6569, 11.1271])
    .addTo(map);

  function onDragEnd() {
    var lngLat = marker2.getLngLat();
    console.log(lngLat.lng, lngLat.lat);
  }
  marker2.on("dragend", onDragEnd);

  var geocoder = new MapboxGeocoder({
    accessToken: mapboxgl.accessToken,
    flyTo: false,
    marker: {
      color: "orange",
    },
    mapboxgl: mapboxgl,
  });
  map.addControl(geocoder);
}
