from django.shortcuts import render,redirect

import location
from folium.plugins import HeatMap
from .models import locate
import folium

def save_location(request):
    if request.method == "POST":
        form = request.POST
        long = form.get('long')
        lat = form.get('lat')
        insert_data = locate.objects.create(long=long,lat=lat)
        return redirect('loc/')
    return render(request, 'index.html')

def mapping(request):
    a = locate.objects.get(id=15)
    long= a.long
    lat = a.lat
    data = [[24.78, 80.89, 8.76]]

    # mapp = folium.Map(location=[long,lat])
    m=folium.Map(location=[long, lat] ,zoom_start=3,maptype="satellite")
    tile = folium.TileLayer(
        tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr = 'Esri',
        name = 'Esri Satellite',
        overlay = False,
        control = True
       ).add_to(m)
    HeatMap(data).add_to(m)
    output = 'templates/aa.html'
    abc = m.save(output)

    # b = locate.objects.get('lat')
    return render(request, 'aa.html')