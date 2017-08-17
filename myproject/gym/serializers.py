from gym.models import *
from rest_framework import serializers


class WorkoutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Workout
        fields = ('id','name','start_time','end_time','location') 
		
class SetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Set
        fields = ('id','excercise','workout','reps','weight')

class ExcerciseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Excercise
        fields = ('id','excercise','muscle_group','lever','mass_share')

class MuscleGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MuscleGroup
        fields = ('id','muscle_group')
