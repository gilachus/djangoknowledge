import random
from django.http import HttpResponse

def home_example(request):
    number = random.randint(1, 999)
    html_code = f"""<h1>Home example, welcome random {number}!!!<h1/>"""
    print("Alguien está en home example")
    return HttpResponse(html_code)