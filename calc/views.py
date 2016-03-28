from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sumador(request, num1, num2):
    try:
        result = int(num1) + int(num2)
        print_result = "<h3>Calculadora realizada con Django</h3>" + \
                        "<p>Suma: " + str(num1) + " + " + str(num2) + " = " +\
                        str(result) + "</p>"
    except ValueError:
        print_result = "<h3><font color='red'>Error! Tienes que introducir " +\
                        "numeros</font></h3>"

    response = HttpResponse(print_result)
    return response

def restador(request, num1, num2):
    try:
        result = int(num1) - int(num2)
        print_result = "<h3>Calculadora realizada con Django</h3>" + \
                        "<p>Resta: " + str(num1) + " - " + str(num2) + " = " +\
                        str(result) + "</p>"
    except ValueError:
        print_result = "<h3><font color='red'>Error! Tienes que introducir " +\
                        "numeros</font></h3>"

    response = HttpResponse(print_result)
    return response

def multiplicador(request, num1, num2):
    try:
        result = int(num1) * int(num2)
        print_result = "<h3>Calculadora realizada con Django</h3>" + \
                        "<p>Multipliacion: " + str(num1) + " * " + str(num2) +\
                        " = " + str(result) + "</p>"
    except ValueError:
        print_result = "<h3><font color='red'>Error! Tienes que introducir " +\
                        "numeros</font></h3>"

    response = HttpResponse(print_result)
    return response

def divisor(request, num1, num2):
    try:
        result = float(num1) / float(num2)
        print_result = "<h3>Calculadora realizada con Django</h3>" + \
                        "<p>Division: " + str(num1) + " / " + str(num2) + " = " +\
                        str(result) + "</p>"
    except ValueError:
        print_result = "<h3><font color='red'>Error! Tienes que introducir " +\
                        "numeros</font></h3>"
    except ZeroDivisionError:
        print_result = "<h3><font color='red'>Error: No se puede dividir " +\
                        "por cero!</font></h3>"

    response = HttpResponse(print_result)
    return response

def error(request):
    response = HttpResponse("<h3><font color='red'>Not found!</font></h3>")
    return response
