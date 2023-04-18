from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import *

router = DefaultRouter()
router.register('stream', StreamPlatformVS,basename ='streamplatform')
urlpatterns = [
    path('list/', WatchListListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchListDetailAV.as_view(), name='movie-detail'),
    
    path('',include(router.urls)),
    
    # path('stream/', StreamPlatformAV.as_view(), name = 'Stream'),
    # path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name = 'Stream-detail'),
    
    # path('review/',ReviewList.as_view(), name = 'Review-list'),
    # path('review/<int:pk>',ReviewDetail.as_view(), name = 'Review-detail'),
    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name = 'Review-create'),
    
    path('stream/<int:pk>/review', ReviewList.as_view(), name = 'Review-list'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name = 'Review-detail'),

    # path('review/<int:pk>',ReviewDetail.as_view(), name = 'Review-detail'),
    
]