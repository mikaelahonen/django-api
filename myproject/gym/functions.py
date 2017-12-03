# Import models
from gym.models import *
#Pandas and NumPy
import numpy as np
import pandas as pd


#Creates sets from routine and returns the list of sets
#More details about routine types in models.py file
def _create_routine_sets(workout, routine, user):

	#Get excercise list
	excercises = Excercise.objects.values('id','muscle_group_id')
	df_excercises = pd.DataFrame(list(excercises))
	df_excercises.columns = ['excercise_id', 'muscle_group_id']	
	#Create column for randomized order
	df_excercises['random_order'] = df_excercises.sample(frac=1).index	
	#Set partition index for muscle group
	df_excercises['mg_order'] = df_excercises.groupby("muscle_group_id")['random_order'].rank(method="dense").astype('int64')
	
	
	#Get sections as values for the routine
	sections = Section.objects.filter(routine=routine.id).order_by('index').values()	
	#Initialize section data frame
	df_sections = pd.DataFrame(list(sections))
	df_sections['section_rank'] = df_sections.index
	df_sections['mg_order'] = df_sections.groupby("muscle_group_id")['section_rank'].rank(method="dense").astype('int64')
	
	#Combine excercises by the random key
	df_sections = pd.merge(df_sections, df_excercises, left_on=['muscle_group_id', 'mg_order'], right_on=['muscle_group_id', 'mg_order'], how='left')	
	#Create excercise column
	df_sections['excercise_id'] = np.where(df_sections['random_excercise'], df_sections['excercise_id_y'], df_sections['excercise_id_x'])
	df_sections
	
	#if(routine.type = 'EF'):	
	#Copy rows by the number of times defined in section's sets column
	df_sets = df_sections.loc[np.repeat(df_sections.index.values, df_sections.sets)]
	#Reset index
	df_sets = df_sets.reset_index(drop=True)
	#Create new index column for sets 
	df_sets['workout_order'] = df_sets.index + 1
	
	#if(routine.type = 'SF'):
	
	#if(routine.type = 'AT'):
		
		
	#Create empty list to save sets
	sets = []
	#Iterate over sets data frame
	for index, row in df_sets.iterrows():
		set = Set.objects.create(
			workout = workout,
			excercise_id = row['excercise_id'],			
			workout_order = row['workout_order'],
			user = user,
			#reps = section.target,
		)
		sets.append(set)
	
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
