from gym.models import *
from rest_framework import serializers
import json

class WorkoutSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Workout
		fields = ('id','name','start_time','end_time','location') 
		
class SetSerializer(serializers.HyperlinkedModelSerializer):
	
	#Example
	excercise_id = serializers.SerializerMethodField()
	
		
	class Meta:
		model = Set
		fields = ('id','workout','reps','weight','excercise_id') #'excercise
	
	#Example
	def get_excercise_id(self, obj):
		pair = {"url":"http://asd.com"}
		jsonStr = json.dumps(pair)
		return obj.excercise.id

class ExcerciseSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Excercise
		fields = ('id','excercise','muscle_group','lever','mass_share')

class MuscleGroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = MuscleGroup
		fields = ('id','muscle_group')
