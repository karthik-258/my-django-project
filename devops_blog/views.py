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

def jenkinsview(request):
    my_list = blogmodel.objects.order_by('author_name')
    my_dict = {'form':my_list}
    return render(request,'devops_blog/jenkins.html',context=my_dict)

def ansibleview(request):
    my_list = blogmodel.objects.order_by('author_name')
    my_dict = {'form':my_list}
    return render(request,'devops_blog/ansible.html',context=my_dict)

def buildtoolsview(request):
    my_list = blogmodel.objects.order_by('author_name')
    my_dict = {'form':my_list}
    return render(request,'devops_blog/buildtools.html',context=my_dict)

def cloudview(request):
    my_list = blogmodel.objects.order_by('author_name')
    my_dict = {'form':my_list}
    return render(request,'devops_blog/cloud.html',context=my_dict)

def datascienceview(request):
    my_list = blogmodel.objects.order_by('author_name')
    my_dict = {'form':my_list}
    return render(request,'devops_blog/datascience.html',context=my_dict)

def dockerview(request):
    my_list = blogmodel.objects.order_by('author_name')
    my_dict = {'form':my_list}
    return render(request,'devops_blog/docker.html',context=my_dict)

def kubernatesview(request):
    my_list = blogmodel.objects.order_by('author_name')
    my_dict = {'form':my_list}
    return render(request,'devops_blog/kubernates.html',context=my_dict)

def linuxview(request):
    my_list = blogmodel.objects.order_by('author_name')
    my_dict = {'form':my_list}
    return render(request,'devops_blog/linux.html',context=my_dict)

def machinelearningview(request):
    my_list = blogmodel.objects.order_by('author_name')
    my_dict = {'form':my_list}
    return render(request,'devops_blog/machinelearning.html',context=my_dict)

def monitoringtoolsview(request):
    my_list = blogmodel.objects.order_by('author_name')
    my_dict = {'form':my_list}
    return render(request,'devops_blog/monitoringtools.html',context=my_dict)

def pythonview(request):
    my_list = blogmodel.objects.order_by('author_name')
    my_dict = {'form':my_list}
    return render(request,'devops_blog/python.html',context=my_dict)
