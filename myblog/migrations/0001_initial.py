# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table('myblog_post', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('myblog', ['Post'])

        # Adding model 'Tag'
        db.create_table('myblog_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('myblog', ['Tag'])

        # Adding M2M table for field post on 'Tag'
        db.create_table('myblog_tag_post', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tag', models.ForeignKey(orm['myblog.tag'], null=False)),
            ('post', models.ForeignKey(orm['myblog.post'], null=False))
        ))
        db.create_unique('myblog_tag_post', ['tag_id', 'post_id'])


    def backwards(self, orm):
        # Deleting model 'Post'
        db.delete_table('myblog_post')

        # Deleting model 'Tag'
        db.delete_table('myblog_tag')

        # Removing M2M table for field post on 'Tag'
        db.delete_table('myblog_tag_post')


    models = {
        'myblog.post': {
            'Meta': {'object_name': 'Post'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'myblog.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'post': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['myblog.Post']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['myblog']