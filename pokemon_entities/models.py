from django.db import models

class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200, verbose_name='Имя на русском')
    title_en = models.CharField(max_length=200, verbose_name='Имя на английском', blank=True)
    title_jp = models.CharField(max_length=200, verbose_name='Имя на японском', blank=True)
    description = models.TextField(blank=True, verbose_name='Описание')
    next_evolution = models.OneToOneField(
        "Pokemon", related_name='previous_evolution', 
        verbose_name='Описание',
        on_delete=models.SET_NULL, null=True, blank=True
        )
    image = models.ImageField(upload_to='pokemons', blank=True)

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, verbose_name='Покемон', on_delete=models.CASCADE)
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(verbose_name='Время появления', null=True)
    dissapeared_at = models.DateTimeField(verbose_name='Время исчезновения', null=True)
    level = models.IntegerField(verbose_name='Уровень', null=True, blank=True)
    health = models.IntegerField(verbose_name='Здоровье', null=True, blank=True)
    strength = models.IntegerField(verbose_name='Сила', null=True, blank=True)
    defence = models.IntegerField(verbose_name='Защита', null=True, blank=True)
    stamina = models.IntegerField(verbose_name='Стамина', null=True, blank=True)

    def __str__(self):
        return "Pokemon {}_{} level {}".format(self.pokemon, self.id, self.level)
