from gym.models import *
from rest_framework import serializers
import json

#Relations
#http://www.django-rest-framework.org/api-guide/relations/#serializer-relations

class WorkoutSerializer(serializers.ModelSerializer):
	
	sets = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	
	class Meta:
		model = Workout
		fields = ('id','name','start_time','end_time','location','sets') 
		
class SetSerializer(serializers.ModelSerializer):
	
	#Example
	excercise_id = serializers.SerializerMethodField()
	
	class Meta:
		model = Set
		fields = ('id','workout','excercise','reps','weight','excercise_id') #'excercise
		depth = 0
	
	#Example
	def get_excercise_id(self, obj):
		pair = {"url":"http://asd.com"}
		jsonStr = json.dumps(pair)
		return obj.excercise.id


class ExcerciseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Excercise
		fields = ('id','excercise','muscle_group','lever','mass_share')

class MuscleGroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = MuscleGroup
		fields = ('id','muscle_group')
