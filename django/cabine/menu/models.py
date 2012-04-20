# _*_ coding: UTF-8 _*_
import os
import settings
from django.db import models
from django.forms import ModelForm

class Clip(models.Model):
    name = models.CharField(verbose_name='Título do filme', max_length = 300)
    orig_name = models.CharField(verbose_name='Título original do filme', max_length = 300)
    sinopse = models.TextField(null=True, blank=True, verbose_name='Sinopse')
    classificacao = models.TextField(null=True, blank=True, verbose_name='Classificação Etária')
    position = models.IntegerField(max_length = 10, verbose_name='Posição', blank=True, null=True )
    file_path = models.CharField(verbose_name='Caminho do arquivo', max_length = 300)
    genre = models.ManyToManyField('Genre', null=True, blank=True, verbose_name='Gênero')
    director = models.ManyToManyField('Director', null=True, blank=True, verbose_name='Diretor')
    country = models.ForeignKey('Country', null=True, blank=True, verbose_name='País')
    year = models.ForeignKey('Year',null=True, blank=True, verbose_name='Ano de lançamento')
    star = models.ManyToManyField('Star', null=True, blank=True, verbose_name='Estrelas')
    cover = models.BooleanField(verbose_name="Tem capa em arquivo")
    count = models.IntegerField(max_length=100000, verbose_name="Total de reproduções")

    def verifica_capa(self):
        if os.path.exists("%s/%s/%s.jpg" % ( settings.path,  "/menu/static/thumbs/", self.id)):
            self.cover = True
	    self.save()
	else:
	    self.cover = False
	    self.save()  	


    def __unicode__(self):
        return self.name
    
    def update_reproducoes(self):
        count = 0
        for entrada in Log.objects.all():
            if entrada.clip == self:
                count += 1
        self.count = count
        self.save()
        

class Log(models.Model):
    clip = models.ForeignKey('Clip', null=False, blank=False, verbose_name="Cena")
    date = models.DateTimeField(auto_now_add=True, verbose_name = "Data da reprodução")

    def __unicode__(self):
        return self.clip.name

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

