from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from apps.base.serializers import BaseSerializer
from apps.user.models import Student
from apps.user.serializers import StudentLiteSerializer
from .models import Course, StudentGrade



class StudentCourseEnrollmentSerializer(BaseSerializer, WritableNestedModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name')


class StudentCourseEnrollmentLiteSerializer(serializers.Serializer):
    student_id = serializers.IntegerField()


class CourseSerializer(BaseSerializer, WritableNestedModelSerializer):
    # students = StudentCourseEnrollmentSerializer(many=True, allow_null=True, required=False, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'created_at', 'name', 'semester', 'teacher']
    
    def validate_teacher(self, teacher):
        if teacher is not None and int(teacher.user.user_type) != 2:
            raise serializers.ValidationError("Teacher must have user_type 2")
        return teacher


class CourseLiteSerializer(BaseSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name']


class StudentGradeSerializer(BaseSerializer):
    student = StudentLiteSerializer(source='enrollment.student', read_only=True)
    course = CourseLiteSerializer(source='enrollment.course', read_only=True)

    class Meta:
        model = StudentGrade
        fields = '__all__'


class StudentGradeLiteSerializer(BaseSerializer):
    course = CourseLiteSerializer(source='enrollment.course', read_only=True)

    class Meta:
        model = StudentGrade
        fields = '__all__'