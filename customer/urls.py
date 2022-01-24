from customer import views
from django.conf.urls import url

app_name = 'customer'

urlpatterns = [
    url(r'^list_customer/$',views.listCustomer,name='list_customer'),
    url(r'^create_customer/$',views.createCustomer,name='create_customer')
]
