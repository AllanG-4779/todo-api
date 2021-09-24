from django.db import models

# Create your models here.
class Item(models.Model):
    task_name = models.CharField(verbose_name="Task Name", max_length=50)
    completed = models.BooleanField( default=False )
    added = models.DateTimeField( auto_now=False, auto_now_add=True)
    completed_at= models.DateTimeField(auto_now=True, auto_now_add=False)

    

    def __str__(self):
        status = ""
        if self.completed:
            status = "Completed"
        else:
            status = "not Completed"

        return f'Task "{self.task_name}" was added at {self.added} and is {status} '

    


    