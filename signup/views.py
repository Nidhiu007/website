from django.shortcuts import render
#?import mysql.connector as sql
fn=''
ln=''
s=''
em=''
pwd=''

# Create your views here.
def signaction(request):
    global fn,ln,s,em,pwd
    if request.method=='POST':
      m=sql.connector(host="localhost:3306",user="root",passwd="Pratik@007",database='website')
    cursor=m.cursor()
    d=request.Post
    for key,value in d.items():
        if key=="fitst_name":
            fn==value
        if key=="last_name":
            ln==value
        if key=="sex":
            s==value
        if key=="email":
            em==value
        if key=="password":
            pwd==value
    
    c="insert into users values('{}','{}','{}','{}','{}')".format(fn,ln,s,em,pwd)
    cursor.execute(c)
    m.commit()


    return render(request,'signup_page.html')