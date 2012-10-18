# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Tutorial.path'
        db.delete_column('tutorials_tutorial', 'path')

        # Adding field 'Tutorial.content'
        db.add_column('tutorials_tutorial', 'content',
                      self.gf('django.db.models.fields.files.FileField')(default='temp', max_length=100),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Tutorial.path'
        raise RuntimeError("Cannot reverse this migration. 'Tutorial.path' and its values cannot be restored.")
        # Deleting field 'Tutorial.content'
        db.delete_column('tutorials_tutorial', 'content')


    models = {
        'tutorials.tutorial': {
            'Meta': {'object_name': 'Tutorial'},
            'content': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tutorial_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['tutorials']