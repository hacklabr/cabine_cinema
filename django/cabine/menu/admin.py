from django.contrib import admin
from menu.models import Clip, Director, Country, Year, Genre, Star, Log

class ClipAdmin(admin.ModelAdmin):
    list_display = ('name','orig_name', 'sinopse', 'year')
    ordering = ('name',)

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)

class YearAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)

class StarAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)

class LogAdmin(admin.ModelAdmin):
    list_display = ('clip','date')
    ordering = ('date',)

admin.site.register(Clip, ClipAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Year, YearAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Star, StarAdmin)
admin.site.register(Log, LogAdmin)
