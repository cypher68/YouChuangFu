from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from myapp.models import *
from myapp.models import book

@csrf_exempt
def add_user(request):
    try:
        # 创建模型类实例
        addUser = book()  # 根据实际模型修改
        # 从请求中获取数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        addUser = book(username=username,password=password)


        # 调用 save 方法，保存数据到数据库
        addUser.save()

        # 返回成功的 JSON 响应
        return JsonResponse({
            'status': 'success',
            'message': 'User added successfully.',
            'user_id': addUser.id
        })
    except Exception as e:
        # 捕获异常并返回错误信息
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        })# 调用save方法，保存数据到数据库

def get_user(request):
    # 获取所有书籍数据
    books = book.objects.all().values()

    # 返回 JSON 响应
    return JsonResponse(list(books), safe=False)


def find_user(request):
    # 从请求中获取查询参数
    username = request.GET.get('username')

    if not username:
        return JsonResponse({
            'status': 'error',
            'message': 'Username is required.'
        })

    try:
        # 查询数据库中是否存在该用户
        user = book.objects.filter(username=username).values('username', 'password')  # 确保返回密码字段

        if user.exists():
            # 返回找到的用户信息
            return JsonResponse({
                'status': 'success',
                'data': list(user)  # 将 QuerySet 转换为列表
            })
        else:
            # 用户不存在
            return JsonResponse({
                'status': 'not_found',
                'message': 'User not found.'
            })
    except Exception as e:
        # 捕获异常并返回错误信息
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        })

@csrf_exempt
def delete_user(request):
    try:
        # 获取请求中的用户名
        username = request.POST.get('username')

        # 检查用户名是否为空
        if not username:
            return JsonResponse({
                'status': 'error',
                'message': 'Username is required.'
            })

        # 查找用户
        try:
            user = book.objects.get(username=username)
        except book.DoesNotExist:
            return JsonResponse({
                'status': 'error',
                'message': 'User not found.'
            })

        # 删除用户
        user.delete()

        # 返回成功响应
        return JsonResponse({
            'status': 'success',
            'message': f'User {username} deleted successfully.'
        })
    except Exception as e:
        # 捕获异常并返回错误信息
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        })

@csrf_exempt
def update_user_password(request):
    try:
        # 从请求中获取数据
        username = request.POST.get('username')
        newPassword = request.POST.get('password')

        # 检查数据是否为空
        if not username or not newPassword:
            return JsonResponse({
                'status': 'error',
                'message': 'Username and new password are required.'
            })

        # 查找用户
        try:
            user = book.objects.get(username=username)
        except book.DoesNotExist:
            return JsonResponse({
                'status': 'error',
                'message': 'User not found.'
            })

        # 更新用户的密码
        user.password = newPassword
        user.save()

        # 返回成功的 JSON 响应
        return JsonResponse({
            'status': 'success',
            'message': f'Password for user {username} updated successfully.'
        })
    except Exception as e:
        # 捕获异常并返回错误信息
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        })

@csrf_exempt
def add_project(request):
    try:
        # 从请求中获取数据
        projectname = request.POST.get('projectname')
        projectteam = request.POST.get('projectteam')
        projectpeople = request.POST.get('projectpeople')
        companysituation = request.POST.get('companysituation')
        projectdescription = request.POST.get('projectdescription')
        #projectimage = request.FILES.get('image')  # 获取上传的文件

        # 检查必填字段是否为空
        if not projectname or not projectteam or not projectpeople:
            return JsonResponse({
                'status': 'error',
                'message': 'Project name, team, and people are required.'
            })

        # 创建新的项目实例并保存到数据库
        project = Project(
            projectname=projectname,
            projectteam=projectteam,
            projectpeople=int(projectpeople),
            companysituation=companysituation,
            projectdescription=projectdescription,
            #image=projectimage  # 将图片赋值给项目
        )
        project.save()

        # 返回成功的 JSON 响应
        return JsonResponse({
            'status': 'success',
            'message': 'Project added successfully.',
            'project_id': project.id
        })
    except Exception as e:
        # 捕获异常并返回错误信息
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        })


@csrf_exempt
def delete_project(request):
    try:
        # 从请求中获取项目名称
        projectname = request.POST.get('projectname')

        # 检查项目名称是否为空
        if not projectname:
            return JsonResponse({
                'status': 'error',
                'message': 'Project name is required.'
            })

        # 查找并删除项目
        try:
            project = Project.objects.get(projectname=projectname)
            project.delete()
            return JsonResponse({
                'status': 'success',
                'message': f'Project "{projectname}" deleted successfully.'
            })
        except Project.DoesNotExist:
            return JsonResponse({
                'status': 'error',
                'message': 'Project not found.'
            })
    except Exception as e:
        # 捕获异常并返回错误信息
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        })

@csrf_exempt
def update_project(request):
    try:
        # 从请求中获取项目名称
        projectname = request.POST.get('projectname')

        # 检查项目名称是否为空
        if not projectname:
            return JsonResponse({
                'status': 'error',
                'message': 'Project name is required.'
            })

        # 查找项目
        try:
            project = Project.objects.get(projectname=projectname)
        except Project.DoesNotExist:
            return JsonResponse({
                'status': 'error',
                'message': 'Project not found.'
            })

        # 获取新的项目信息
        new_projectteam = request.POST.get('projectteam')
        new_projectpeople = request.POST.get('projectpeople')
        new_companysituation = request.POST.get('companysituation')
        new_projectdescription = request.POST.get('projectdescription')

        # 更新项目信息
        if new_projectteam:
            project.projectteam = new_projectteam
        if new_projectpeople:
            project.projectpeople = int(new_projectpeople)
        if new_companysituation:
            project.companysituation = new_companysituation
        if new_projectdescription:
            project.projectdescription = new_projectdescription

        # 保存更改
        project.save()

        # 返回成功的 JSON 响应
        return JsonResponse({
            'status': 'success',
            'message': f'Project "{projectname}" updated successfully.'
        })
    except Exception as e:
        # 捕获异常并返回错误信息
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        })

# 视图函数，用于列出所有项目
def list_projects(request, sort_by='projectname'):
    # 根据排序参数选择排序字段
    if sort_by == 'projectteam':
        projects = Project.objects.order_by('projectteam')
    else:
        projects = Project.objects.order_by('projectname')

    # 构建项目列表的 JSON 数据
    projects_list = list(projects.values())

    return JsonResponse({'projects': projects_list})
