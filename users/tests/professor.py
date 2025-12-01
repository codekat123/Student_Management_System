from django.test import override_settings
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken
from django.utils import timezone
from ..models import Professor


User = get_user_model()



class ProfessorAPITest(APITestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser(
            national_id="9384456475938475",
            password="test1234",
            is_active=True,
            is_staff=True,
            is_superuser=True
            )

        token = AccessToken.for_user(self.admin)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {str(token)}")
        
        self.professor = Professor.objects.create_user(
            national_id="984334039265492",
            full_name="Ahmed Gaber",
            password="9348753409587",

        )

     
    def test_professor_create(self):
                 
        url = reverse("users:professor-create")
        payload = {
            "national_id":"984334534265492",
            "full_name":"Ahmed Gaber",
            "password":"9348753409587",

        }
        response = self.client.post(url,payload,format='json')
        self.assertEqual(status.HTTP_201_CREATED,response.status_code)
    
    def test_professor_update(self):
        url = reverse("users:professor-update-admin",kwargs={'pk':self.professor.id})
        payload = {
            "full_name":"test38"
        }
        response = self.client.put(url,payload,format='json')

        # print(response.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    def test_list_professor(self):
        url = reverse("users:professor-list")
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK,response.status_code)
    
    def rest_detail_professor(self):
        url = reverse("users:professor-detail-admin",kwargs={'pk':self.professor.id})
        response = self.client.get(url)
        self.assertEqual(response.status,status.HTTP_200_OK)

    def test_delete_professor(self):
        url = reverse("users:professor-destroy",kwargs={'pk':self.professor.id})
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_204_NO_CONTENT,response.status_code)