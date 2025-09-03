from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406436890',
        'name': 'Nita Pasaribu',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)