# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0032_contact_api_indexes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactgroup',
            name='name',
            field=models.CharField(help_text='The name of this contact group', max_length=64, verbose_name='Name'),
            preserve_default=True,
        ),
    ]
