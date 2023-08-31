from rest_framework import serializers
from apps.base.serializers import BaseSerializer

from .models import CustomUser, Student, Teacher


class UserSerializer(BaseSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'password', 'user_type']
        extra_kwargs = {'password': {'write_only': True}}


class StudentSerializer(BaseSerializer):
    courses = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'user', 'first_name', 'last_name', 'birth_date', 'courses']
    
    def get_courses(self, obj):
        courses = obj.courses.all()
        course_data = [{'id':course.id, 'name': course.name, 'semester': course.get_semester_display()} for course in courses]
        return course_data


class StudentLiteSerializer(BaseSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name']


class TeacherSerializer(BaseSerializer):
    courses = serializers.SerializerMethodField()
    
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'courses']
    
    def get_courses(self, obj):
        courses = obj.course_set.all()
        course_data = [{'id':course.id, 'name': course.name, 'semester': course.get_semester_display()} for course in courses]
        return course_data