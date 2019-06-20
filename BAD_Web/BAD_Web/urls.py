"""
url file of the alert system project.

Created by BrayanRojas0630, Elkin77, on June 2019.
Copyright (c) 2019 BrayanRojas0630, Elkin77 Corporación Universitaria Minuto de Dios. All rights reserved.

This file is part of ProjectName (BudRot-AutomaticDetection).

ProjectName (BudRot-AutomaticDetection) is free software: you can redistribute it and/or modify it under the terms of the
GNU General Public License as published by the Free Software Foundation, version 3.
"""

  
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('user.urls')),
    path('admin/', admin.site.urls),
    path('network/', include('network.urls')),
    path('user/', include('user.urls')),
]