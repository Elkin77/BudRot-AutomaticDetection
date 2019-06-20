# Generated by Django 2.2 on 2019-06-02 20:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import network.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('file_name', models.CharField(max_length=100)),
                ('message_file', models.TextField()),
                ('output_file', models.FileField(upload_to=network.models.create_path)),
                ('create_at', models.DateTimeField()),
                ('update_at', models.DateTimeField(null=True)),
                ('delete_at', models.DateTimeField(null=True)),
                ('status', models.BooleanField(default=True)),
                ('status_file', models.IntegerField(default=0)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file_created_by', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file_delete_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file_update_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
