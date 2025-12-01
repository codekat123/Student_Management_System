from rest_framework import serializers
from ..models import Student



class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
        extra_kwargs = {
            'full_name': {'required': False},
            'phone_number': {'required': False},
            'governorate': {'required': False},
            'location': {'required': False},
            'password': {'required': False},
            'national_id':{'required':False},
            'year':{'required':False}
        }


class StudentListSerializer(serializers.ModelSerializer):
     class Meta:
          model = Student
          fields = ['full_name','national_id','year']