from django.shortcuts import render

def about_me(request):
    return render(request, 'personal/about_me.html')

def projects(request):
    return render(request, 'personal/projects.html')

def tech_stack(request):
    return render(request, 'personal/tech_stack.html')


