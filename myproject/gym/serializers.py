from gym.models import *
from rest_framework import serializers
import json
from gym.functions import *

#Relations
#http://www.django-rest-framework.org/api-guide/relations/#serializer-relations


class ExcerciseSerializer(serializers.ModelSerializer):

	muscle_group_name = serializers.SerializerMethodField()

	def get_muscle_group_name(self, obj):
		return obj.muscle_group.muscle_group

	class Meta:
		model = Excercise
		fields = ('id','excercise','muscle_group','muscle_group_name','lever','mass_share')
		
class SetSerializer(serializers.ModelSerializer):
	
	#Example
	#excercise = ExcerciseSerializer()	
	#add 'excercise_obj' to fields
	
	#Override excercise id to default excercise name
	
	excercise_name = serializers.SerializerMethodField()
	muscle_group_name = serializers.SerializerMethodField()
	workout_name = serializers.SerializerMethodField()
	one_rep_max = serializers.SerializerMethodField()
	workout_date = serializers.SerializerMethodField()
	
	def get_workout_name(self, obj):
		if(obj.workout is None):
			return None
		else:
			return obj.workout.name
	
	def get_workout_date(self, obj):
		if(obj.workout is None):
			return None
		else:
			return obj.workout.start_time
	
	def get_excercise_name(self, obj):
		return obj.excercise.excercise
		
	def get_muscle_group_name(self, obj):
		return obj.excercise.muscle_group.muscle_group
		
	def get_one_rep_max(self, obj):	
		orp = one_rep_max(obj.reps, obj.weight)
		orp = round(orp, 1)		
		return orp
	
	class Meta:
		model = Set
		fields = ('id','workout_order','workout','workout_date','workout_name','reps','weight','one_rep_max','done','excercise','excercise_name','muscle_group_name','user','comments') #'excercise
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
class WorkoutSerializer(serializers.ModelSerializer):

	#Show all details from sets as sub array
	#sets = SetSerializer(many=True, read_only=True)
	
	next_id = serializers.SerializerMethodField(read_only=True)
	prev_id = serializers.SerializerMethodField(read_only=True)
	active_set = serializers.SerializerMethodField()
	#sets = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	
	
	class Meta:
		model = Workout
		fields = ('id','name','start_time','end_time','location','active_set','sets','prev_id', 'next_id')
		
	def get_next_id(self, obj):
		return get_next(obj, Workout)
		
	def get_prev_id(self, obj):
		return get_prev(obj, Workout)
	
	def get_active_set(self, obj):
		#Filter to undone sets in this workout
		workout_sets = Set.objects.filter(workout=obj).filter(done=0)
		#Get the workout with lowest workout order
		workout_sets = workout_sets.order_by('workout_order')
		
		#If there are no sets
		if(len(workout_sets) == 0):
			active_set = None
		#At least one set
		else:
			active_set = workout_sets[0].id

		return active_set
		
class RoutineSerializer(serializers.ModelSerializer):

	section_count = serializers.SerializerMethodField(read_only=True)
	
	def get_section_count(self, obj):
		section_list = Section.objects.filter(routine=obj)
		if(section_list is None):
			section_count = 0
		else:
			section_count = len(section_list)
		return section_count	


	class Meta:
		model = Routine
		fields = ('id','name','plan','type','comments','section_count')
