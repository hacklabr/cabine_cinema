# _*_ coding: UTF-8 _*_
from django.db import models

class Clip(models.Model):
    name = models.CharField(verbose_name='Nome do filme', max_length = 300)
    description = models.TextField( null=True, blank=True, verbose_name='Descrição')
    position = models.IntegerField(max_length = 10, verbose_name='Posição', blank=True, null=True )
    file_path = models.CharField(verbose_name='Caminho do arquivo', max_length = 300)
    genre = models.ManyToManyField('Genre', null=True, blank=True, verbose_name='Gênero')
    director = models.ManyToManyField('Director', null=True, blank=True, verbose_name='Diretor')
    writer = models.ManyToManyField('Writer', null=True, blank=True, verbose_name='Escritor')
    star = models.ManyToManyField('Star', null=True, blank=True, verbose_name='Estrela')
    year = models.ForeignKey('Year',null=True, blank=True, verbose_name='Ano de lançamento')

    def __unicode__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(verbose_name='Gênero', max_length = 300)
    
    def __unicode__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(verbose_name='Diretor', max_length = 300)
    
    def __unicode__(self):
        return self.name

class Writer(models.Model):
    name = models.CharField(verbose_name='Escritor', max_length = 300)
    
    def __unicode__(self):
        return self.name

class Star(models.Model):
    name = models.CharField(verbose_name='Estrela', max_length = 300)
    
    def __unicode__(self):
        return self.name

class Year(models.Model):
    name = models.CharField(verbose_name='Ano', max_length = 300)
    
    def __unicode__(self):
        return self.name

