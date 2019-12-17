from django.shortcuts import render
from devops_blog.forms import blogform
from devops_blog.models import blogmodel
from devops_blog import views
# Create your views here.
def blogformview(request):

    if request.method == 'POST':
        form = blogform(data=request.POST)
        if form.is_valid():
            form.save()
            return views.thankyouview(request)

    else:
        form = blogform()

    return render(request,'devops_blog/form.html',{'form':form})

def all_blogsview(request):
    my_list = blogmodel.objects.order_by('author_name')
    my_dict = {'form':my_list}
    return render(request,'devops_blog/index.html',context=my_dict)

def thankyouview(request):
    return render(request,'devops_blog/thankyou.html')

def gitview(request):
    my_list = blogmodel.objects.order_by('author_name')
    my_dict = {'form':my_list}
    return render(request,'devops_blog/git.html',context=my_dict)
