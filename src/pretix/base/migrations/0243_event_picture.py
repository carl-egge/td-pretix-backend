# Generated by Django 3.2.19 on 2023-09-22 10:03

from django.db import migrations, models
import pretix.base.models.event


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0242_event_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='picture',
            field=models.ImageField(max_length=255, null=True, upload_to=pretix.base.models.event.eventpicture_upload_to),
        ),
    ]
