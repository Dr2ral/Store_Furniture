
from django.urls import path
from goods import views

app_name = 'mgoods'

urlpatterns = [
    path('', views.catalog, name='index'),
    path('product/', views.product, name='product'),

]