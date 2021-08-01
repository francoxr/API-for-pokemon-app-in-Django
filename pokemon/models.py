from django.db import models
from django.db import models

# Create your models here.


class Types(models.Model):
    name = models.CharField("Nombre", max_length=255)
    created = models.DateTimeField('creado',auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Pokemon(models.Model):
    name = models.CharField("Nombre", max_length=255)
    height = models.PositiveSmallIntegerField("Altura")
    weight = models.PositiveSmallIntegerField("Peso")
    image = models.URLField("Url Image")
    hp = models.PositiveSmallIntegerField("Vida")
    attack = models.PositiveSmallIntegerField("Ataque")
    defense = models.PositiveSmallIntegerField("Defensa")
    special_attack = models.PositiveSmallIntegerField("Ataque Especial")
    special_defense = models.PositiveSmallIntegerField("Defensa Especial")
    speed = models.PositiveSmallIntegerField("Velocidad")
    price = models.DecimalField("Precio", decimal_places=2, max_digits=5)
    type_ids = models.ManyToManyField(Types)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
