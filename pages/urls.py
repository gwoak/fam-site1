from django.urls import path
from .views import HomePageView, PageView, KPageView, TreePageView


urlpatterns = [
    
   path('', HomePageView.as_view(), name='home'),
   path('page/graham_page', PageView.as_view(), name='graham_page'), 
   path('page/karin_page', KPageView.as_view(), name='karin_page'),
   path('page/tree', TreePageView.as_view(), name='tree')
    
]