from django.shortcuts import render

def index(request):
    return render(request, 'catalog/index.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        massage = request.POST.get('massage')
        print(f'{name} email - {email}, сообщение - ({massage})')

    return render(request, 'catalog/contacts.html')
