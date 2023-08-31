import json, random
from pathlib import Path
from decimal import Decimal

from apps.user.models import Teacher, Student
from apps.course.models import Course, StudentCourseEnrollment, StudentGrade


class CourseMock():


    def _create_courses(self):

        WORKING_DIR = Path(__file__).resolve().parent

        with open("{}/courses.json".format(WORKING_DIR), encoding="utf8") as json_file:
            courses = json.load(json_file)
            teachers = Teacher.objects.all()

            for course, teacher in zip(courses, teachers):
                course = Course.objects.get_or_create(
                    name=course['name'],
                    semester=course['semester'],
                    teacher=teacher
                )
    

    def _create_student_course_enrollment(self):
        students = Student.objects.all()
        courses = Course.objects.all()

        for student in students:
            if len(student.studentcourseenrollment_set.all()) < 2:
                for i in range(3):
                    course = random.choice(courses)
                    StudentCourseEnrollment.objects.get_or_create(student=student, course=course)
    

    def _create_enrollment_grade(self):
        enrollments = StudentCourseEnrollment.objects.order_by('?')[:20]

        for enrollment in enrollments:
            grade = Decimal(random.uniform(0, 100)) 
            StudentGrade.objects.get_or_create(enrollment=enrollment, grade=grade)


    def execute(self):
        self._create_courses()
        self._create_student_course_enrollment()
        self._create_enrollment_grade()