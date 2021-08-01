from django.urls import path
from . import views

urlpatterns = [
    path("hello-world/", views.index), 
    path('', views.PokemonList.as_view()),
    path('<int:pk>/', views.PokemonOneList.as_view()),
    # v2
    path("v2/", views.PokemonGetAll),
    path("v2/<int:pk>/", views.PokemonGetOne),
    path("v2/pokemon", views.PokemonGetWithFilter),

]
