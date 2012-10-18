# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tutorial'
        db.create_table('tutorials_tutorial', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tutorial_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('content', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('tutorials', ['Tutorial'])


    def backwards(self, orm):
        # Deleting model 'Tutorial'
        db.delete_table('tutorials_tutorial')


    models = {
        'tutorials.tutorial': {
            'Meta': {'object_name': 'Tutorial'},
            'content': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tutorial_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['tutorials']