from gym.models import Workout
from rest_framework import serializers


class WorkoutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'
