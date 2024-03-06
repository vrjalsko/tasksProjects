# Generated by Django 4.1.13 on 2024-03-04 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(blank=True, max_length=160, unique=True)),
                ('description', models.TextField(blank=True, max_length=255, unique=True)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=160, unique=True)),
                ('prenom', models.CharField(blank=True, max_length=160, unique=True)),
                ('username', models.CharField(blank=True, max_length=160, unique=True)),
                ('email', models.EmailField(blank=True, max_length=160, unique=True)),
                ('password', models.CharField(blank=True, max_length=160, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(blank=True, max_length=160, unique=True)),
                ('description', models.TextField(blank=True, max_length=255, unique=True)),
                ('date_creation', models.DateField()),
                ('status', models.BooleanField(default=False)),
                ('assignedTo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_tasks', to='tasks.users')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='tasks.project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='tasks.users'),
        ),
    ]
