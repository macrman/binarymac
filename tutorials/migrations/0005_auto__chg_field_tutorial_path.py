# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Tutorial.path'
        db.alter_column('tutorials_tutorial', 'path', self.gf('django.db.models.fields.FilePathField')(path='/home/', max_length=100, recursive=True))

    def backwards(self, orm):

        # Changing field 'Tutorial.path'
        db.alter_column('tutorials_tutorial', 'path', self.gf('django.db.models.fields.FilePathField')(path='/home/', max_length=100, recursive='True'))

    models = {
        'tutorials.tutorial': {
            'Meta': {'object_name': 'Tutorial'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.FilePathField', [], {'path': "'/home/'", 'max_length': '100', 'recursive': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        }
    }

    complete_apps = ['tutorials']