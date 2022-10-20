from django.urls import path
from .views import (
    # StatusAPIView,
    # StatusListAPIView,
    # StatusCreateAPIView,
    # StatusDetailAPIView,
    # StatusUpdateAPIView,
    # StatusDeleteAPIView,
    #StatusListCreateView,
    #StatusDetailUpdateDeleteAPIView,
    StatusListCreateDetailUpdateDeleteAPIView
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'status', StatusListCreateDetailUpdateDeleteAPIView, basename="status")

urlpatterns = [
    # path('status/', StatusAPIView.as_view()),
    # path('status/list/', StatusListAPIView.as_view()),
    # path('status/create/', StatusCreateAPIView.as_view()),
    #path('status/', StatusListCreateView.as_view()),
    # path('status/detail/<id>/', StatusDetailAPIView.as_view()),
    # path('status/update/<pk>/', StatusUpdateAPIView.as_view()),
    # path('status/delete/<id>/', StatusDeleteAPIView.as_view()),
    #path('status/<id>/', StatusDetailUpdateDeleteAPIView.as_view()),
] + router.urls