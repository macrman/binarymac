# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Tutorial.content'
        db.delete_column('tutorials_tutorial', 'content')

        # Deleting field 'Tutorial.tutorial_name'
        db.delete_column('tutorials_tutorial', 'tutorial_name')

        # Adding field 'Tutorial.slug'
        db.add_column('tutorials_tutorial', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='temp', max_length=50),
                      keep_default=False)

        # Adding field 'Tutorial.title'
        db.add_column('tutorials_tutorial', 'title',
                      self.gf('django.db.models.fields.CharField')(default='temp', max_length=140),
                      keep_default=False)

        # Adding field 'Tutorial.path'
        db.add_column('tutorials_tutorial', 'path',
                      self.gf('django.db.models.fields.FilePathField')(default='temp', path='/home/', max_length=100, recursive='True'),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Tutorial.content'
        raise RuntimeError("Cannot reverse this migration. 'Tutorial.content' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Tutorial.tutorial_name'
        raise RuntimeError("Cannot reverse this migration. 'Tutorial.tutorial_name' and its values cannot be restored.")
        # Deleting field 'Tutorial.slug'
        db.delete_column('tutorials_tutorial', 'slug')

        # Deleting field 'Tutorial.title'
        db.delete_column('tutorials_tutorial', 'title')

        # Deleting field 'Tutorial.path'
        db.delete_column('tutorials_tutorial', 'path')


    models = {
        'tutorials.tutorial': {
            'Meta': {'object_name': 'Tutorial'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.FilePathField', [], {'path': "'/home/'", 'max_length': '100', 'recursive': "'True'"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        }
    }

    complete_apps = ['tutorials']