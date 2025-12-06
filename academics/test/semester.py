from rest_framework.test import APITestCase
from rest_framework import status
from django.test import override_settings
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken
from django.utils import timezone
from datetime import timedelta
from ..models import Semester


User = get_user_model()

class SemesterTest(APITestCase):

     def setUp(self):
          self.admin = User.objects.create_superuser(
               national_id="9384456475938475",
               password="password13243",
               is_active=True,
               is_staff=True,
               is_superuser=True,
          )
          token = AccessToken.for_user(self.admin)
          self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {str(token)}")

     def test_create_semester(self):
          url = reverse("academics:semester-list")
          payload = {
               "name":"fall",
               "start_date":timezone.now().date().isoformat(),
               "end_date": timezone.now().date().isoformat(),
          }
          response = self.client.post(url,payload,format='json')
          # print(response.data)
          self.assertEqual(status.HTTP_201_CREATED,response.status_code)
     def test_update_semester(self):
          semester = Semester.objects.create(
               name='winter',
               start_date=timezone.now().date().isoformat(),
               end_date=timezone.now().date().isoformat(),
          )
          url = reverse("academics:semester-detail",kwargs={"pk":semester.pk})

          payload = {
               "name":"summer",
               "start_date":timezone.now().date().isoformat(),
               "end_date": timezone.now().date().isoformat(),
          }
          response = self.client.put(url,payload,format='json')
          self.assertEqual(status.HTTP_200_OK,response.status_code)
     def test_delete_semester(self):
          semester = Semester.objects.create(
               name="springs",
               start_date=timezone.now().date().isoformat(),
               end_date=timezone.now().date().isoformat(),
          )
          url = reverse("academics:semester-detail",kwargs={"pk":semester.pk})
          
          response = self.client.delete(url)
          self.assertEqual(status.HTTP_204_NO_CONTENT,response.status_code)
     