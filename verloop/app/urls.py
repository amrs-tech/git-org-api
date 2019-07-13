from django.urls import include,path
from . import views

app_name = 'app'

urlpatterns = [
    path('repos/<str:org>', views.repos, name='repos'),
]