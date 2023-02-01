from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import random
from main.management.commands import nlp_func, nlp_recommen 
from .models import Book
from .apps import MainConfig
from django.views.generic import ListView
import json
  

# library use
import pandas as pd
import numpy as np 
# Create your views here.



def homepage(request):
    book = list(Book.objects.exclude(url__isnull=True))

    book = random.sample(book, 16)
    
    return render(request=request,
                  template_name="main/home.html",                  
                  context={"book":book})
    
def book(request,book_id):
    book = Book.objects.get(book_id=book_id)
    book_sum=book.summary
    
    whatis =nlp_recommen.recommend(book.book_title)
    recom_book = Book.objects.filter(book_id__in=whatis)                
    if request.method == 'POST':      
        valuee = request.POST.get("sli")
        sum_result=nlp_func.summarize(book_sum,float(valuee))
        return JsonResponse({"summary":sum_result})
    else:
        return render(request=request,template_name="main/book.html",context={"book":book,"recomm":recom_book})
    

def compare(request):
    book = list(Book.objects.exclude(url__isnull=True))
    # book = list(Book.objects.values('book_title'))
    if request.method =='POST':
        value1=request.POST.get("left_book")   
        value2=request.POST.get("right_book")
        sim_val=MainConfig.sim_model.dv.similarity(int(value1)-1,int(value2)-1)
        print(sim_val)
        return JsonResponse({"sim_value":round(float(sim_val),2)})
    else:  
        return render(request=request,
                  template_name="main/compare.html",                  
                  context={'book':book})
    


    
    
    
