# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table('posts_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('posts', ['Tag'])

        # Adding M2M table for field post on 'Tag'
        db.create_table('posts_tag_post', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tag', models.ForeignKey(orm['posts.tag'], null=False)),
            ('post', models.ForeignKey(orm['posts.post'], null=False))
        ))
        db.create_unique('posts_tag_post', ['tag_id', 'post_id'])

        # Removing M2M table for field tag on 'Post'
        db.delete_table('posts_post_tag')


    def backwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table('posts_tag')

        # Removing M2M table for field post on 'Tag'
        db.delete_table('posts_tag_post')

        # Adding M2M table for field tag on 'Post'
        db.create_table('posts_post_tag', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm['posts.post'], null=False)),
            ('tag', models.ForeignKey(orm['tags.tag'], null=False))
        ))
        db.create_unique('posts_post_tag', ['post_id', 'tag_id'])


    models = {
        'posts.post': {
            'Meta': {'object_name': 'Post'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'posts.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'post': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['posts.Post']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['posts']