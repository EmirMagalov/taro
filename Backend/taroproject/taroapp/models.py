from django.db import models

class TaroCard(models.Model):
    img = models.ImageField(upload_to='photo')
    filename = models.CharField(max_length=255,blank=True,null=True)
    name = models.CharField(max_length=255)
    descr_text = models.TextField()
    love_text = models.TextField()
    work_text = models.TextField()
    day_text = models.TextField()
    advice_text = models.TextField()
    yesno_text = models.TextField()

    def __str__(self):
        return self.name
