from django.urls import path

from . import views
# Эта строчка обязательна.
# Без неё namespace работать не будет:
# namespace должен быть объявлен при include и тут, в app_name
app_name = 'posts'

urlpatterns = [
    # главная страница
    path('', views.index, name='index'),
    # страница списка постов
    path('group/<slug:slug>/', views.group_posts, name='group_posts'),
    # slug(это строка из букв и циф path('group/<slug:slug>/'
]
