from rest_framework import serializers
from .models import AttendanceSession,AttendanceRecord
from django.utils import timezone


class AttendanceSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceSession
        fields = [
            "id",
            "lecture_offering",
            "start_time",
            "end_time",
            "date",
        ]
        read_only_fields = ["id"]

    def validate(self, attrs):
        if attrs["session_date"] < timezone.now().date():
            raise serializers.ValidationError("Session date can't be in the past.")
        return attrs

class AttendanceRecordListSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source="student.full_name", read_only=True)

    class Meta:
        model = AttendanceRecord
        fields = [
            "id",
            "attendance_session",
            "student",
            "student_name",
            "status",
        ]
        read_only_fields = ["id", "timestamp"]


