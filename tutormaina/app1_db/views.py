from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Topic, Department, Course, Author
from .forms import NewUserForm

def single_slug(request, single_slug):

    departments = [d.department_slug for d in Department.objects.all()]
    if single_slug in departments:
        course_series = Course.objects.filter(department_name__department_slug=single_slug)

        return render(request=request,
                      template_name='app1_db/course.html',
                      context={"course_series": course_series})

    courses = [c.course_slug for c in Course.objects.all()]
    if single_slug in courses:
        author_series = Author.objects.filter(course_name__course_slug = single_slug)

        return render(request,
                      'app1_db/author.html',
                      {"author_series": author_series})

    authors = [a.author_slug for a in Author.objects.all()]
    if single_slug in authors:
        topic_series = Topic.objects.filter(author_name__author_slug = single_slug)

        return render(request,
                      'app1_db/topic.html',
                      {"topic_series": topic_series})

    topics = [t.topic_slug for t in Topic.objects.all()]
    if single_slug in topics:
        clicked_topic = Topic.objects.get(topic_slug=single_slug)
        topics_fromthis_series = Topic.objects.filter(author_name__author_name=clicked_topic.author_name)
        this_topic_idx = list(topics_fromthis_series).index(clicked_topic)

    return render(request=request,
                      template_name='app1_db/viewtopic.html',
                      context={"topic": clicked_topic,
                               "sidebar": topics_fromthis_series,
                               "this_tut_idx": this_topic_idx})

    return HttpResponse("not found anything")
# Create your views here.
def homepage(request):
    return render(request = request,
                  template_name='app1_db/departments.html',
                  context = {"departments":Department.objects.all})

def register(request):
    if request.method  == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"NEW ACCOUNT CREATED: {username}")
            login(request,user)
            return redirect("homepage")
        else :
            for msg in form.error_messages:
                print(form.error_messages[msg])
            return render(request, "app1_db/register.html", context={"form":form})

    form = NewUserForm
    return render(request, "app1_db/register.html", context={"form": form})


def logout_request(request):
    logout(request)
    messages.info(request,'logout successfully')
    return redirect("homepage")


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                messages.success(request, f"logged in as: {username}")
                return redirect("homepage")

    form = AuthenticationForm()
    return render(request,"app1_db/login.html",context = {"form":form})

