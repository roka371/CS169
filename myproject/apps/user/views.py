from django.shortcuts import render
from django.http import HttpResponse
import json
from myproject.apps.user.models import User
from django.views.decorators.csrf import csrf_exempt
import unittest
from StringIO import StringIO
from myproject.apps.user.tests import AddTests, LoginTests, ResetTests

# Create your views here.

@csrf_exempt
def login(request):
    try:
        if request.method == "POST":
            request = json.loads(request.body)
            count = User.objects.login(user = request['user'], password = request['password'])
            if count < 0:
                response['errCode'] = count
            else:
                response['errCode'] = 1
                response['count'] = count
            return HttpResponse(json.dumps(response), content_type = "application/json")
    except:
        return HttpResponse(status=500)

@csrf_exempt
def add(request):
    try:
        if request.method == "POST":
            request = json.loads(request.body)
            count = User.objects.add(user = request['user'], password = request['password'])
            response = {}
            if count < 0:
                response['errCode'] = count
            else:
                response['errCode'] = 1
                response['count'] = count
            return HttpResponse(json.dumps(response), content_type = "application/json")
    except:
        return HttpResponse(status=500)

@csrf_exempt
def reset(request):
    try:
        if request.method == "POST":
            response = {}
            response['errCode'] = User.objects.TESTAPI_resetFixture()
            return HttpResponse(json.dumps(response), content_type = "application/json")
    except:
        return HttpResponse(status=500)

@csrf_exempt
def test(request):
    if request.method == "POST":
        result = StringIO()
        tests = ( AddTests , LoginTests , ResetTests)
        response = {}
        response['nrFailed'] = 0
        response['totalTests'] = 0
        for t in tests:
            test = unittest.TestLoader().loadTestsFromTestCase(t)
            tresult = unittest.TextTestRunner(stream = result, verbosity=5).run(test)
            response['nrFailed'] += len(tresult.failures)
            response['totalTests'] += tresult.testsRun
        response['output'] = result.getvalue()
        return HttpResponse(json.dumps(response), content_type="application/json", status=200)
    else:
        return HttpResponse(200)