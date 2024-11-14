from django.urls import path
from . import views
app_name = 'sochuyentruong'
urlpatterns=[
    path('',views.index, name='index')
]