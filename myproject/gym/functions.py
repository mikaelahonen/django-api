# Import models
from gym.models import *

#Takes and routine object as an argument.
#Returns the list of set indexes.
def _create_routine_sets(workout, routine, user):
	
	#Create sets by sections
	section_list = Section.objects.filter(routine=routine.id)
	for section in section_list:
		#Get the excercise of this section
		if(section.random):
			excercises = Excercise.objects.filter(muscle_group=section.excercise.muscle_group)
			excercise = random.choice(excercises)
		else:
			excercise = section.excercise
			
		# Create the specified number of sections	
		for i in range(0, section.sets):
			#Create Set object where foreign key is the related Workout
			Set.objects.create(
				workout = workout,
				excercise = excercise,
				user = user,
				#reps = section.target
			)
	
	sets = [1,2,3]
	return sets
	
def _create_routine_workout(routine, user):		
	#Create new workout
	name = routine.name + ' - Created from routine'
	workout = Workout.objects.create(
		name = name,
		user = user,
	)
	
	return workout

def routine_start(routine, user):
	
	workout= _create_routine_workout(routine, user)
	sets = _create_routine_sets(workout, routine, user)
		
	#Pass some information that the data were created
	response = {
		'routine_id': routine.id,
		'workout_id': workout.id,
		'section_count': len(sets),
	}
	
	return response
	
#Retrieves the next id of an object for any model
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
		
#Retrieves the previous id of an object for any model
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
	
def one_rep_max(reps, weight):
	#Make sure repetitions is not None or 0
	if(reps is not None and reps!=0):
		if(weight is not None and weight!=0):
			one_rep_max = 36/(37-reps)*weight
		else:
			one_rep_max = reps
	else:
			one_rep_max = 0
			
	return one_rep_max
