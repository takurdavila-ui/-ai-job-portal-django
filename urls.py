from django.urls import path
from . import views

urlpatterns = [

    # ======================
    # JOB LIST
    # ======================
    path('', views.job_list, name='job_list'),

    # ======================
    # JOB DETAIL
    # ======================
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),

    # ======================
    # APPLY JOB
    # ======================
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),

    # ======================
    # MY APPLICATIONS
    # ======================
    path('my-applications/', views.my_applications,
         name='my_applications'),

    # ======================
    # POST JOB
    # ======================
    path('post-job/', views.post_job, name='post_job'),

    # ======================
    # EMPLOYER DASHBOARD
    # ======================
    path('employer/dashboard/',
         views.employer_dashboard,
         name='employer_dashboard'),

    # ======================
    # VIEW APPLICANTS
    # ======================
    path('job/<int:job_id>/applicants/',
         views.view_applicants,
         name='view_applicants'),

    # ======================
    # ACCEPT / REJECT
    # ======================
    path('application/<int:app_id>/<str:status>/',
         views.update_status,
         name='update_status'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),
    path('post-job/', views.post_job, name='post_job'),
    path('my-applications/', views.my_applications, name='my_applications'),

    # EMPLOYER
    path('employer/dashboard/', views.employer_dashboard,
         name='employer_dashboard'),

    path('job/<int:job_id>/applicants/',
         views.view_applicants,
         name='view_applicants'),

    path('application/<int:app_id>/<str:status>/',
         views.update_status,
         name='update_status'),
]
path(
    'apply/<int:job_id>/',
    views.apply_job,
    name='apply_job'
),

from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('jobs/', views.job_list, name='job_list'),

    path('jobs/<int:job_id>/', views.job_detail, name='job_detail'),

    path('post-job/', views.post_job, name='post_job'),

    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),

    path('my-applications/', views.my_applications, name='my_applications'),

    path('employer-dashboard/', views.employer_dashboard, name='employer_dashboard'),

    path('view-applicants/<int:job_id>/', views.view_applicants, name='view_applicants'),

    path('update-status/<int:app_id>/<str:status>/', views.update_status, name='update_status'),
    path('recommended-jobs/', views.recommended_jobs, name='recommended_jobs'),]