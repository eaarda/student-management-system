import json
from pathlib import Path

from apps.user.models import CustomUser, Student, Teacher


class UserMock():

    def _create_admin(self):

        user, created = CustomUser.objects.get_or_create( email='admin@admin.com', 
                                                          user_type=1,
                                                          is_admin=True,
                                                          is_active=True,
                                                          is_staff=True,
                                                          is_superuser=True)
        password = f"admin1234"
        user.set_password(password)
        user.save()

    def _create_teachers(self):

        WORKING_DIR = Path(__file__).resolve().parent

        with open("{}/teachers.json".format(WORKING_DIR), encoding="utf8") as json_file:
            data = json.load(json_file)

            for i in data:
                user, created = CustomUser.objects.get_or_create(email=i['email'], user_type=2)
                password = f"{i['first_name'].lower()}1234"
                user.set_password(password)
                user.save()

                Teacher.objects.get_or_create(user=user, first_name=i['first_name'], last_name=i['last_name'])
    

    def _create_students(self):

        WORKING_DIR = Path(__file__).resolve().parent

        with open("{}/students.json".format(WORKING_DIR), encoding="utf8") as json_file:
            data = json.load(json_file)

            for i in data:
                user, created = CustomUser.objects.get_or_create(email=i['email'], user_type=3)
                password = f"{i['first_name'].lower()}1234"
                user.set_password(password)
                user.save()

                Student.objects.get_or_create(user=user, first_name=i['first_name'], last_name=i['last_name'], birth_date=i['birth_date'])





    def execute(self):
        self._create_admin()
        self._create_teachers()
        self._create_students()