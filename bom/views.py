from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
import hashlib
import os

@csrf_exempt
def register(request):
	json = {
		"ResultCode": 200,
		"Message": "注册成功"
	}
	if request.method == 'POST':
		name = request.POST.get("username", None)
		password = request.POST.get("password", None)
		email = request.POST.get("email", None)
		# 用md5 hash生成密码摘要并储存
		password = sha256hash(password)
		user = User.objects.filter(name=name)
		# 无重复用户, 成功注册
		if not user:
			user = User(name=name, password=password, email=email)
			user.save()
			return JsonResponse(json)
		else:
			json["ResultCode"] = 501
			json["Message"] = "用户名已被注册"
			return JsonResponse(json)



def logout(request):
	del request.session['user_info']
	return redirect('/')


# 用md5加密用户密码
def sha256hash(psw):
	h = hashlib.sha256()
	h.update(psw.encode('utf-8'))
	password = h.hexdigest()

	return password


# 判断用户登陆状态
def auth(request):
	try:
		user = User.objects.get(name=request.session.get('user_info', None)["name"])

		return user
	except Exception as e:
		print(e)
		return False