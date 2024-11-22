from django.urls import path
from . import views
# from .views import home_view


urlpatterns = [
  
    path("ask-database/", views.ask_database, name="ask_database"),
    # path('', home_view, name='home'),
]
