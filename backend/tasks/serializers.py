from rest_framework import serializers
from .models import Users, Task, Project
from datetime import datetime

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'nom', 'prenom', 'username', 'email', 'password']

    def validate_email(self, value):
        # Vérifie si l'email est unique
        if Users.objects.filter(email=value).exists():
            raise serializers.ValidationError("Cet email est déjà utilisé.")
        return value


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'titre', 'description', 'date_debut', 'date_fin', 'users']

    def validate(self, data):
        # Ajoutez ici la logique de validation personnalisée
        return data

    def validate_date_fin(self, value):
        # Vérifie si la date de fin est postérieure à la date de début
        if 'date_debut' in self.initial_data:
            date_debut_str = self.initial_data['date_debut']
            date_debut = datetime.strptime(date_debut_str, '%Y-%m-%d').date()
            if value <= date_debut:
                raise serializers.ValidationError("La date de fin doit être postérieure à la date de début.")
        return value
