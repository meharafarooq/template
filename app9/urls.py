from django.urls import path
from.import views
app_name='app9'
urlpatterns=[
    path('',views.index,name='index'),
]