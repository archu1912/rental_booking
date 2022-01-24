from booking import views
from django.conf.urls import url

app_name = 'booking'

urlpatterns = [
    url(r'^list_booking/$',views.listBooking,name='list_booking'),
    url(r'^create_booking/$',views.createBooking,name='create_booking'),
    url(r'^edit_booking/(?P<id>[0-9]+)/$',views.updateBooking,name='edit_booking')
]
