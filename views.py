from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings

from .models import Job, Application, Company
from .forms import ApplicationForm


# ===============================
# JOB LIST + SEARCH + FILTER
# ===============================
def job_list(request):

    query = request.GET.get('q')
    location = request.GET.get('location')

    jobs = Job.objects.all()

    if query:
        jobs = jobs.filter(
            Q(title__icontains=query) |
            Q(location__icontains=query)
        )

    if location:
        jobs = jobs.filter(location__icontains=location)

    return render(
        request,
        'jobs/job_list.html',
        {'jobs': jobs}
    )


# ===============================
# JOB DETAIL
# ===============================
def job_detail(request, job_id):

    job = get_object_or_404(Job, id=job_id)

    already_applied = False

    if request.user.is_authenticated:
        already_applied = Application.objects.filter(
            user=request.user,
            job=job
        ).exists()

    return render(
        request,
        'jobs/job_detail.html',
        {
            'job': job,
            'already_applied': already_applied
        }
    )


# ===============================
# POST JOB
# ===============================
@login_required
def post_job(request):

    companies = Company.objects.filter(user=request.user)

    if request.method == "POST":

        Job.objects.create(
            title=request.POST.get('title'),
            company=get_object_or_404(
                Company,
                id=request.POST.get('company')
            ),
            location=request.POST.get('location'),
            description=request.POST.get('description')
        )

        messages.success(request, "Job posted successfully!")

        return redirect('employer_dashboard')

    return render(
        request,
        'jobs/job_post.html',
        {'companies': companies}
    )


# ===============================
# APPLY JOB
# ===============================
@login_required
def apply_job(request, job_id):

    job = get_object_or_404(Job, id=job_id)

    if Application.objects.filter(
        user=request.user,
        job=job
    ).exists():

        messages.warning(
            request,
            "You already applied for this job."
        )

        return redirect('job_detail', job_id=job.id)

    if request.method == "POST":

        form = ApplicationForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            application = form.save(commit=False)
            application.user = request.user
            application.job = job
            application.save()

            messages.success(
                request,
                "Application submitted successfully!"
            )

            return redirect('my_applications')

    else:
        form = ApplicationForm()

    return render(
        request,
        'jobs/apply_job.html',
        {'form': form, 'job': job}
    )


# ===============================
# MY APPLICATIONS
# ===============================
@login_required
def my_applications(request):

    applications = Application.objects.filter(
        user=request.user
    ).select_related('job', 'job__company')

    return render(
        request,
        'jobs/my_applications.html',
        {'applications': applications}
    )


# ===============================
# EMPLOYER DASHBOARD
# ===============================
@login_required
def employer_dashboard(request):

    jobs = Job.objects.filter(
       company = Company.objects.get(user=request.user)
    ).select_related('company')

    return render(
        request,
        'jobs/employer_dashboard.html',
        {'jobs': jobs}
    )


# ===============================
# VIEW APPLICANTS
# ===============================
@login_required
def view_applicants(request, job_id):

    applications = Application.objects.filter(
        job_id=job_id
    ).select_related('user')

    return render(
        request,
        'jobs/view_applicants.html',
        {'applications': applications}
    )


# ===============================
# ACCEPT / REJECT APPLICATION
# ===============================
@login_required
def update_status(request, app_id, status):

    application = get_object_or_404(
        Application,
        id=app_id
    )

    application.status = status
    application.save()

    # EMAIL NOTIFICATION
    subject = "Job Application Status Update"

    message = f"""
Hello {application.user.username},

Your application for "{application.job.title}"
has been {status}.

Thank you for using our Job Portal.
"""

    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [application.user.email],
        fail_silently=False
    )

    messages.success(
        request,
        f"Application {status} successfully!"
    )

    return redirect(request.META.get('HTTP_REFERER'))

from django.db.models import Count

def employer_dashboard(request):
    company = request.user.company

    jobs = Job.objects.filter(company=company).annotate(
        applicant_count=Count('application')
    )

    return render(request, 'jobs/employer_dashboard.html', {
        'jobs': jobs
    })

    from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .models import Job, Profile

def recommended_jobs(request):
    profile = Profile.objects.get(user=request.user)
    user_skills = profile.skills

    jobs = Job.objects.all()

    job_skills = [job.skills_required for job in jobs]

    documents = [user_skills] + job_skills

    tfidf = TfidfVectorizer().fit_transform(documents)

    similarity = cosine_similarity(tfidf[0:1], tfidf[1:]).flatten()

    job_scores = list(zip(jobs, similarity))

    job_scores.sort(key=lambda x: x[1], reverse=True)

    recommended = [job for job, score in job_scores if score > 0][:5]

    return render(request, "jobs/recommended_jobs.html", {
        "jobs": recommended
    })