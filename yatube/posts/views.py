from django.shortcuts import render, get_object_or_404

from .models import Post, Group


# from .models import Post
NUM_POST = 10


# Главная страница
def index(request):
    posts = Post.objects.order_by('-pub_date')[:NUM_POST]
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'title': 'Последние обновления на сайте',
        'posts': posts,
    }
    # Третьим параметром передаём словарь context
    return render(request, 'posts/index.html', context)


# Страница со списком постов
def group_posts(request, slug):
    # Функция get_object_or_404 получает по заданным критериям объект
    # из базы данны{% block title %}
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=slug)

    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:NUM_POST]
    context = {
        'title': 'записи сообщества',
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
