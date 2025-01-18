from django.db import models
from django.contrib.auth.models import AbstractUser

# Our authentication model
class UserProfile(AbstractUser):
    pass

class Todo(models.Model):
    title = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # user = UserProfile.objects.get(id=1)
    # user_todos = user.todos.all()  
    # Returns a QuerySet of all Todo objects for this user
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='todos'
      )

    def __str__(self):
        # Return title instead of object id
        return self.title
