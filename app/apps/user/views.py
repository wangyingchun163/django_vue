from django.shortcuts import HttpResponse, render, redirect

#登录接口
def login(request):
    if request.method == 'GET':
        # return HttpResponse("OK")
        # return redirect('http://192.168.1.11')
        return render(request, "index.html", {"name": "monicx", "hobby": ["reading", "blog"]})
    if request.method == 'POST':
        # 这里判断，如果是name值为login的，则执行此段代码
        if 'login' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username, password=password).first()
            if user_obj:
                # return HttpResponse('登录成功')
                request.session['is_login'] = '1'
                request.session['username'] = username
                return redirect('/infinigo_devops/index/')
            else:
                #return redirect('/infinigo_devops/login/',{"error_info":"用户名或者密码错误！"})
                return render(request, 'devops/user/login.html',{"error_info":"用户名或者密码错误！"})

        elif 'register' in request.POST:
            return redirect('/infinigo_devops/register/')
        else:
            return HttpResponse('需要注册才能访问哦，请先注册账号...')