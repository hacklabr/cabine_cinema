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
