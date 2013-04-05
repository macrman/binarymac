# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Stage.info'
        db.add_column(u'creative_stage', 'info',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Stage.info'
        db.delete_column(u'creative_stage', 'info')


    models = {
        u'creative.idea': {
            'Meta': {'object_name': 'Idea'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'featured_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['creative.Project']", 'symmetrical': 'False', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'stage': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['creative.Stage']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'creative.project': {
            'Meta': {'object_name': 'Project'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'creative.stage': {
            'Meta': {'object_name': 'Stage'},
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['creative']