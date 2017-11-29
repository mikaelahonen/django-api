# Import models
from .models import *

def routineStart(routine, user):
	
	#Create new workout
	name = routine.name + ' - Created from routine'
	workout = Workout.objects.create(
		name = name,
		user = user,
	)
	
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
			
	response = {
		'routine_id': routine.id,
		'workout_id': workout.id,
		'section_count': len(section_list),
	}
	
	return response