# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse, render

import json
import requests

def index(request):

    persons = requests.get('https://thecountedapi.com/api/counted')
    json_persons = persons.text
    persons_info = json.loads(json_persons)
    parsedData = []
    for data in persons_info[:10000]:
        temp_dict = {}
        if data["armed"] == "No":
            temp_dict["day"] = data["day"]
            temp_dict["month"] = data["month"]
            temp_dict["year"] = data["year"]
            parsedData.append(temp_dict)
    count = (len(parsedData))

    return render(request, "people/index.html", {"peoples": parsedData})