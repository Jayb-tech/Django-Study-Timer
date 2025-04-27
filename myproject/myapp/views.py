from django.shortcuts import render, redirect
from .models import StudySession
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def start_study_timer(request):
    session = StudySession.objects.filter(user=request.user, is_active=True).first()  # Fix: objects.filter instead of objects

    if not session:
        session = StudySession.objects.create(
            user=request.user,
            start_time=timezone.now(),
            is_active=True
        )
    return redirect('study_timer')  # Fix: redirect instead of render

@login_required
def stop_study_timer(request):
    session = StudySession.objects.filter(user=request.user, is_active=True).first()  # Fix: objects.filter instead of objects

    if session:
        session.end_time = timezone.now()
        session.is_active = False
        session.save()

    return redirect('study_timer')

@login_required  # Add login_required here too
def study_timer(request):
    current_session = StudySession.objects.filter(user=request.user, end_time=None).first()
    past_sessions = StudySession.objects.filter(user=request.user, end_time__isnull=False).order_by('-start_time')
    return render(request, 'study_timer.html', {
        'session': current_session,
        'past_sessions': past_sessions
    })

