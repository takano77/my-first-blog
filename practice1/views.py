from django.shortcuts import render
from .forms import PostForm
from django.shortcuts import redirect
# Create your views here.
def post_list(request):
    return render(request, 'practice1/post_list.html',{})
def clothes_list(request):
    if request.method == "POST":
        results = request.POST
        #return redirect(request, 'closet',{'color':results})
        return render(request, 'practice1/closet.html',{'color':results})
    else:
        form=PostForm()
    return render(request, 'practice1/clothes_list.html',{'form':form})

def closet(request):
    return render(request, 'practice1/closet.html',{'color':color})