from django.db import models

class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200, blank=True)
    title_jp = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    next_evolution = models.OneToOneField(
        "Pokemon", related_name='previous_evolution', 
        on_delete=models.SET_NULL, null=True, blank=True
        )
    image = models.ImageField(upload_to='pokemons', blank=True)

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    appeared_at = models.DateTimeField(default=None)
    dissapeared_at = models.DateTimeField(default=None)
    level = models.IntegerField(null=True, blank=True)
    health = models.IntegerField(null=True, blank=True)
    strength = models.IntegerField(null=True, blank=True)
    defence = models.IntegerField(null=True, blank=True)
    stamina = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "Pokemon {}_{} level {}".format(self.pokemon, self.id, self.level)
