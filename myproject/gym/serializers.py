from gym.models import *
from rest_framework import serializers
import json

#Relations
#http://www.django-rest-framework.org/api-guide/relations/#serializer-relations

def get_next(object, model):
	id = object.id
	all = model.objects.all()
	#Find greater than
	gt = all.filter(id__gt=id).order_by('id')
	if(len(gt)==0):
		#If no bigger ids exist, take the first id
		firstObj = all.order_by('id')[0]
		nextId = firstObj.id
	else:
		nextObj = gt[0]
		nextId = nextObj.id
	return nextId
		
def get_prev(object, model):
	id = object.id
	all = model.objects.all() 
	#Find less than
	lt = all.filter(id__lt=id).order_by('-id')
	if(len(lt)==0):
		#If no smaller ids exist, take the last id
		lastObj = all.order_by('-id')[0]
		prevId = lastObj.id 
	else:
		prevObj = lt[0]
		prevId = prevObj.id
	return prevId

class WorkoutSerializer(serializers.ModelSerializer):
	
	sets = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	
	class Meta:
		model = Workout
		fields = ('id','name','start_time','end_time','location','sets')


class ExcerciseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Excercise
		fields = ('id','excercise','muscle_group','lever','mass_share')
		
class SetSerializer(serializers.ModelSerializer):
	
	#Example
	excercise_obj = ExcerciseSerializer(source='excercise')
	
	
	class Meta:
		model = Set
		fields = ('id','workout','excercise_obj','reps','weight') #'excercise
		depth = 0
	
	#Example
	def get_excercise_id(self, obj):
		pair = {"url":"http://asd.com"}
		jsonStr = json.dumps(pair)
		return obj.excercise.id

class MuscleGroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = MuscleGroup
		fields = ('id','muscle_group')


#Return a single workout together with all related sets		
class WorkoutSetsSerializer(serializers.ModelSerializer):

	sets = SetSerializer(many=True, read_only=True)
	next_id = serializers.SerializerMethodField(read_only=True)
	prev_id = serializers.SerializerMethodField(read_only=True)
	
	class Meta:
		model = Workout
		fields = ('id','name','start_time','end_time','location','sets','prev_id', 'next_id')
		
	def get_next_id(self, obj):
		return get_next(obj, Workout)
		
	def get_prev_id(self, obj):
		return get_prev(obj, Workout)

