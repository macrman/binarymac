# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Page.slug'
        db.add_column('simplepages_page', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='tempslug', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Page.slug'
        db.delete_column('simplepages_page', 'slug')


    models = {
        'simplepages.page': {
            'Meta': {'object_name': 'Page'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['simplepages']