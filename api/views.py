from django.shortcuts import render
from django.http import HttpResponse


def main_api(request):
    return HttpResponse('alo')