# Generated by Django 3.2.19 on 2023-07-03 08:11

from django.db import migrations
import i18nfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0241_itemmetaproperties_required_values'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='desc',
            field=i18nfield.fields.I18nTextField(null=True),
        ),
    ]
