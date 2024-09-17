from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

days = {
    'saturday': 'this is saturday',
    'sunday': 'this is sunday',
    'monday': 'this is monday',
    'tuesday': 'this is tuesday',
    'wednesday': 'this is wednesday',
    'thursday': 'this is thursday',
    'friday': 'this is friday',
}

#def saturday(request):
#    return HttpResponse("this is saturday")
#
#def sunday(request):
#    return HttpResponse("this is sunday")
#
#def monday(request):
#    return HttpResponse("this is monday")

def days_list(request):
    days_list = list(days.keys())
    list_items = ""

    for day in days_list:
        url_path = reverse('days-of-week', args=[day])
        list_items += f'<li> <a href = "{url_path}"> {day} </a></li> \n'



    content = f'<ul> {list_items} </ul>'
    return HttpResponse(content)

def dynamic_days_by_number(request, day):
    days_names = list(days.keys())
    if day > len(days_names):
        return HttpResponseNotFound('day does not found')
    redirect_day = days_names[day-1]
    redirect_url = reverse('days-of-week', args = [redirect_day])
    return HttpResponseRedirect(redirect_url)
    #return HttpResponse(day)

def dynamic_days(request, day):
    day_data = days.get(day)
    if day_data is not None:
        response_data = f'<h1 style = "color:red">day is : {day} and description is {day_data}</h1>'
        return HttpResponse(response_data)
    return HttpResponseNotFound('day does not found')