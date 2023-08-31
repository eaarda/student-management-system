from rest_framework import viewsets, serializers, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from apps.base.views import BaseModelViewSet
from .models import Student, Teacher
from .serializers import UserSerializer, StudentSerializer, TeacherSerializer


class StudentViewSet(BaseModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdminUser]
    search_fields = ['first_name', 'last_name']

    def create(self, request, *args, **kwargs):
        required_fields = ['email', 'password', 'first_name', 'last_name', 'birth_date']
        missing_fields = {}
        for field in required_fields:
            if not request.data.get(field):
                missing_fields[field] = ['This field is required.']
        if missing_fields:
            raise serializers.ValidationError(missing_fields)
        
        user_data = {
            'email': request.data.get('email'),
            'password': request.data.get('password'),
            'user_type': 3
        }
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            user.set_password(user_data['password'])
            user.save()
            student_data = {
                'user': user.id,
                'first_name': request.data.get('first_name'),
                'last_name': request.data.get('last_name'),
                'birth_date': request.data.get('birth_date')
            }
            student_serializer = StudentSerializer(data=student_data)
            if student_serializer.is_valid():
                student_serializer.save()
                return Response(student_serializer.data, status=status.HTTP_201_CREATED)
            else:
                user.delete()
                return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data_dict = request.data.dict()
        data_dict['user'] = instance.user.id
        serializer = self.get_serializer(instance, data=data_dict, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user = instance.user 
        self.perform_destroy(instance)  
        user.delete() 
        return Response(status=status.HTTP_204_NO_CONTENT)


class TeacherViewSet(BaseModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    http_method_names = ['get']
    permission_classes = [IsAdminUser]
    search_fields = ['first_name', 'last_name']
