from django.http import HttpResponse
import datetime

def greet(request):
    return HttpResponse("Hello World")

def getDate(request):
    actualDate = datetime.datetime.now()
    response="""<html><p>Actual date</p><p>%s</p></html>""" %actualDate
    return HttpResponse(response)

def calculateAge(request, age, year):
    newAge = (year - 2020) + age
    response = """<html><body><p> In this %s you will have %s years old</body></html>""" % (year, newAge)
    return HttpResponse(response)
