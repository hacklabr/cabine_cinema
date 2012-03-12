# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Star'
        db.create_table('menu_star', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal('menu', ['Star'])

        # Adding M2M table for field star on 'Clip'
        db.create_table('menu_clip_star', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('clip', models.ForeignKey(orm['menu.clip'], null=False)),
            ('star', models.ForeignKey(orm['menu.star'], null=False))
        ))
        db.create_unique('menu_clip_star', ['clip_id', 'star_id'])


    def backwards(self, orm):
        
        # Deleting model 'Star'
        db.delete_table('menu_star')

        # Removing M2M table for field star on 'Clip'
        db.delete_table('menu_clip_star')


    models = {
        'menu.clip': {
            'Meta': {'object_name': 'Clip'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['menu.Country']", 'null': 'True', 'blank': 'True'}),
            'director': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['menu.Director']", 'null': 'True', 'blank': 'True'}),
            'file_path': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'genre': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['menu.Genre']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'orig_name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'position': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'sinopse': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'star': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['menu.Star']", 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['menu.Year']", 'null': 'True', 'blank': 'True'})
        },
        'menu.country': {
            'Meta': {'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'menu.director': {
            'Meta': {'object_name': 'Director'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'menu.genre': {
            'Meta': {'object_name': 'Genre'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'menu.star': {
            'Meta': {'object_name': 'Star'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'menu.year': {
            'Meta': {'object_name': 'Year'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        }
    }

    complete_apps = ['menu']
