from django.shortcuts import render, redirect
from .forms import Post_Creation_Form

# Create your views here.

def create_post(request):
    if request.method == 'POST':
        form = Post_Creation_Form(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  # Сохраняем пост в базу данных

            if 'image' in request.FILES:
                post.image = request.FILES['image']

            # Сохраняем обрезанное изображение как миниатюру
            if 'image_thumbnail' in request.FILES:
                post.image_thumbnail = request.FILES['image_thumbnail']

            post.save()

            return redirect('creation')  # Перенаправляем после успешной загрузки поста
    else:
        form = Post_Creation_Form()
    return render(request, 'create_post.html', {'form': form})