import datetime

import jwt
from django.conf import settings
from django.db import DatabaseError
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.utils import timezone
from jwt import InvalidTokenError
from rest_framework.decorators import api_view
from rest_framework.response import Response

from polls.captcha import Captcha
from polls.models import Subject, Teacher, User
from polls.serializers import SubjectSerializer, TeacherSerializer, SubjectSimpleSerializer
from polls.utils import gen_random_code, gen_md5_digest


def show_index(requests: HttpRequest) -> HttpResponse:
    return redirect('/static/html/subjects.html')


@api_view(('GET', ))
def show_subjects(request: HttpRequest) -> HttpResponse:
    subjects = Subject.objects.all().order_by('no')
    serializer = SubjectSerializer(subjects, many=True)
    return Response(serializer.data)


@api_view(('GET', ))
def show_teachers(request: HttpRequest) -> HttpResponse:
    try:
        sno = int(request.GET.get('sno'))
        subject = Subject.objects.only('name').get(no=sno)
        teachers = Teacher.objects.filter(subject=subject).defer('subject').order_by('no')
        subject_seri = SubjectSimpleSerializer(subject)
        teacher_seri = TeacherSerializer(teachers, many=True)
        return Response({'subject': subject_seri.data, 'teachers': teacher_seri.data})
    except (TypeError, ValueError, Subject.DoesNotExist):
        return Response(status=404)


def praise_or_criticize(request: HttpRequest) -> HttpResponse:
    token = request.META.get('HTTP_TOKEN')
    if token:
        try:
            jwt.decode(token, settings.SECRET_KEY)
            tno = int(request.GET.get('tno'))
            teacher = Teacher.objects.get(no=tno)
            if request.path.startswith('/praise/'):
                teacher.good_count += 1
                count = teacher.good_count
            else:
                teacher.bad_count += 1
                count = teacher.bad_count
            teacher.save()
            data = {'code': 20000, 'mesg': '投票成功', 'count': count}
        except (ValueError, Teacher.DoesNotExist):
            data = {'code': 20001, 'mesg': '投票失败'}
        except InvalidTokenError:
            data = {'code': 20002, 'mesg': '登录已过期，请重新登录'}
    else:
        data = {'code': 20002, 'mesg': '请先登录'}
    return JsonResponse(data)


def get_captcha(request: HttpRequest) -> HttpResponse:
    captcha_text = gen_random_code()
    request.session['captcha'] = captcha_text
    image_data = Captcha.instance().generate(captcha_text)
    return HttpResponse(image_data, content_type='image/png')


@api_view(('POST', ))
def login(request: HttpRequest) -> HttpResponse:
    username = request.data.get('username')
    password = request.data.get('password')
    if username and password:
        password = gen_md5_digest(password)
        user = User.objects.filter(username=username, password=password).first()
        if user:
            payload = {
                'exp': timezone.now() + datetime.timedelta(days=1),
                'userid': user.no
            }
            token = jwt.encode(payload, settings.SECRET_KEY).decode()
            return Response({'code': 10000, 'token': token, 'username': user.username})
        else:
            hint = '用户名或密码错误'
    else:
        hint = '请输入有效的用户名和密码'
    return Response({'code': 10001, 'mesg': hint})


@api_view(('POST', ))
def register(request: HttpRequest) -> HttpResponse:
    agreement = request.data.get('agreement')
    if agreement:
        username = request.data.get('username')
        password = request.data.get('password')
        tel = request.data.get('tel')
        if username and password and tel:
            try:
                password = gen_md5_digest(password)
                user = User(username=username, password=password, tel=tel)
                user.save()
                return Response({'code': 30000, 'mesg': '注册成功'})
            except DatabaseError:
                hint = '注册失败，请尝试更换用户名'
        else:
            hint = '请输入有效的注册信息'
    else:
        hint = '请勾选同意网站用户协议及隐私政策'
    return Response({'code': 30001, 'mesg': hint})
