from django.urls import path, include
from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

from .views import StudentViewSet, TeacherViewSet


router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)


urlpatterns = [
    path('', include(router.urls)),

    path('login', TokenObtainPairView.as_view(), name="login")
]