from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import *
urlpatterns = [
    path('list/', WatchListListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchListDetailAV.as_view(), name='movie-detail'),
    path('stream/', StreamPlatformAV.as_view(), name = 'Stream'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name = 'Stream-detail'),
    path('review/',ReviewList.as_view(), name = 'Review-list'),
    
    path('stream/<int:pk>/review', StreamPlatformDetailAV.as_view(), name = 'Stream-detail'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name = 'Stream-detail'),

    # path('review/<int:pk>',ReviewDetail.as_view(), name = 'Review-detail'),
    
]