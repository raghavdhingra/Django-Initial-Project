from django.shortcuts import render
import django.contrib.sessions

# Create your views here.
def post_list(request):
    return render(request, 'post_list.html',{})

def name(request):
    get_name = request.POST['text']
    print(get_name)
    request.session['name'] = get_name
    print(request.session['name'])
    return render(request,'output.html',{})

def delete(request):
    del request.session['name']
    return render(request,'output.html',{})