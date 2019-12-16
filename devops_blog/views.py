from django.shortcuts import render
from devops_blog.forms import blogform
# Create your views here.
def blogformview(request):

    if request.method == 'POST':
        form = blogform(data=request.POST)
        form = form.save()

    else:
        form = blogform()

    return render(request,'devops_blog/form.html',{'form':form})
