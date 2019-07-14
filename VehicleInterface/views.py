# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from VehicleInterface import database

import logging
logger = logging.getLogger(__name__)


def home_page(request):
    if request.method == 'POST':
        selected_date = request.POST.get('selected_date')
        logger.debug("Coming date: %s" % selected_date)
        get_report_table_information = database.fill_report_table(selected_date)

        return HttpResponse(get_report_table_information, content_type="application/json")
    else:
        get_vehicles = database.get_vehicle()
        context = {'vehicles': get_vehicles}
        return render(request, 'home_page.html', context)
