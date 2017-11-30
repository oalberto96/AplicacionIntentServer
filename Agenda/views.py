from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from Agenda.models import *
import json
from django.http import JsonResponse


# Create your views here.
@csrf_exempt
def get_user_list(request):
    if request.method == "GET":
        contactos = Contacto.objects.all()
        if contactos:
            json_contacts = {'results': [model_to_dict(ob)for ob in contactos]}

            return JsonResponse(json_contacts, safe=False, content_type='application/json')
