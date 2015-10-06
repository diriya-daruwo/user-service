# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'User.role'
        db.add_column(u'user_api_user', 'role',
                      self.gf('django.db.models.fields.CharField')(default='PA', max_length=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'User.role'
        db.delete_column(u'user_api_user', 'role')


    models = {
        u'user_api.user': {
            'Meta': {'object_name': 'User'},
            'auth_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'default': "'PA'", 'max_length': '2'})
        }
    }

    complete_apps = ['user_api']