# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Clip.position'
        db.alter_column('menu_clip', 'position', self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True))


    def backwards(self, orm):
        
        # Changing field 'Clip.position'
        db.alter_column('menu_clip', 'position', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=10))


    models = {
        'menu.clip': {
            'Meta': {'object_name': 'Clip'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'director': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['menu.Director']", 'null': 'True', 'blank': 'True'}),
            'file_path': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'genre': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['menu.Genre']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'position': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'star': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['menu.Star']", 'null': 'True', 'blank': 'True'}),
            'writer': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['menu.Writer']", 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['menu.Year']", 'null': 'True', 'blank': 'True'})
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
        'menu.writer': {
            'Meta': {'object_name': 'Writer'},
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
