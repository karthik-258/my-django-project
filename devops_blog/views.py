from django.shortcuts import render
from devops_blog.forms import blogform
from devops_blog.models import blogmodel
# Create your views here.
def blogformview(request):

    if request.method == 'POST':
        form = blogform(data=request.POST)
        form = form.save()

    else:
        form = blogform()

    return render(request,'devops_blog/form.html',{'form':form})

def all_blogsview(request):
    my_list = blogmodel.objects.order_by('author_name')
    my_dict = {'form':my_list}
    return render(request,'devops_blog/index.html',context=my_dict)
