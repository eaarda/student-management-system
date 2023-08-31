from django.urls import path, include
from rest_framework import routers

from .views import CourseViewSet, StudentGradeViewSet


router = routers.DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'grades', StudentGradeViewSet)


urlpatterns = [
    path('', include(router.urls)),
]