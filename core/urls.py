from django.urls import path
from . import views
from .views import (
    TrackListView,  
    TrackDetailView,
    TrackCreateView,
    TrackUpdateView,
    TrackDeleteView,
    home
)

#name allows me to create a url pattern of a given name
#ex: in html, saying {% url 'track_list' %} generates /records/
#name is used for navigation links in templates

urlpatterns = [
    path('', home, name='home'),
    path("records/", TrackListView.as_view(), name="track_list"),
    path('records/<int:pk>/', TrackDetailView.as_view(), name='track_detail'),
    
    path('records/add/', TrackCreateView.as_view(), name='track_add'),
    path('records/<int:pk>/edit/', TrackUpdateView.as_view(), name='track_edit'),
    path('records/<int:pk>/delete/', TrackDeleteView.as_view(), name='track_delete'),
    path('analytics/', views.analytics, name='analytics'),
    path('fetch/', views.fetch_data_view, name='fetch_data'),
]
