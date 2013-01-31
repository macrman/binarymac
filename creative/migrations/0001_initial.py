# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table('creative_post', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('stage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['creative.Stage'])),
        ))
        db.send_create_signal('creative', ['Post'])

        # Adding M2M table for field project on 'Post'
        db.create_table('creative_post_project', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm['creative.post'], null=False)),
            ('project', models.ForeignKey(orm['creative.project'], null=False))
        ))
        db.create_unique('creative_post_project', ['post_id', 'project_id'])

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
        # Deleting model 'Post'
        db.delete_table('creative_post')

        # Removing M2M table for field project on 'Post'
        db.delete_table('creative_post_project')

        # Deleting model 'Project'
        db.delete_table('creative_project')

        # Deleting model 'Stage'
        db.delete_table('creative_stage')


    models = {
        'creative.post': {
            'Meta': {'object_name': 'Post'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['creative.Project']", 'symmetrical': 'False'}),
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