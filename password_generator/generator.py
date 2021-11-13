from django.http import HttpResponse
import random
import string

def index(request):
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 16))
    return HttpResponse(ran_str)