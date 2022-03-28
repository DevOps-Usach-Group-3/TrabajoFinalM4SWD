from curses.ascii import HT
from django.shortcuts import render
from .forms import DxcForm

from .utils import get_response

def index(request):
    context = {}    
    return render(request, 'dxc/index.html', context)


def retiro(request):
    answered = False
    dxc = None
    tipo = None
    message = None
    valor = None

    if request.method == 'POST':
        dxc_form = DxcForm(data=request.POST)

        if dxc_form.is_valid():
            sueldo = int(dxc_form.cleaned_data['sueldo'])
            ahorro = int(dxc_form.cleaned_data['ahorro'])
            tipo =  dxc_form.cleaned_data['tipo']

            print(f"Tipo: {tipo}")

            dxc = get_response(sueldo, ahorro, tipo)
            answered = True

            # Generar mensaje de salida
            valor = dxc['valor']
            if tipo == '10x100':
                message = 'Pidiendo el 10% usted podrá retirar:'
            elif tipo == 'saldo':
                message = 'Pidiendo el 10% su saldo restante será de:'
            elif tipo == 'impuesto':
                message = 'El impuesto a pagar es de:'


    else:
        dxc_form = DxcForm()

    context = {
        'dxc_form': dxc_form,
        'answered': answered,
        'dxc': dxc,
        'tipo': tipo,
        'message': message,
        'valor': valor
    }  
    return render(request, 'dxc/retiro.html', context)
