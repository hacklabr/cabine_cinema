# Copyright (C) 2012 Hacklab Ltda

# This software is free software; you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public
# License as published by the Free Software Foundation;  either
# version 3 of the License, or (at your option) any later version.

# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.

# You should have received a copy of the GNU Lesser General Public
# License along with this software; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA


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
    country = models.ManyToManyField('Country', null=True, blank=True, verbose_name='País')
    year = models.ForeignKey('Year',null=True, blank=True, verbose_name='Ano de lançamento')
    star = models.ManyToManyField('Star', null=True, blank=True, verbose_name='Estrelas')
    cover = models.BooleanField(verbose_name="Tem capa em arquivo")
    #cover_path = models.BooleanField(verbose_name="Tem capa em arquivo")
    #medium_cover_path = models.BooleanField(verbose_name="Tem capa em arquivo")
    #small_cover_path = models.BooleanField(verbose_name="Tem capa em arquivo")
    count = models.IntegerField(max_length=100000, verbose_name="Total de reproduções")

    def verifica_capa(self):
        
        clip_id = str(self.id)
        if (self.id < 10):
            clip_id = "0"+clip_id
        
        cover_path = "/static/thumbs/{0}_grande.jpg".format(clip_id)
        medium_cover_path = "/static/thumbs/{0}_media.jpg".format(clip_id)
        small_cover_path = "/static/thumbs/{0}_pequena.jpg".format(clip_id)
        
        if os.path.exists(settings.path + "/menu/" + cover_path):
            self.cover_path = cover_path            
        else:
            self.cover_path = "{0}_grande.jpg".format("/static/thumbs/default")

        if os.path.exists(settings.path + "/menu/" + medium_cover_path):
            self.medium_cover_path = medium_cover_path            
        else:
            self.medium_cover_path = "{0}_media.jpg".format("/static/thumbs/default")
            
        if os.path.exists(settings.path + "/menu/" + small_cover_path):
            self.small_cover_path = small_cover_path            
        else:
            self.small_cover_path = "{0}_pequena.jpg".format("/static/thumbs/default")
        
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

