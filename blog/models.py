from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def date_short(self):
        return self.pub_date.strftime('%b %Y')

    def summary(self):
        summary = self.body[:300]
        summary = summary[:summary.rfind(' ')]
        return summary

