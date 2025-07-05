from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()


    RATING_CHOICE = [
        ('1', 'Very Bad'),
        ('2', 'Bad'),
        ('3', 'Average'),
        ('4', 'Good'),
        ('5', 'Excellent',)
    ]
    rating = models.CharField(max_length=1, choices=RATING_CHOICE, default='3' )
   

    def __str__(self):
        return f"{self.name} ({self.email})"
