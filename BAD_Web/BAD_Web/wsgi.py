"""
wsgi file of the alert system project.

Created by BrayanRojas0630, Elkin77, on June 2019.
Copyright (c) 2019 BrayanRojas0630, Elkin77 Corporación Universitaria Minuto de Dios. All rights reserved.

This file is part of ProjectName (BudRot-AutomaticDetection).

ProjectName (BudRot-AutomaticDetection) is free software: you can redistribute it and/or modify it under the terms of the
GNU General Public License as published by the Free Software Foundation, version 3.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BAD_Web.settings')

application = get_wsgi_application()
