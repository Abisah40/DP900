from django.urls import path
from .import views

urlpatterns = [
    path('',views.Home, name='home'),
    path('explore/',views.FileStorage, name='explore'),
    path('explore/databases',views.ExploreDb, name='databases'),
    path('explore/databases/transactionaldb',views.Trans, name='transactionaldb'),
    path('explore/databases/transactionaldb/analytical',views.Analytic, name='analytical'),
    path('explore/databases/transactionaldb/analytical/databricks',views.Databricks, name='databricks'),
]