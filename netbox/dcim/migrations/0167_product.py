# Generated by Django 4.0.6 on 2022-08-02 09:39

import django.core.serializers.json
from django.db import migrations, models
import taggit.managers
import utilities.fields
import utilities.ordering


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0073_journalentry_tags_custom_fields'),
        ('dcim', '0166_remove_device_products_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('local_context_data', models.JSONField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('_name', utilities.fields.NaturalOrderingField('name', blank=True, max_length=100, naturalize_function=utilities.ordering.naturalize, null=True)),
                ('comments', models.CharField(default='', max_length=255)),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'ordering': ('_name', 'pk'),
                'unique_together': {('name',)},
            },
        ),
    ]
