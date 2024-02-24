from django.db import models

class Volunteer(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    year_choices = [
        ('FE', 'First Year'),
        ('SE', 'Second Year'),
        ('TE', 'Third Year'),
        ('BE', 'Fourth Year'),
    ]
    year = models.CharField(max_length=2, choices=year_choices)
    branch_choices = [
        ('Computer', 'Computer Engineering'),
        ('AIDS', 'Artificial Intelligence and Data Science'),
        ('CDS', 'Computer (DS)'),
    ]
    branch = models.CharField(max_length=50, choices=branch_choices)
    skills = models.CharField(max_length=255)
    event_choices = [
        ('Website Design Portfolio Showcase', 'Website Design Portfolio Showcase'),
        ('Poster Competition', 'Poster Competition'),
        ('Coding Challange', 'Coding Challenge'),
        ('Tech Trivia Showdown (Tech-Quiz)', 'Tech Trivia Showdown (Tech-Quiz)'),
        ('Tech-Debate', 'Tech-Debate'),
        ('Treasure Hunt/CTF', 'Treasure Hunt/CTF'),
        ('Project Competition', 'Project Competition'),
        ('Esports Tournament', 'Esports Tournament'),
    ]
    event = models.CharField(max_length=100, choices=event_choices)
    registration_for_choices = [
        ('Club Member', 'Club Member'),
        ('Event Volunteer', 'Event Volunteer'),
    ]
    registration_for = models.CharField(max_length=50, choices=registration_for_choices)
    reason = models.TextField()
