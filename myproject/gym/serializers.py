from gym.models import *
from rest_framework import serializers
import json
from gym.functions import *

#Relations
#http://www.django-rest-framework.org/api-guide/relations/#serializer-relations
class MyModelSerializer(serializers.ModelSerializer):
	"""
	A ModelSerializer that takes an additional `fields` argument that
	controls which fields should be displayed.
	"""

	def __init__(self, *args, **kwargs):
		# Don't pass the 'fields' arg up to the superclass
		fields = kwargs.pop('fields', None)

		# Instantiate the superclass normally
		super(MyModelSerializer, self).__init__(*args, **kwargs)

		if fields is not None:
			# Drop any fields that are not specified in the `fields` argument.
			allowed = set(fields)
			existing = set(self.fields.keys())
			for field_name in existing - allowed:
				self.fields.pop(field_name)

class ExcerciseSerializer(MyModelSerializer):

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
	workout_date = serializers.SerializerMethodField(read_only=True)
	user = serializers.PrimaryKeyRelatedField(
		read_only=True,
		default=serializers.CurrentUserDefault(),
	)

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

class MuscleGroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = MuscleGroup
		fields = ('id','muscle_group')


#Return a single workout together with all related sets
class WorkoutSerializer(MyModelSerializer):

	#Show all details from sets as sub array
	#sets = SetSerializer(many=True, read_only=True)

	next_id = serializers.SerializerMethodField(read_only=True)
	prev_id = serializers.SerializerMethodField(read_only=True)
	active_set = serializers.SerializerMethodField()
	#Keep read_only=True to not require it on forms
	sets_done = serializers.SerializerMethodField(read_only=True)
	sets_total = serializers.SerializerMethodField(read_only=True)
	user = serializers.PrimaryKeyRelatedField(
		read_only=True,
		#http://www.django-rest-framework.org/api-guide/validators/#currentuserdefault
		default=serializers.CurrentUserDefault()
	)


	class Meta:
		model = Workout
		fields = (
			'id',
			'name',
			'start_time',
			'end_time',
			'location',
			'comments',
			'user',
			'active_set',
			'sets_done',
			'sets_total',
			'prev_id',
			'next_id',
		)

	def get_next_id(self, obj):
		return get_next(obj, Workout)

	def get_prev_id(self, obj):
		return get_prev(obj, Workout)

	def get_sets_done(self, obj):
		sets_done = Set.objects.filter(workout=obj, done=True)
		return len(sets_done)

	def get_sets_total(self, obj):
		sets_total = Set.objects.filter(workout=obj)
		return len(sets_total)

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
	type_name = serializers.SerializerMethodField()

	def get_section_count(self, obj):
		section_list = Section.objects.filter(routine=obj)
		if(section_list is None):
			section_count = 0
		else:
			section_count = len(section_list)
		return section_count

	def get_type_name(self, obj):
		return obj.get_type_display()


	class Meta:
		model = Routine
		fields = ('id','name','plan','type','type_name','comments','section_count')

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'
