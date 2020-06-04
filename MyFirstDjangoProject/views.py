from django.http import HttpResponse
import datetime

def greet(request):
    return HttpResponse("Hello World")

def getDate(request):
    actualDate = datetime.datetime.now()
    response="""<html><p>Actual date</p><p>%s</p></html>""" %actualDate
    return HttpResponse(response)
