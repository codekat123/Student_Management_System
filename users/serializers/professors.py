from rest_framework import serializers
from ..models import Professor


class ProfessorCreateSerializer(serializers.ModelSerializer):
     class Meta:
          model = Professor
          fields = '__all__'
          read_only_fields = ['id','updated_at','created_at']
          extra_kwargs = {
            'full_name': {'required': False},
            'phone_number': {'required': False},
            'governorate': {'required': False},
            'location': {'required': False},
            'password': {'required': False},
            'national_id':{'required':False},
            'academic_title':{'required':False},
            'office_location':{'required':False}
        }



class ProfessorListSerializer(serializers.ModelSerializer):
     class Meta:
          model = Professor
          fields = ['full_name','academic_title',]
