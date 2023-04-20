from rest_framework.throttling import UserRateThrottle


class ReviewCreateThrottle(UserRateThrottle):
    scope = 'review-create'
    
class RevieListThrottle(UserRateThrottle):
    scope = 'review-list'