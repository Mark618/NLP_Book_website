from operator import index
from traceback import StackSummary
from django.db import models

# Create your models here.

class Book(models.Model):
    index_num=models.AutoField(primary_key=True)
    book_id = models.IntegerField()
    freebase_id = models.CharField(max_length=200)
    book_title=models.CharField(max_length=200,null=True)
    author=models.CharField(max_length=200,null=True)
    pub_date=models.CharField(max_length=200,null=True)
    book_genre=models.CharField(max_length=200,null=True)    
    summary = models.TextField()
    url=models.URLField(null=True)
    pub_year = models.IntegerField()
    
    
    def __str__(self):
        return self.book_title 