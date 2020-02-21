from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'practice1/post_list.html',{})