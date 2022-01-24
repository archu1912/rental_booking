from vehicle import views as vehicle_view
from django.conf.urls import url

app_name = 'vehicle'

urlpatterns = [
    url(r'^list_vehicle/$',vehicle_view.listVehicle,name='list_vehicle')
]
