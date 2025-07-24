import osmnx as ox
import folium

# 1. Získání geografického středu Kasselu
center_point = ox.geocode("Kassel, Germany")

# 2. Načtení silniční sítě v okruhu 15 km
graph = ox.graph_from_point(center_point, dist=15000, network_type='drive')

# 3. Převod hran (silnic) na GeoDataFrame
edges = ox.graph_to_gdfs(graph, nodes=False, edges=True)

# 4. Pomocná funkce: převede atribut 'lanes' na celé číslo
def parse_lanes(value):
    try:
        if isinstance(value, list):
            value = value[0]
        value = str(value).split(';')[0].strip()
        return int(value)
    except:
        return None

edges['lanes_num'] = edges['lanes'].apply(parse_lanes)

# 5. Filtrování:
# - silnice s lanes >= 2
# - NEBO dálnice (i bez uvedeného počtu pruhů)
filtered_edges = edges[
    (edges['lanes_num'] >= 2) |
    (edges['highway'].isin(['motorway', 'motorway_link']))
]

# 6. Vykreslení mapy
center = filtered_edges.geometry.unary_union.centroid
m = folium.Map(location=[center.y, center.x], zoom_start=12)

# 7. Přidání zvýrazněných silnic
for _, row in filtered_edges.iterrows():
    color = 'orange' if row.get('highway') in ['motorway', 'motorway_link'] else 'blue'
    weight = 4 if row.get('highway') in ['motorway', 'motorway_link'] else 2

    if row.geometry.geom_type == 'LineString':
        points = [(lat, lon) for lon, lat in row.geometry.coords]
        folium.PolyLine(points, color=color, weight=weight, opacity=0.8).add_to(m)

    elif row.geometry.geom_type == 'MultiLineString':
        for line in row.geometry:
            points = [(lat, lon) for lon, lat in line.coords]
            folium.PolyLine(points, color=color, weight=weight, opacity=0.8).add_to(m)

# 8. Uložení do HTML
m.save("kassel_dvou_a_viceproude_silnice.html")
