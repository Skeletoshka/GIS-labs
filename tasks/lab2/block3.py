import geopandas as gpd
import matplotlib.pyplot as plt


def readFiles(path):
    cities = gpd.read_file(path + r'\cities.shp')
    rivers = gpd.read_file(path + r'\rivers.shp')
    territory = gpd.read_file(path + r'\territory.shp')
    cities = cities.to_crs(32639)
    rivers = rivers.to_crs(32639)
    territory = territory.to_crs(32639)
    fig, axes = plt.subplots(figsize=(15, 8))
    territory['geometry'].plot(ax=axes, color='green')
    territory = territory.geometry.unary_union
    rivers = rivers[rivers.geometry.within(territory)]
    cities = cities[cities.geometry.within(territory)]
    cities['geometry'].plot(ax=axes, color='black', alpha=0.5, markersize=10)
    rivers['geometry'].plot(ax=axes, color='blue', alpha=0.3)
    axes.set_title('World Map')
    plt.show()