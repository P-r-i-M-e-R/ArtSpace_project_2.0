from django.shortcuts import render, redirect
from .forms import User_Registration_Form

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = User_Registration_Form(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)  # Сохраняем без коммита, чтобы обработать пароль

            if 'avatar' in request.FILES:
                user.avatar = request.FILES['avatar']

            # Сохраняем обрезанное изображение как миниатюру
            if 'avatar_thumbnail' in request.FILES:
                user.avatar_thumbnail = request.FILES['avatar_thumbnail']


            user.set_password(form.cleaned_data['password'])  # Устанавливаем пароль
            user.save()  # Сохраняем пользователя в базу данных
            return redirect('register')  # Перенаправляем после успешной регистрации
    else:
        form = User_Registration_Form()
    return render(request, 'register.html', {'form': form})