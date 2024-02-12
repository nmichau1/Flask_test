



let geojson2 = {
  "type": "FeatureCollection",
  "features": [
}
var width = 2500; 
var height = 3000;

let projection = d3.geoAlbersUsa()
  //.center([-74, 40.71])
  .scale(400000)
  .translate([-116750,29010])
  

let geoGenerator = d3.geoPath()
  .projection(projection);

var svg = d3.select("#maptest") 
            .attr("width", width)
            .attr("height", height)
          
svg.selectAll('path')
    .data(geojson2.features)
    .enter()
    .append('path')
    .attr('d', geoGenerator)
    .style("fill", "white") 
    .style("stroke", "black");

