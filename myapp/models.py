from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class StudySession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)  # Add this line
    
    def session_duration(self):
        if self.end_time:
            duration = self.end_time - self.start_time
            # Convert to total seconds
            total_seconds = int(duration.total_seconds())
            
            # Calculate hours, minutes, and seconds
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            seconds = total_seconds % 60
            
            # Format the time parts
            if hours > 0:
                return f"{hours}h {minutes}m {seconds}s"
            elif minutes > 0:
                return f"{minutes}m {seconds}s"
            else:
                return f"{seconds}s"
        return None
    
    def __str__(self):
        return f"{self.user.username}'s session on {self.start_time.strftime('%Y-%m-%d %H:%M')}"