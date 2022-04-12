from django.http import HttpResponse
from datetime import date, datetime
from django.template import Context, Template
from django.template import loader

def saluda(request):
    return HttpResponse('Hola a todos, que facil es programar en Django')

def part2(request):
    return HttpResponse('Abby')

def saluda_nombre(request, nombre):
    return HttpResponse(f'Hola {nombre}!')

def saluda_nombre_edad(request, nombre, edad):

    plantilla = loader.get_template('template2.html')

    return HttpResponse(plantilla.render({"name": nombre, "edad": edad}))

def probandoTemplate(request, nombre):
    
    listaNotas = [8, 4, 9, 1, 10]


    # miHtml = open('C:/Users/jesus/Desktop/Django/ProyectoFinal/Web/Web/templates/template1.html')

    # plantilla = Template(miHtml.read())

    # miHtml.close()

    # miContexto = Context({"name": nombre, "ahora": datetime.now(), "notas": listaNotas})

    # return HttpResponse(plantilla.render(miContexto))

    plantilla = loader.get_template('template1.html')

    return HttpResponse(plantilla.render({"name": nombre, "ahora": datetime.now(), "notas": listaNotas}))