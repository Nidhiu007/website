from urllib import response
from django.shortcuts import render
import mysql.connector as sql
fn=''
ln=''
s=''
em=''
pwd=''
m=""

# Create your views here.
def signaction(request):
    global fn,ln,s,em,pwd,m
    if request.method=='POST':
      m=sql.connector(host="localhost:3306",user="root",passwd="Pratik@007",database='website')
    
            
    
    c="insert into users values('{}','{}','{}','{}','{}')".format(fn,ln,s,em,pwd)
    m.commit()


    return render(request,'signup_page.html')
    return response