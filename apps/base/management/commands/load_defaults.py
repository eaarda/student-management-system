from typing import Any, Optional
from django.core.management.base import BaseCommand, CommandError

from .users_mock import UserMock
from .courses_mock import CourseMock


class Command(BaseCommand):

    def handle(self, *args, **options):
        UserMock().execute()
        CourseMock().execute()