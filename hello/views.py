from django.shortcuts import render,HttpResponse
from django.contrib.auth.admin import User
import datetime
from hello.models import Publisher
from hello.forms import PublisherForm
# Create your views here.
def test(request):
    value1 = 'This is a bag!'
    value2 = 10
    value3 = datetime.datetime.now()
    user_list = User.objects.all()
    return render(request,'table.html',locals())

def add_publisher(request):
    if request.method == 'POST':
        #1.不使用form情况接受用户传过来的数据
       # name = request.POST['name']
       # address = request.POST['address']
       # state_province = request.POST['state_province']
       # city = request.POST['city']
       # country = request.POST['country']
       # website = request.POST['website']
       # Publisher.objects.create(
       #     name= name,
       #     address= address,
       #     state_province= state_province,
       #     city = city,
       #     country= country,
       #     website = website,
       #
       # )
       # return HttpResponse('添加出版社成功！')
       #2.使用Djangoform
        # publisher_form = PublisherForm(request.POST)
        # if publisher_form.is_valid():
        #     Publisher.objects.create(
        #         name= publisher_form.cleaned_data['name'],
        #         address= publisher_form.cleaned_data['address'],
        #         state_province=publisher_form.cleaned_data['state_province'],
        #         city= publisher_form.cleaned_data['city'],
        #         country= publisher_form.cleaned_data['country'],
        #         website= publisher_form.cleaned_data['website'],
        #     )
        #     return HttpResponse('添加成功')
        # 3.使用DjangoModelform
        publisher_form = PublisherForm(request.POST)
        if publisher_form.is_valid():
            publisher_form.save()
            return  HttpResponse('添加出版社成功!')
        else:
            return HttpResponse('错误！')

    else:
        publisher_form = PublisherForm()
        return render(request,'add_publisher.html',locals())


