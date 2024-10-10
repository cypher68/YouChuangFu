"""
URL configuration for djangoProject1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]
from django.urls import path
from myapp.views import *
from myapp.views import find_user  # 导入 find_user 视图函数
urlpatterns = [
    path('addUser/', add_user, name='add_user'),              # 添加数据
    path('getUser/', get_user),              # 查询数据
    path('findUser/',find_user,name='find_user'),
    path('updateUserPassword/', update_user_password, name='update_user_password'),
    path('deleteUser/',delete_user,name='delete_user'),
    path('addProject/', add_project, name='add_project'),
    path('deleteProject/', delete_project, name='delete_project'),
    path('updateProject/', update_project, name='update_project'),
    path('listProjects/',list_projects,name='list_projects')
]
