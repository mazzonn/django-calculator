from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    try:
        if request.method == 'POST':
            button_value = request.POST.get('button')

            if button_value == 'AC':
                new_value = ''
            elif button_value == '=':
                current_value = request.POST.get('current_value', '')
                new_value = eval(str(current_value))
            else:
                current_value = request.POST.get('current_value', '')
                new_value = current_value + button_value

            return render(request, 'home.html', {'input_value': new_value})
    except:
        return render(request, 'home.html', {'input_value': 'Error'})

    return render(request, 'home.html', {'input_value': ''})