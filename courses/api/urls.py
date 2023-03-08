from django.urls import path, include
from rest_framework import routers

from .views import SubjectList, SubjectDetail, CourseViewSet

router = routers.DefaultRouter()
router.register("courses", CourseViewSet)

app_name = "courses"
urlpatterns = [
    path("subjects/", SubjectList.as_view(), name="subject_list"),
    path("subjects/<int:pk>/", SubjectDetail.as_view(), name="subject_detail"),
    # path("courses/<pk>/enroll/", CourseEnrollView.as_view(), name="course_enroll"),
    path("", include(router.urls)),
]
