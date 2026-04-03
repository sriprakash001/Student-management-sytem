from django.shortcuts import render , redirect ,get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Count, Q
from .models import *
from courses.models import Course
from .forms import *
from django.contrib.auth.decorators import login_required
from .forms import Attendence_forms
from django.utils import timezone
from django.contrib import messages

@login_required(login_url='/')
def student_create(request):
    context = {
        'student_data':student_forms()
    }
    if request.method == 'POST':
        student_data = student_forms(request.POST)
        if student_data.is_valid():
            student_data.save()
            return redirect('students_list')
        else:
            print(student_data.errors) # to find an errors
    else:
        student_data = student_forms()
    return render(request,'students/student_create.html',context)

@login_required(login_url='/')
def student_list(request):
    search_query = request.GET.get("q","")
    all_students = Student.objects.all().order_by("-id")

    #Searching using Q
    if search_query:
        all_students = all_students.filter(
            Q(name__icontains = search_query)
        )

    # Pagination
    paginator = Paginator(all_students,5)  # 5 student per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'all_students':page_obj,
        'search_query':search_query
    }
    return render(request ,'students/student_list.html',context)

@login_required(login_url='/')
def student_update(request,pk):
    student_id = get_object_or_404(Student,id = pk)
    context = {
        'student_data':student_forms(instance=student_id)
    }
    if request.method == 'POST':
        student_data = student_forms(request.POST , instance=student_id)
        if student_data.is_valid():
            student_data.save()
            return redirect('students_list')
    return render(request,'students/student_update.html',context)

@login_required(login_url='/')
def student_delete(request,pk):
    student_id = get_object_or_404(Student,id = pk)
    context = {
        'student_del':student_id
    }
    if request.method == "POST":
        student_id.delete()
        return redirect('students_list')
    return render(request,'students/student_delete.html',context)


# ENROLLMENT FUNCTIONS
@login_required(login_url='/')
def entroll_student(request):
    context = {
        'entroll_form':Enrollment_forms()
    }
    if request.method == 'POST':
        entroll_form = Enrollment_forms(request.POST)
        if entroll_form.is_valid():
            entroll_form.save()
            return redirect('students_list')
    else:
        entroll_form = Enrollment_forms()
    return render(request,'students/entroll.html',context)

# DASHBOARD FUNCTIONS
@login_required(login_url='/')
def dashboard(request):
    context = {
        'students':Student.objects.count(),
        'courses':Course.objects.count(),
        'enrollments':Enrollment.objects.count()
    }
    return render(request,'students/dashboard.html',context)

# ATTENDENCE FUNCTIONS
@login_required(login_url='/')
def mark_attendence(request):
    students = Student.objects.all()
    courses = Course.objects.all()

    course_id = request.GET.get("course")
    today = timezone.now().date()

    if not course_id:
        return render(request, "students/attendence.html", {
            "courses": courses
        })

    # Create dynamic formset with correct extra forms
    AttendenceFormSet = modelformset_factory(
        Attendence,
        fields=("student", "status"),
        extra=students.count()
    )

    queryset = Attendence.objects.none()

    initial_data = []
    for student in students:
        initial_data.append({
            "student": student,
            "status": "Present"
        })

    formset = AttendenceFormSet(queryset=queryset, initial=initial_data)

    if request.method == "POST":
        formset = AttendenceFormSet(request.POST)

        if formset.is_valid():
            for form in formset:
                student = form.cleaned_data.get("student")
                status = form.cleaned_data.get("status")

                if student:  # important check
                    Attendence.objects.update_or_create(
                        student=student,
                        course_id=course_id,
                        date=today,
                        defaults={"status": status}
                    )

            messages.success(request, "Attendance Saved Successfully")
            return redirect(f"/attendence/?course={course_id}")

    return render(request, "students/attendence.html", {
        "formset": formset,
        "courses": courses,
        "course_id": course_id,
    })

# Attendence Dashboard
@login_required(login_url='/')
def attendance_dashboard(request):
    today = timezone.now().date()

    dashboard_data = (
        Course.objects.annotate(
            total_students=Count(
                "attendence",
                filter=Q(attendence__date=today)
            ),
            present=Count(
                "attendence",
                filter=Q(attendence__date=today, attendence__status="Present")
            ),
            absent=Count(
                "attendence",
                filter=Q(attendence__date=today, attendence__status="Absent")
            ),
            late=Count(
                "attendence",
                filter=Q(attendence__date=today, attendence__status="Late")
            ),
            excused=Count(
                "attendence",
                filter=Q(attendence__date=today, attendence__status="Excused")
            ),
        )
        .order_by("name")
    )

    return render(request, "students/attendence_dash.html", {
        "dashboard_data": dashboard_data,
        "today": today
    })

