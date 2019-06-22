# Generated by Django 2.2.1 on 2019-06-22 06:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('coreapi', '0005_inputembed_fileurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputembed',
            name='fileurl',
            field=models.CharField(default='/Users/amit/GitHub/Rekognition/media/face/b6d49cd4-adcf-4442-aaa3-b7ff63a06122.jpg', editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='inputembed',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b6d49cd4-adcf-4442-aaa3-b7ff63a06122'), editable=False, primary_key=True, serialize=False),
        ),
    ]