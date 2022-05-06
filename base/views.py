from django.shortcuts import redirect, render
from .forms import CourseSignUpForm
from django.contrib import messages

from .models import CourseSignUp


# Create your views here.

def home(request):
    people = CourseSignUp.objects.all()
    person = people.first()
    print(vars(person))
    print(people)
    # if request.method == "POST":
    #     form = CourseSignUpForm(request.post)
    #     if form.is_valid():
    #         f = form.save(commit=False)
    #         f.course="fullstack_web_course_2022_06"
    #         f.save()

    #         messages.success(request, "Sign Up For Submitted Successfully")
    # else:
    form = CourseSignUpForm()
    
    context = {
        "form": form
    }

    return render(request, "home.html", context)

def sign_up(request):
    if request.method == "POST":
        form = CourseSignUpForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.course="fullstack_web_course_2022_06"
            f.save()

            messages.success(request, "Sign Up For Submitted Successfully")
            redirect("home")
    else:
            redirect("home")

