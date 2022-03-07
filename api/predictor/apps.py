from django.apps import AppConfig
from django.conf import settings
import os
import pickle

class PredictorConfig(AppConfig):
   name = 'predictor'

   # create path to models
   path = os.path.join(settings.MODELS, 'models.p')
 
   # load models into separate variables
   # these will be accessible via this class
   with open(path, 'rb') as pickled:
      models = pickle.load(pickled)

    # create variables for each model
   alcohol = models['Alcohol']
   amphet = models['Amphet']
   amyl = models['Amyl']
   benzos = models['Benzos']
   caff = models['Caff']
   cannabis = models['Cannabis']
   coke = models['Coke']
   crack = models['Crack']
   ecstasy = models['Esctasy']
   heroin = models['Heroin']
   ketamine = models['Ketamine']
   legalh = models['Legalh']
   lsd = models['LSD']
   meth = models['Meth']
   mushrooms = models['Mushrooms']
   nicotine = models['Nicotine']
   vsa = models['VSA']