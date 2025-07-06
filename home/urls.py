from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('sell/',views.sell,name='sell'),
    path('calci/',views.calci,name='calci'),
    path('apron/',views.apron,name='apron'),
    path('etb/',views.etb,name='etb'),
    path('projects/',views.projects,name='projects'),
    path('other/',views.others,name='others'),
    path('order/<int:product_id>/', views.order_view, name='order'),
]
