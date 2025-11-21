from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_approved = False
            user.role = 2  # 默认注册为读者
            user.save()
            return redirect('login')  # 注册成功后跳转登录页
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})