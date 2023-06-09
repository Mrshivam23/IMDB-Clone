from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import *

router = DefaultRouter()
router.register('stream', StreamPlatformVS,basename ='streamplatform')
urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchListDetailAV.as_view(), name='movie-detail'),
    path('',include(router.urls)),
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name = 'Review-create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name = 'Review-list'),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name = 'Review-detail'),
    path('reviews/', UserReview.as_view(), name = 'user-review-detail'),
    path('list2/', WatchListGV.as_view(), name = 'watch-detail'),
    # path('stream/', StreamPlatformAV.as_view(), name = 'Stream'),
    # path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name = 'Stream-detail'),
    # path('review/',ReviewList.as_view(), name = 'Review-list'),
    # path('review/<int:pk>',ReviewDetail.as_view(), name = 'Review-detail'),
    
    
]