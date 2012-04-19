# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Log'
        db.create_table('menu_log', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('clip', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['menu.Clip'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('menu', ['Log'])

        # Adding field 'Clip.count'
        db.add_column('menu_clip', 'count', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=100000), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'Log'
        db.delete_table('menu_log')

        # Deleting field 'Clip.count'
        db.delete_column('menu_clip', 'count')


    models = {
        'menu.clip': {
            'Meta': {'object_name': 'Clip'},
            'classificacao': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'count': ('django.db.models.fields.IntegerField', [], {'max_length': '100000'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['menu.Country']", 'null': 'True', 'blank': 'True'}),
            'cover': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
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
            'Meta': {'ordering': "('name',)", 'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'menu.director': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Director'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'menu.genre': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Genre'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'menu.log': {
            'Meta': {'object_name': 'Log'},
            'clip': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['menu.Clip']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'menu.star': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Star'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'menu.year': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Year'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        }
    }

    complete_apps = ['menu']
