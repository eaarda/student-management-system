from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from apps.base.permissions import IsStudentUser
from apps.base.views import BaseModelViewSet
from .models import Course, StudentGrade, Student
from .serializers import CourseSerializer, StudentGradeSerializer, StudentCourseEnrollmentLiteSerializer, StudentGradeLiteSerializer


class CourseViewSet(BaseModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    search_fields = ['name']
    permission_classes = [IsAdminUser | IsStudentUser]

    @action(detail=True, methods=['post'], serializer_class=StudentCourseEnrollmentLiteSerializer)
    def enroll(self, request, pk=None):
        course = self.get_object()
        student_id = request.data.get('student_id')
        try:
            student = Student.objects.get(id=student_id)
            course.students.add(student)
            return Response({"message": f"Student {student} has been enrolled in the course {course}"}, status=201)
        except Student.DoesNotExist:
            return Response({"message": "Student not found"}, status=404)
    
    @action(detail=True, methods=['post'])
    def disenroll(self, request, pk=None):
        course = self.get_object()
        student_id = request.data.get('student_id')
        try:
            student = Student.objects.get(id=student_id)
            course.students.remove(student)
            return Response({"message": f"Student {student} has been disenrolled from the course {course}"}, status=200)
        except Student.DoesNotExist:
            return Response({"message": "Student not found"}, status=404)


class StudentGradeViewSet(BaseModelViewSet):
    queryset = StudentGrade.objects.all()
    serializer_class = StudentGradeSerializer
    permission_classes = [IsAdminUser | IsStudentUser]
    filterset_fields = ['grade', 
                        'enrollment__student__id',
                        'enrollment__student__first_name', 
                        'enrollment__student__last_name',
                        'enrollment__course__id',
                        'enrollment__course__name']
    ordering_fields = [ 'grade', 
                        'enrollment__student__id',
                        'enrollment__student__first_name', 
                        'enrollment__student__last_name',
                        'enrollment__course__id',
                        'enrollment__course__name']
    search_fields = [   'grade', 
                        'enrollment__student__id',
                        'enrollment__student__first_name', 
                        'enrollment__student__last_name',
                        'enrollment__course__id',
                        'enrollment__course__name']
    
    # Students can only view their own grades but admin can see all grades
    def list(self, request):
        if int(request.user.user_type) == 3:
            queryset = self.queryset.filter(enrollment__student=request.user.student)
            serializer = StudentGradeLiteSerializer(queryset, many=True)
            return Response(serializer.data)
        return super().list(request)
    
    def retrieve(self, request, *args, **kwargs):
        if int(request.user.user_type) == 3:
            queryset = StudentGrade.objects.filter(enrollment__student=request.user.student)
            user_grade = get_object_or_404(queryset, pk=kwargs['pk'])
            serializer = StudentGradeLiteSerializer(user_grade)
            return Response(serializer.data)
        return super().retrieve(request, *args, **kwargs)

