from rest_framework import serializers
from .models import User, EnrolledBatches
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'age', 'dob', 'phone')

class EnrolledBatchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnrolledBatches
        fields = ('id', 'user', 'batch', 'month', 'payment_status')
