from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .models import Post
import templates

# @csrf_protect
def createpost(request):
    print('hi')
    if request.method == 'POST':
        print("hegde ")
        if request.POST.get('title') and request.POST.get('content'):
            post = Post()
            post.title = request.POST.get('title')
            post.content = request.POST.get('content')
            post.save()

            return render(request, 'Shr_Template/createpost.html')

    else:
        return render(request, 'Shr_Template/createpost.html')
# def AddData(request) :
#     return render(request,templates/)

# @csrf_protect
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
