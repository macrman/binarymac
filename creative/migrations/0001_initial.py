# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Idea'
        db.create_table('creative_idea', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('stage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['creative.Stage'])),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('featured_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('creative', ['Idea'])

        # Adding M2M table for field project on 'Idea'
        db.create_table('creative_idea_project', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('idea', models.ForeignKey(orm['creative.idea'], null=False)),
            ('project', models.ForeignKey(orm['creative.project'], null=False))
        ))
        db.create_unique('creative_idea_project', ['idea_id', 'project_id'])

        # Adding model 'Project'
        db.create_table('creative_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('creative', ['Project'])

        # Adding model 'Stage'
        db.create_table('creative_stage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('creative', ['Stage'])


    def backwards(self, orm):
        # Deleting model 'Idea'
        db.delete_table('creative_idea')

        # Removing M2M table for field project on 'Idea'
        db.delete_table('creative_idea_project')

        # Deleting model 'Project'
        db.delete_table('creative_project')

        # Deleting model 'Stage'
        db.delete_table('creative_stage')


    models = {
        'creative.idea': {
            'Meta': {'object_name': 'Idea'},
            'featured_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['creative.Project']", 'symmetrical': 'False', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'stage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['creative.Stage']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'creative.project': {
            'Meta': {'object_name': 'Project'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'creative.stage': {
            'Meta': {'object_name': 'Stage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['creative']