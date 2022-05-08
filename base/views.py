from django.shortcuts import redirect, render
from .forms import CourseSignUpForm
from django.contrib import messages

from .models import CourseSignUp


# Create your views here.

def home(request):
    people = CourseSignUp.objects.all()
    # print(people)
    # if request.method == "POST":
    #     form = CourseSignUpForm(request.POST)
    #     if form.is_valid():
    #         f = form.save(commit=False)
    #         f.course="fullstack_web_course_2022_06"
    #         f.save()

    #         messages.success(request, "Sign Up For Submitted Successfully")
    #         redirect("home")
    # else:
    #     form = CourseSignUpForm()
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
            return redirect("home")
    else:
            messages.error(request, "Something wrong happened. Please contact webdevacademybh@gmail.com")
            return redirect("home")

