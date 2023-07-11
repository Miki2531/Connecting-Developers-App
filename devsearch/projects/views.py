from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
projectList = [
    {
        'id': '1',
        'title': 'Ecommerce website',
        'description': 'One of the largest business based website'
    },

    {'id': '2',
     'title': 'Food delivery website',
     'description': 'One of the largest business based website'

     },

    {'id': '3',
     'title': ' ',
     'description': 'One of the largest business based website'
     },

]


def projects(request):
    mesg = 'This is Miko Web development site!!'
    number = 11
    context = {'message': mesg, 'number': number, 'projects': projectList}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = None
    for i in projectList:
        if i['id'] == pk:
            projectObj = i

    return render(request, 'projects/single.project.html', {'project': projectObj})
