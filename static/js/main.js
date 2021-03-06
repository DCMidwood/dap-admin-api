require([
    "esri/config",
    "esri/Map", 
    "esri/views/MapView",
    "esri/layers/FeatureLayer",
    "esri/layers/GeoJSONLayer"    
], function(
    esriConfig,
    Map,
    MapView,
    FeatureLayer,
    GeoJSONLayer
) { 

    // Set API Key
    esriConfig.apiKey = "AAPK07debd14a9ae4f03a01da38f19b27fedM5k4aLdVhDJxdnNKa3--HjeN9XwqQIScajcYBxn2F8naSMjGFGmpyWrvqhkedhgD";

    const url = "https://services.arcgis.com/JJzESW51TqeY9uat/ArcGIS/rest/services/SSSI_England/FeatureServer/0";
    
    const template = {
        title: "Track Details",
        lastEditInfoEnabled: false,
        content: "TrackId {track_id} <br> Track Type {track_type}"
    }

    const featureLayer = new FeatureLayer({
        title: "SSSI",
        url: url,
        copyright: "Natural England",
        popupTemplate: template
    });

    //const gjson_url =  "resources/data/civ_tracks.geojson";
    //const geojsonLayer = new GeoJSONLayer({
    //    url: gjson_url
    //});

    // create a geojson layer from geojson feature collection
    const geojson = {
            "type": "FeatureCollection",
            "name": "civ_tracks",
            "crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
            "features": [
            { "type": "Feature", "properties": { "uid": 1, "track_id": "AT01", "track_type": "C = Unsealed Minor Access Road" }, "geometry": { "type": "LineString", "coordinates": [ [ -2.700554573797803, 54.222562355370492 ], [ -2.701061428805686, 54.222374631293505 ], [ -2.701643373444365, 54.222440334720446 ], [ -2.701633987240516, 54.222346472681956 ], [ -2.702732173090928, 54.222252610643459 ], [ -2.702497517994686, 54.222036727954915 ], [ -2.702732173090928, 54.221839617674071 ], [ -2.702750945498627, 54.221576803966279 ], [ -2.702910510964072, 54.221285831646938 ], [ -2.703220255691111, 54.221116879977643 ], [ -2.70324841430266, 54.220929155900649 ], [ -2.70411194505683, 54.220046852738783 ], [ -2.704365372560771, 54.219952990700286 ], [ -2.704478007006967, 54.219774652827141 ], [ -2.704478007006967, 54.219493066711649 ], [ -2.704900386180202, 54.219098846149969 ] ] } },
            { "type": "Feature", "properties": { "uid": 2, "track_id": "AT02", "track_type": "C = Unsealed Minor Access Road" }, "geometry": { "type": "LineString", "coordinates": [ [ -2.697288174858116, 54.217934956872604 ], [ -2.702591380033183, 54.21772846038791 ], [ -2.703473683195052, 54.217672143164812 ], [ -2.705125655072595, 54.217503191495517 ], [ -2.705125655072595, 54.217503191495517 ] ] } },
            { "type": "Feature", "properties": { "uid": 3, "track_id": "AT03", "track_type": "C = Unsealed Minor Access Road" }, "geometry": { "type": "LineString", "coordinates": [ [ -2.704862841364804, 54.219098846149969 ], [ -2.704881613772503, 54.218826646238327 ], [ -2.704750206918608, 54.218272860211194 ], [ -2.704731434510908, 54.2180663637265 ], [ -2.705003634422549, 54.217878639649506 ], [ -2.705125655072595, 54.217531350107066 ] ] } },
            { "type": "Feature", "properties": { "uid": 4, "track_id": "AT04", "track_type": "C = Unsealed Minor Access Road" }, "geometry": { "type": "LineString", "coordinates": [ [ -2.695584578859399, 54.221365614379657 ], [ -2.695528261636301, 54.221140345487271 ], [ -2.695415627190105, 54.220952621410277 ], [ -2.695725371917145, 54.220717966314034 ], [ -2.695950640809536, 54.220361290567745 ], [ -2.696889261194504, 54.2201829526946 ], [ -2.697508750648582, 54.220286200936947 ], [ -2.698053150471864, 54.220023387229155 ], [ -2.698118853898811, 54.219816890744461 ], [ -2.698475529645099, 54.219835663152161 ] ] } },
            { "type": "Feature", "properties": { "uid": 5, "track_id": "BT05", "track_type": "C = Unsealed Minor Access Road" }, "geometry": { "type": "LineString", "coordinates": [ [ -2.698503688256648, 54.219816890744461 ], [ -2.697367957590838, 54.218540367020907 ], [ -2.697208392125393, 54.218202463682317 ], [ -2.697283481756191, 54.217930263770683 ] ] } }
            ]
            };

    // create a new blob from geojson featurecollection
    const blob = new Blob([JSON.stringify(geojson)], {
      type: "application/json"
    });

    // URL reference to the blob
    const gjson_url = URL.createObjectURL(blob);
    // create new geojson layer using the blob url
    const geojsonLayer = new GeoJSONLayer({
      url: gjson_url
    });



      const map = new Map({
        //basemap: "gray-vector"
        basemap: "arcgis-topographic", // Basemap layer
        layers: [featureLayer, geojsonLayer]
    }); 

    view = new MapView({
        container: "viewDiv",
        map: map,
        extent: {
            xmin: -2.65, 
            ymin: 54.2,
            xmax: -2.7,
            ymax: 54.25,
           spatialReference: 4326
        }
        //center: [-117.506, 33.66559],
        //zoom: 12
    });
});