from . import views
from django.urls import path

urlpatterns=[
    path('',views.index,name = 'index'),
    path('profile/', views.user_profile, name='profile'),
    path('accounts/profile/', views.index,name='profile'),
    path('upload/project/', views.upload_project, name ='upload'),
    path('update_profile/<int:id>',views.update_profile, name='update_profile'),
    path('create_profile/',views.create_profile,name = 'create_profile'),
    path('search/', views.search_results, name='search_results'),
    path('project/<int:project_id>',views.project,name ='project'),
    path('rate/<int:id>',views.rate, name='rate'),
]