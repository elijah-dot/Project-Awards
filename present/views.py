from django.shortcuts import render,redirect
from .models import Profile,Project,Rating
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import PostProjectForm,UpdateProfileForm,ProfileForm,RateProjectForm
from django.http import HttpResponseRedirect
from .email import send_welcome_email






# Create your views here.
def index(request):
    project = Project.objects.all().order_by('-id')
    
    return render(request,'index.html',{'project':project})

def email(request):
    current_user = request.user
    email = current_user.email
    name = current_user.username
    send_welcome_email(name, email)
    return redirect(create_profile)

@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    title = "Create Profile"
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:
        form = ProfileForm()
    return render(request, 'profile/create_profile.html', {"form": form, "title": title})
    
@login_required(login_url='/accounts/login/')
def user_profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    project = Project.objects.filter(user_id=current_user.id)

    return render(request,"index.html",{'profile':profile,'project':project})

@login_required(login_url='/accounts/login/')
def user_profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    project = Project.objects.filter(user_id=current_user.id)

    return render(request,"profile/profile.html",{'profile':profile,'project':project})

@login_required(login_url='/accounts/login/')
def upload_project(request):
    if request.method == "POST":
        form = PostProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
        return redirect('/')
    else:
        form = PostProjectForm()
    return render(request, 'project/post_project.html', {"form": form})

def update_profile(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user = user)
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
            form = UpdateProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():  
                
                profile = form.save(commit=False)
                profile.save()
                return redirect('profile') 
            
    return render(request, 'profile/update_profile.html', {"form":form})

@login_required(login_url='/accounts/login/')
def search_results(request):

    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search").lower()
        projects = Project.search_by_project_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"success":message,"projects":projects})

    else:
        message = "You haven't searched for any item!"
        return render(request, 'search.html',{'warning':message})

@login_required(login_url='/accounts/login/')
def project(request,project_id):
    project = Project.objects.get(id = project_id)
    rating = Rating.objects.filter(project = project)
    return render(request,"project/project.html", {"project":project,"rating":rating})

@login_required(login_url='/accounts/login/')
def rate(request,id):
    if request.method == 'POST':
        project = Project.objects.get(id = id)
        current_user = request.user
        design_rate = request.POST['design']
        content_rate = request.POST['content']
        usability_rate = request.POST['usability']

        Rating.objects.create(
            project=project,
            user=current_user,
            design_rate=design_rate,
            usability_rate=usability_rate,
            content_rate=content_rate,
            average=round((float(design_rate)+float(usability_rate)+float(content_rate))/3,2))

        return render(request,"project/project.html",{"project":project})
    else:
        project = Project.objects.get(id = id) 
        return render(request,"project/project.html",{"project":project})