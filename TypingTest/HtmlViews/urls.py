from django.conf.urls import url
from HtmlViews import views
from django.conf import settings
from django.urls import path 

urlpatterns = [
    url(r'^$',views.htmlhello, name='index'),
    url('index/', views.htmlhello),  
]