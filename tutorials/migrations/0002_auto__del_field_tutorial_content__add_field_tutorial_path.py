# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Tutorial.content'
        db.delete_column('tutorials_tutorial', 'content')

        # Adding field 'Tutorial.path'
        db.add_column('tutorials_tutorial', 'path',
                      self.gf('django.db.models.fields.FilePathField')(default='temp', path='/home/dev/binarymac/binarymac/static', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Tutorial.content'
        db.add_column('tutorials_tutorial', 'content',
                      self.gf('django.db.models.fields.files.FileField')(default='temp', max_length=100),
                      keep_default=False)

        # Deleting field 'Tutorial.path'
        db.delete_column('tutorials_tutorial', 'path')


    models = {
        'tutorials.tutorial': {
            'Meta': {'object_name': 'Tutorial'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.FilePathField', [], {'path': "'/home/dev/binarymac/binarymac/static'", 'max_length': '100'}),
            'tutorial_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['tutorials']