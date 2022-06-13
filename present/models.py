from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE



# Create your models here.
class Profile(models.Model):
    prof_photo = CloudinaryField('image',null=True)
    bio = models.TextField(max_length=1000, blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def update_profile(self):
        self.save()

    @classmethod
    def get_profile_by_user(cls, user):
        profile = cls.objects.filter(user=user)
        return profile


class Project(models.Model):
    image = CloudinaryField('image')
    project_name = models.CharField(max_length=50)
    description = models.TextField(max_length=2000)
    category = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    url = models.URLField(max_length=60,null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)
    average_score = models.FloatField(default=0)

    # rating = models.ForeignKey(Rating,null=True,on_delete=CASCADE)
    #avg_rating

    def __str__(self):
        return self.project_name

    @classmethod
    def get_all_projects(cls):
        projects = Project.objects.all()
        return projects

    @classmethod
    def search_by_project_name(cls,search_term):
        projects = cls.objects.filter(project_name__icontains=search_term)
        return projects

    @classmethod
    def display_all_projects(cls):
        return cls.objects.all()

    def save_project(self):
        self.save()

    def update_project(self,project_name,description,category):
        self.project_name = project_name,
        self.description = description,
        self.category = category
        self.save()


    class Meta:
        ordering = ['-pub_date']

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,null=True)
    design_rate = models.IntegerField(default=0, blank=True, null=True)
    usability_rate = models.IntegerField(default=0, blank=True, null=True)
    content_rate = models.IntegerField(default=0, blank=True, null=True)
    average = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def save_rate(self):
        self.save()

    def delete_rate(self):
        self.delete()

    @classmethod
    def get_project_rates(cls):
        return cls.objects.get_or_create()