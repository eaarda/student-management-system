from django.db import models

from apps.base.models import BaseModel
from apps.user.models import Teacher, Student


class Course(BaseModel):
    SEMESTER_CHOICES = (
        (1, 'Spring'),
        (2, 'Summer'),
        (3, 'Fall'),
    )

    name = models.CharField(max_length=150)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    semester = models.IntegerField(choices=SEMESTER_CHOICES)

    students = models.ManyToManyField(Student, related_name='courses', through='StudentCourseEnrollment')

    def __str__(self):
        return self.name


class StudentCourseEnrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class StudentGrade(BaseModel):
    enrollment = models.ForeignKey(StudentCourseEnrollment, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.enrollment.student} - {self.enrollment.course} - Grade: {self.grade}"