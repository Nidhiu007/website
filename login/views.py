from sqlite3 import Cursor
from urllib import request, response
from django.shortcuts import render
import mysql.connector as sql
from django.shortcuts import redirect, render

em=''
pwd=''
m=''

# Create your views here.
def loginaction(request):
    global em,pwd,m
    if request.method=="POST":
        m=sql.connector(host="localhost",user="root",password="Pratik@007",database="web")

        c="select * from users where email '{}' and password '{}'".format(em,pwd)
         
    

    
        return (request,'login_page.html')