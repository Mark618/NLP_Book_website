from django.apps import AppConfig
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
import os
import pickle
from gensim.models.doc2vec import Doc2Vec



class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
    model_path = os.path.join(settings.MODELS, 'feature.pkl')
    sim_model_path = os.path.join(settings.MODELS, 'sim.model')
    tf1 = pickle.load(open(model_path, 'rb'))
    sim_model = Doc2Vec.load(sim_model_path)
