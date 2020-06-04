from django.http import HttpResponse
from django.template import Template, Context
import datetime

def greet(request):
    open_template = open("C:/Users/Andreu/Documents/uoc/django/MyFirstDjangoProject/MyFirstDjangoProject/templates/greet.html")
    tmplt = Template(open_template.read())
    open_template.close()
    ctx = Context()
    response = tmplt.render(ctx)
    return HttpResponse(response)

def get_date(request):
    actualDate = datetime.datetime.now()
    response="""<html><p>Actual date</p><p>%s</p></html>""" %actualDate
    return HttpResponse(response)

def calculate_age(request, age, year):
    newAge = (year - 2020) + age
    response = """<html><body><p> In this %s you will have %s years old</body></html>""" % (year, newAge)
    return HttpResponse(response)
