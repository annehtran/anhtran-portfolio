![DAX](https://img.shields.io/badge/DAX-0E5A8A?logo=microsoft&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)

## Report 1 - Sea Level Rises

[Power BI App](https://app.powerbi.com/view?r=eyJrIjoiMzc4YWY4NmUtZDZiMi00YzY2LTk0ZGYtN2ViZDRlNDZlOGM2IiwidCI6ImVlZGE2ZTc3LWZkZjMtNGYwMS04OWEwLTQ5Zjk2NDgwMGJjYyIsImMiOjZ9)  

### Skills Demonstrate
Using Vega-lite code to create custom Deneb chart, the combination of line charts and scatterplot displays the sea level rising from 1977 to 2020.
- The combined line‑and‑point design makes it easy to see both the long‑term upward trend and the year‑to‑year variability in sea levels.
```json  
  "layer": [
    {
      "mark": {
        "type": "point",
        "tooltip": true,
        "filled": true,
        "opacity": 0.4,
        "size": 20
      },
      "encoding": {
        "x": {
          "field": "Time",
          "type": "temporal",
          "title": null,
          "axis": {
            "format": "%Y",
            "labelAngle": 0,
            "grid": false,
            "tickCount": "year",
            "labelColor": "#666666"
          }
        },
        "y": {
          "field": "Sea Level",
          "type": "quantitative",
          "title": "Sea Level (mm)",
          "axis": {
            "grid": true,
            "gridColor": "#eeeeee",
            "labelColor": "#666666",
            "labelExpr": "datum.value + ' mm'"
          }
        },
```
 - Deneb allows to build visuals that are impossible with native Power BI charts. Vega‑Lite gives full control over marks, layers, scales, tooltips, and interactions, enabling pixel‑perfect custom visualizations inside Power BI.     

 ```markdown
![Sea Level Visualization](report_snapshots/Sealevelrises.PNG)

```
### Raw Dataset
- Retrieved on January 28, 2024
- Source: https://ourworldindata.org/grapher/sea-level?time=earliest..2020-10-15
- Data source: NOAA Climate.gov (2022) – processed by Our World in Data
