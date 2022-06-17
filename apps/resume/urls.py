from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('send-email', views.send_email, name='send_email'),
    path('send-grid-email', views.send_grid_email, name='send_grid_email'),

    # Contact end point
    path('contact/<platform>', views.contact, name='contact'),

]
