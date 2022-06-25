require(["esri/config", "esri/Map", "esri/views/MapView"], function (
  esriConfig,
  Map,
  MapView
) {
  const map = new Map({
    basemap: "gray-vector",
  });

  view = new MapView({
    container: "viewDiv",
    map: map,
    extent: {
      xmin: -2.65,
      ymin: 54.2,
      xmax: -2.7,
      ymax: 54.25,
      spatialReference: 4326,
    },
  });
});
