from django.db import models

class Contacts(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    colorCode = models.CharField(max_length=7, default='#FFFFFF')  
    textColorCode = models.CharField(max_length=7, default='#000000')  
    selected = models.BooleanField(default=False)
    initials = models.CharField(max_length=2, default='')

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, choices=[
        ('User Story', 'User Story'),
        ('Testing', 'Testing'),
        ('Research', 'Research'),
        ('Other', 'Other'),
        ('Technical Task', 'Technical Task'),
        ('Infrastructure', 'Infrastructure'),
        ('Enhancement', 'Enhancement'),
        ('Feature Request', 'Feature Request'),
        ('Bug', 'Bug'),
        ('Documentation', 'Documentation'),
        ('Design', 'Design'),
    ])
    
    def __str__(self):
        return self.name
    
class Tasks(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    board = models.CharField(max_length=50, choices=[('toDo', 'To Do'), 
                                                     ('inProgress', 'In Progress'),
                                                     ('awaitFeedback', 'Await Feedback'),
                                                     ('done', 'Done')], default='toDo')

    priority = models.CharField(max_length=20, choices=[('urgent', 'Urgent'), 
                                                        ('medium', 'Medium'), 
                                                        ('low', 'Low')])
    assigned_to = models.ManyToManyField(Contacts, related_name='tasks')
    subtasks = models.JSONField(default=dict, blank=True, null=False) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_assigned_users(self):
        return ", ".join([contact.name for contact in self.assigned_to.all()])
    
    def get_subtasks(self):
        return {
        "items": self.subtasks.get("items", []),
        "completed": self.subtasks.get("completed", [])
    }
    
class Subtask(models.Model):
    task = models.ForeignKey(Tasks, related_name='subtask_list', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    done = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Subtask: {self.description}"