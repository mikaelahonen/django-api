from django.db import models
from django.db.models import F, Count, Value, ExpressionWrapper
#from gym.models import *

#Pandas and NumPy
import numpy as np
import pandas as pd

class SetManager(models.Manager):

    #Default queryset
    def get_queryset(self):
        #Initial queryset
        queryset = super(SetManager, self).get_queryset().select_related('workout')
        queryset = queryset.annotate(
            orp=ExpressionWrapper(
                (36/(37-F('reps')))*F('weight'),
                #F('reps')+F('weight'),
                output_field=models.FloatField()
            )
        )
        return queryset
