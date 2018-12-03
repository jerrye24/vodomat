# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def reports(request):
    return render(request, 'reports/reports.html')