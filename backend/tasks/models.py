from django.db import models

class Users(models.Model):
    nom = models.CharField(max_length=160, blank=True, unique=True)
    prenom = models.CharField(max_length=160, blank=True, unique=True)
    username = models.CharField(max_length=160, blank=True, unique=True)
    email = models.EmailField(max_length=160, blank=True, unique=True)
    password = models.CharField(max_length=160, blank=True, unique=True)

    def __str__(self):
        return f"{self.nom}, {self.prenom}, {self.username}"

class Task(models.Model):
    titre = models.CharField(max_length=160, blank=True, unique=True)
    description = models.TextField(max_length=255, blank=True, unique=True)
    date_creation = models.DateField()
    status = models.BooleanField(default=False)
    assignedTo = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='assigned_tasks')
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return f"{self.titre}"
        
class Project(models.Model):
    titre = models.CharField(max_length=160, blank=True, unique=True)
    description = models.TextField(max_length=255, blank=True, unique=True)
    date_debut = models.DateField()
    date_fin = models.DateField()
    users = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='projects')
    # Supprimez task = models.ForeignKey('Task', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titre}"
