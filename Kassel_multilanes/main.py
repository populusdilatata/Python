import osmnx as ox
import folium
import pandas as pd

# 1. Získání dat pro město Kassel
place_name = "Kassel, Germany"
graph = ox.graph_from_place(place_name, network_type='drive')

# 2. Převod hran (silnic) na GeoDataFrame
edges = ox.graph_to_gdfs(graph, nodes=False, edges=True)

# 3. Vytvoření pomocné funkce pro převod lanes na číslo
def parse_lanes(value):
    try:
        if isinstance(value, list):
            value = value[0]
        # Odstraní např. hodnoty jako '2;3' nebo '2.5'
        value = str(value).split(';')[0].strip()
        return int(value)
    except:
        return None

edges['lanes_num'] = edges['lanes'].apply(parse_lanes)

# 4. Filtrování silnic se dvěma a více pruhy
multi_lane_roads = edges[edges['lanes_num'] >= 2]

# 5. Vykreslení mapy
center = multi_lane_roads.geometry.unary_union.centroid
m = folium.Map(location=[center.y, center.x], zoom_start=13)

for _, row in multi_lane_roads.iterrows():
    if row.geometry.geom_type == 'LineString':
        points = [(lat, lon) for lon, lat in row.geometry.coords]
        folium.PolyLine(points, color='orange', weight=3, opacity=0.8).add_to(m)
    elif row.geometry.geom_type == 'MultiLineString':
        for line in row.geometry:
            points = [(lat, lon) for lon, lat in line.coords]
            folium.PolyLine(points, color='orange', weight=3, opacity=0.8).add_to(m)

# 6. Uložení mapy
m.save("kassel_viceproude_silnice.html")
