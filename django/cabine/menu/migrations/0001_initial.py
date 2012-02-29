# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Clip'
        db.create_table('menu_clip', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('position', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
            ('file_path', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('year', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['menu.Year'], null=True, blank=True)),
        ))
        db.send_create_signal('menu', ['Clip'])

        # Adding M2M table for field genre on 'Clip'
        db.create_table('menu_clip_genre', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('clip', models.ForeignKey(orm['menu.clip'], null=False)),
            ('genre', models.ForeignKey(orm['menu.genre'], null=False))
        ))
        db.create_unique('menu_clip_genre', ['clip_id', 'genre_id'])

        # Adding M2M table for field director on 'Clip'
        db.create_table('menu_clip_director', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('clip', models.ForeignKey(orm['menu.clip'], null=False)),
            ('director', models.ForeignKey(orm['menu.director'], null=False))
        ))
        db.create_unique('menu_clip_director', ['clip_id', 'director_id'])

        # Adding M2M table for field writer on 'Clip'
        db.create_table('menu_clip_writer', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('clip', models.ForeignKey(orm['menu.clip'], null=False)),
            ('writer', models.ForeignKey(orm['menu.writer'], null=False))
        ))
        db.create_unique('menu_clip_writer', ['clip_id', 'writer_id'])

        # Adding M2M table for field star on 'Clip'
        db.create_table('menu_clip_star', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('clip', models.ForeignKey(orm['menu.clip'], null=False)),
            ('star', models.ForeignKey(orm['menu.star'], null=False))
        ))
        db.create_unique('menu_clip_star', ['clip_id', 'star_id'])

        # Adding model 'Genre'
        db.create_table('menu_genre', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal('menu', ['Genre'])

        # Adding model 'Director'
        db.create_table('menu_director', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal('menu', ['Director'])

        # Adding model 'Writer'
        db.create_table('menu_writer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal('menu', ['Writer'])

        # Adding model 'Star'
        db.create_table('menu_star', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal('menu', ['Star'])

        # Adding model 'Year'
        db.create_table('menu_year', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal('menu', ['Year'])


    def backwards(self, orm):
        
        # Deleting model 'Clip'
        db.delete_table('menu_clip')

        # Removing M2M table for field genre on 'Clip'
        db.delete_table('menu_clip_genre')

        # Removing M2M table for field director on 'Clip'
        db.delete_table('menu_clip_director')

        # Removing M2M table for field writer on 'Clip'
        db.delete_table('menu_clip_writer')

        # Removing M2M table for field star on 'Clip'
        db.delete_table('menu_clip_star')

        # Deleting model 'Genre'
        db.delete_table('menu_genre')

        # Deleting model 'Director'
        db.delete_table('menu_director')

        # Deleting model 'Writer'
        db.delete_table('menu_writer')

        # Deleting model 'Star'
        db.delete_table('menu_star')

        # Deleting model 'Year'
        db.delete_table('menu_year')


    models = {
        'menu.clip': {
            'Meta': {'object_name': 'Clip'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'director': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['menu.Director']", 'null': 'True', 'blank': 'True'}),
            'file_path': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'genre': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['menu.Genre']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'position': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
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
