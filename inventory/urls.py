from inventory import views
from django.conf.urls import url

app_name = 'inventory'

urlpatterns = [
    url(r'^list_inventory/$',views.listInventory,name='list_inventory')
]
