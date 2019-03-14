from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .models import Post
from django.http import HttpResponse
from django.db import IntegrityError
import sqlite3
from django.shortcuts import render_to_response


import templates

# conn = sqlite3.connect('C:\Shreedhar_Projects\SHR_HTML\db.sqlite3')
# c = conn.cursor()
# print(c.execute('select * from Form_Validation_post'))
#
# shr = c.execute('Select * from Form_Validation_post')
# print(c.fetchall())

# @csrf_protect
def createpost(request):
    # try:
        if request.method == 'POST':
            print("hegde")
            if request.POST.get('title') and request.POST.get('content'):
                post = Post()
                post.title = request.POST.get('title')
                post.content = request.POST.get('content')
                print(post.title)
                print(post.content)
                post.save()
                return HttpResponse("sved")
        else:
            return render(request, 'Shr_Template/createpost.html')

# @csrf_protect
def employeeDetails(request):
    # try:
        print("hegde")
        print(request.method)
        if request.method == 'POST':
            print("huli")
            if request.POST.get('First name') and request.POST.get('lastname') and request.POST.get('email') and request.POST.get('mobileno') and request.POST.get('company'):
                post = Post()
                post.firstname = request.POST.get('firstname')
                post.lastname = request.POST.get('lastname')
                post.email = request.POST.get('email')
                post.mobileno = request.POST.get('mobileno')
                post.company = request.POST.get('company')
                print(post.firstname)
                print(post.lastname)
                post.save()
                return HttpResponse("sved")
        else:
            return render(request, 'Shr_Template/form1234.html')
    # except  ValueError:
    #     print("Exception Handled")
    # except IntegrityError:
    #     print("handled")
# def AddData(request) :db
#     return render(request,templates/)

# @csrf_protectdjango_migrations
# def post(self , request):
#     form = AddUser(request.POST or None)
#     context = { 'form': form }
# if form.is_valid():
#     first_name = form.cleaned_data['first_name']
#     context.update({'first_name': first_name})
#     last_name = form.cleaned_data['last_name']
#     context.update({'last_name': last_name})
#     salary = form.cleaned_data['salary']
#     context.update({'salary': salary})
#     country = form.cleaned_data['country']
#     context.update({'country': country})
#     city = form.cleaned_data['city']
#     context.update({'city': city})
#     return render(request, self.template_name, context)
