Title: [GIS] Leaflet+GIS tools~
Date: 2015-09-03 12:28
Modified: 2015-09-03 12:28
Category: Archive
Tags: [GIS, front-end]
Authors: Solring Lin
Summary: (archive) [GIS] Leaflet+GIS tools~


# GIS Tools

## 經緯度及坐標系統
二度分帶坐標 TWD97
http://www.sunriver.com.tw/grid_tm2.htm

EPSG
收錄訂定各種投影坐標系統的組織

某人整理的心得
http://vinn.logdown.com/posts/2014/03/11/note-3-overview-of-openlayers-map-projection

## Leaflet
[http://leafletjs.com/examples/quick-start.html](http://ogre.adc4gis.com/)
繪製GIS
可吃圖磚, GeoJSON

A simple example
```html
<html>
<head>
  <title>Leaflet test</title>
  <link rel=stylesheet type=text/css href="http://cdn.leafletjs.com/leaflet-0.7/leaflet.css" />
	<script src="http://cdn.leafletjs.com/leaflet-0.7/leaflet.js"></script>
</head>

<body>
  <div id="map" style="height:300px; width:600px;"></div>
	<p>This is a test map</p>

<script>
var map = L.map('map').setView([25.032961, 121.562655], 14);
mapLink = 'OpenStreetMap';
        L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', 
            {
                attribution: 'Map data &copy; ' + mapLink,
                maxZoom: 18
            }
        ).addTo(map);
</script>
</body>

</html>
```
Reference
https://leanpub.com/leaflet-tips-and-tricks/read#leanpub-auto-html-1

## Shapefile轉GeoJSON
org2org lib
[http://www.gdal.org/ogr2ogr.html](http://www.gdal.org/ogr2ogr.html)

org2org online tool
[http://ogre.adc4gis.com/](http://ogre.adc4gis.com/)

# Tile services
中研院WMTS
[http://gis.sinica.edu.tw/tileserver/](http://gis.sinica.edu.tw/tileserver/)


# Other tools

## JS test tool
[https://jsfiddle.net/](https://jsfiddle.net/)

## Turf.js
對GeoJSON做運算 output也是GeoJSON 沒有畫圖功能
[http://turfjs.org/](http://turfjs.org/)

## Google map styler
[http://www.mapstylr.com/](http://www.mapstylr.com/)
可以修改顯示的圖層，顏色，線段寬度等資訊
最後會產生一個json file，可餵給Google map API or leaflet GMAP plugin

