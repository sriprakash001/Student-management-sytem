from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def course_create(request):
    context = {
        'course_data':course_forms()
    }
    if request.method == 'POST':
        course_data = course_forms(request.POST)
        if course_data.is_valid():
            course_data.save()
            return redirect('courses_list')
    return render(request,'courses/course_create.html',context)

@login_required(login_url='/')
def course_list(request):
    context = {
        'all_courses':Course.objects.all()
    }
    return render(request,"courses/course_list.html",context)

@login_required(login_url='/')
def course_update(request,pk):
    select_course = get_object_or_404(Course,id = pk)
    context = {
        "course_data":course_forms(instance=select_course)
    }
    if request.method == 'POST':
        course_data = course_forms(request.POST,instance=select_course)
        if course_data.is_valid():
            course_data.save()
            return redirect('courses_list')
    return render(request,'courses/course_update.html',context)

@login_required(login_url='/')
def course_delete(request,pk):
    select_coures = get_object_or_404(Course,id = pk)
    select_coures.delete()
    return redirect('courses_list')












































