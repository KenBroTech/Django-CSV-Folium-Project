from django.shortcuts import render
from .models import Data
import folium
from folium import plugins, raster_layers
from django_pandas.io import read_frame
# Create your views here.


def index(request):
    m = folium.Map(location=[19, 12], zoom_start=2)

    map1 = raster_layers.TileLayer(tiles='CartoDB Dark_Matter').add_to(m)
    map2 = raster_layers.TileLayer(tiles='CartoDB Positron').add_to(m)
    map3 = raster_layers.TileLayer(tiles='Stamen Terrain').add_to(m)
    map4 = raster_layers.TileLayer(tiles='Stamen Toner').add_to(m)
    map5 = raster_layers.TileLayer(tiles='Stamen Watercolor').add_to(m)
    folium.LayerControl().add_to(m)
    qs = Data.objects.all()
    df = read_frame(qs, fieldnames=['country',
                                    'latitude', 'longitude', 'population'])
    # print(df)
    for (index, rows) in df.iterrows():
        folium.Marker(location=[rows.loc['latitude'],
                                rows.loc['longitude']], popup=rows.loc['population']).add_to(m)

    plugins.Fullscreen().add_to(m)
    m = m._repr_html_()

    context = {
        'm': m
    }
    return render(request, 'dashboard/index.html', context)
