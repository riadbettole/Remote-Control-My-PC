# In shutdown_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('lock_screen/', views.lockscreen, name='Lock the Screen'),
    path('shut_down/', views.shutdown, name='Shut down the Computer'),
    path('move_mouse/<int:x>/<int:y>', views.move_mouse, name='Move The Mouse'),
    path('set_volume/<int:volume>/', views.set_volume, name='Volume'),
    path('coordinates/', views.coordinates_view, name='coordinates'),
    path('send-coordinates/', views.send_coordinates, name='coordinates'),
    path('right_click/', views.right_click_mouse, name='right_click'),
    path('left_click/', views.left_click_mouse, name='left_click'),
]