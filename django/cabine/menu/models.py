# _*_ coding: UTF-8 _*_
from django.db import models
from django.forms import ModelForm

class Clip(models.Model):
    name = models.CharField(verbose_name='Título do filme', max_length = 300)
    orig_name = models.CharField(verbose_name='Título original do filme', max_length = 300)
    sinopse = models.TextField(null=True, blank=True, verbose_name='Sinopse')
    position = models.IntegerField(max_length = 10, verbose_name='Posição', blank=True, null=True )
    file_path = models.CharField(verbose_name='Caminho do arquivo', max_length = 300)
    genre = models.ManyToManyField('Genre', null=True, blank=True, verbose_name='Gênero')
    director = models.ManyToManyField('Director', null=True, blank=True, verbose_name='Diretor')
    country = models.ForeignKey('Country', null=True, blank=True, verbose_name='País')
    year = models.ForeignKey('Year',null=True, blank=True, verbose_name='Ano de lançamento')
    star = models.ManyToManyField('Star', null=True, blank=True, verbose_name='Estrelas')
    cover = models.FileField(upload_to='cover')
    
    def __unicode__(self):
        return self.name

class Star(models.Model):
    name = models.CharField(verbose_name='Atores', max_length = 300)
    
    class Meta:
        ordering = ('name',)
        
    def __unicode__(self):
        return self.name
    
class Genre(models.Model):
    name = models.CharField(verbose_name='Gênero', max_length = 300)
    
    class Meta:
        ordering = ('name',)
            

    def __unicode__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(verbose_name='Diretor', max_length = 300)
    
    class Meta:
        ordering = ('name',)
        

    def __unicode__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(verbose_name='País', max_length = 300)
    
    class Meta:
        ordering = ('name',)
        

    def __unicode__(self):
        return self.name

class Year(models.Model):
    name = models.CharField(verbose_name='Ano', max_length = 300)
    
    class Meta:
        ordering = ('name',)
        
    
    def __unicode__(self):
        return self.name

