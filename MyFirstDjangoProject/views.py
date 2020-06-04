from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render
import datetime

def greet(request):
    #open_template = open("C:/Users/Andreu/Documents/uoc/django/MyFirstDjangoProject/MyFirstDjangoProject/templates/greet.html")
    #tmplt = Template(open_template.read())
    #open_template.close()
    #ctx = Context({"name":"django"})
    #tmplt = loader.get_template('greet.html')
    #response = tmplt.render({"name":"django a python framework"})
    return render(request, "greet.html", {"name":"django a python framework"})

def get_date(request):
    actualDate = datetime.datetime.now()
    response="""<html><p>Actual date</p><p>%s</p></html>""" %actualDate
    return HttpResponse(response)

def calculate_age(request, age, year):
    newAge = (year - 2020) + age
    response = """<html><body><p> In this %s you will have %s years old</body></html>""" % (year, newAge)
    return HttpResponse(response)
