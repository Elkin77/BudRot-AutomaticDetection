# Generated by Django 2.2 on 2019-06-04 06:04
"""
MachineLearning for Early-Alert System project.

Created by Brayan Rojas, Elkin Prada, on June 2019.
Co-workers: Carlos Sierra, Santiago Salazar
Copyright (c) 2019 Brayan Rojas, Elkin Prada Corporación Universitaria Minuto de Dios. All rights reserved.

This file is part of ProjectName (BudRot-AutomaticDetection).

ProjectName (BudRot-AutomaticDetection) is free software: you can redistribute it and/or modify it under the terms of the
GNU General Public License as published by the Free Software Foundation, version 3.
"""
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('network', '0005_alert'),
    ]

    operations = [
        migrations.CreateModel(
            name='Processing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thread_is_run', models.BooleanField(default=False)),
                ('context', models.TextField(null=True)),
                ('create_at', models.DateTimeField()),
                ('update_at', models.DateTimeField(null=True)),
                ('delete_at', models.DateTimeField(null=True)),
                ('status', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='processing_created_by', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='processing_delete_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='processing_update_by', to=settings.AUTH_USER_MODEL)),
                ('upload', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thread_upload', to='network.Upload')),
            ],
        ),
    ]
