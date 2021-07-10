import base64
import json
from typing import IO

from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    if request.method == 'POST':
        data = request.body
        # with open(request.body, 'rb') as fp:
        #     data = fp.read()
        out = base64.b64encode(data)

        print('6g')
        return HttpResponseBadRequest()
    else:
        # lol = json.loads(request.body)
        # obj = {
        #     'name': 'alex',
        #     'description': 'full idiot'
        # }
        # with open(request.body, 'rb') as f:
        #     contents = f.read()
        # with open(request.body, 'rb') as f:
        #     lines = [l.decode('utf8', 'ignore') for l in f.readlines()]
        # return JsonResponse(lines)
        filepath = 'MoD.png'
        with open(filepath, 'rb') as fp:
            data = fp.read()
        filename = 'MoD.png'
        response = HttpResponse(content_type="application/octet-stream")
        response['Content-Disposition'] = 'attachment; filename=%s' % filename  # force browser to download file
        response.write(data)

        return response
