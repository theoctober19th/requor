from django.shortcuts import render, redirect
from qna_app.models import UserModel

# Create your views here.

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = UserModel.objects.filter(email=email, password=password)
        if user.count() >0:
            #user is logged in successfully
            request.session['id'] = user[0].id
            request.session['name'] = user[0].name
            request.session['email'] = user[0].email

            return redirect('qna.index')
        else:
            return render(request, 'user_app/login.html')
    else:
        return render(request, 'user_app/login.html')

def logout(request):
    request.session.flush()
    return redirect('user.login')
