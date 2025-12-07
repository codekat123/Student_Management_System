from rest_framework import serializers
from .models import Enrollment


class EnrollmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'lecture_offering', 'status', 'stamptime']
        read_only_fields = ['id', 'stamptime']
    
    def validate(self, attrs):
        student = attrs['student']
        lecture_offering = attrs['lecture_offering']

        if Enrollment.objects.filter(student=student, lecture_offering=lecture_offering).exists():
            raise serializers.ValidationError("Student already enrolled in this lecture.")
        
        return attrs
