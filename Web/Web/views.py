from django.http import HttpResponse

def saluda(request):
    return HttpResponse('Hola a todos, que facil es programar en Django')

def part2(request):
    return HttpResponse('Avril Francesca Espinoza Quijano')

def saluda_nombre(request, nombre):
    return HttpResponse(f'Hola {nombre}!')