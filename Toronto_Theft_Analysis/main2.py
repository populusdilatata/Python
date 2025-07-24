import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import MarkerCluster

# 1. Načtení dat
bike_data = pd.read_csv("data/Cleaned_Bicycle_Thefts_Open_Data.csv")

# --- Úkol 1: Nejvíce a nejméně krádeží kol dle čtvrtletí ---
quarter_counts = bike_data.groupby('quarter').size().reset_index(name='total_per_quarter')

# Graf
plt.figure(figsize=(8, 5))
sns.scatterplot(data=quarter_counts, x='quarter', y='total_per_quarter', s=100)
sns.lineplot(data=quarter_counts, x='quarter', y='total_per_quarter', linewidth=2)
plt.title("Quarterly Trends in Bike Thefts")
plt.ylabel("The Number of Stolen Bikes")
plt.xlabel("Quarter")
plt.show()

high = "Q3"
low = "Q1"

# --- Úkol 2: Nejčastější lokace ---
location_counts = bike_data.groupby('location').size().reset_index(name='total_per_location')
location_counts['percentage_per_location'] = location_counts['total_per_location'] / location_counts['total_per_location'].sum()

plt.figure(figsize=(6, 6))
plt.pie(
    location_counts['percentage_per_location'],
    labels=location_counts['location'],
    autopct=lambda p: f'{p:.1f}%' if p > 2 else '',
    startangle=140
)
plt.title("Number of Bikes Across Different Location Types")
plt.axis('equal')
plt.show()

location = "Residential Structures"
percentage = 0.5

# --- Úkol 3: Region s nejvyšší mediánovou hodnotou kol ---
neighborhood_stats = bike_data.groupby('neighborhood').agg({
    'long': 'mean',
    'lat': 'mean',
    'bike_cost': lambda x: x.median(skipna=True)
}).reset_index().rename(columns={'bike_cost': 'median_value'})

# Filtrování na platné souřadnice
neighborhood_stats = neighborhood_stats.dropna(subset=['lat', 'long'])

# Vytvoření folium mapy
toronto_map = folium.Map(location=[43.7, -79.4], zoom_start=11)
marker_cluster = MarkerCluster().add_to(toronto_map)

# Přidání markerů podle hodnoty kol
for _, row in neighborhood_stats.iterrows():
    popup_text = f"<b>{row['neighborhood']}</b><br>Median Value: ${row['median_value']:.0f}"
    folium.CircleMarker(
        location=(row['lat'], row['long']),
        radius=6,
        color='blue',
        fill=True,
        fill_opacity=0.7,
        popup=popup_text
    ).add_to(marker_cluster)

# Zvýraznění nejdražší čtvrti
top_region = neighborhood_stats.loc[neighborhood_stats['median_value'].idxmax()]
folium.Marker(
    location=(top_region['lat'], top_region['long']),
    popup=f"<b>{top_region['neighborhood']}</b><br><b>HIGHEST MEDIAN VALUE</b>: ${top_region['median_value']:.0f}",
    icon=folium.Icon(color='red', icon='info-sign')
).add_to(toronto_map)

# Uložení do HTML
toronto_map.save("toronto_bike_thefts_map.html")

# Výpis doporučení
action = (
    "In summer (Q3), the demand for outdoor bicycles increases, leading to the highest number of bike thefts. "
    "Approximately 50% of these thefts occur in residential areas. People should be more vigilant when locking their bikes. "
    "In particular, the Bridle Path-Sunnybrook-York Mills region experiences the highest theft values, "
    "so residents and those nearby should exercise extra caution."
)

# Výstup
print(f"Highest quarter: {high}")
print(f"Lowest quarter: {low}")
print(f"Most frequent location: {location} ({percentage*100:.1f}%)")
print(f"Region with highest median value: {top_region['neighborhood']}")
print("Recommended action:\n", action)
