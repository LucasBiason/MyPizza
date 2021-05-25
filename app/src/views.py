from django.shortcuts import redirect
from django.http import HttpResponse


def index_redirect(request):
    ''' Redirect to Admin '''
    return redirect('admin/')

def safe(request):
    ''' Safe url to check '''
    return HttpResponse('My Pyzza Service Online')
