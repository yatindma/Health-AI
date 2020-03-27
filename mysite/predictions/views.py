from django.http import HttpResponse
from predictions import utility  as util
from django.shortcuts import render

def index(request):
    sentence = ""
    obj = util.Utility_()
    sentence = obj.get_heart_attack(request_obj = request)
    conte = {
        'name':'yatin'
    }
    return render(request, 'predictions/index.html',context=conte)
    # return HttpResponse(content=str(sentence))