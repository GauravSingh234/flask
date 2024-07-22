from flask import redirect,render_template,request
import pymysql

conn = pymysql.connect(host="localhost" , user='root' , password='' , database='cms')



def teachers_add(req):
    first_name=req.form.get("name")
    last_name=req.form.get("name")
    father_name=req.form.get("father_name")
    mother_name=req.form.get("mother_name")
    dob=req.form.get("dob")
    address=req.form.get("address")
    salary=req.form.get("salary")
    qualification=req.form.get("qualification")
    timing=req.form.get("timing")
    course=req.form.get("course")
    date_of_joining=req.form.get("date_of_joining")
    print(course) 

    with conn.cursor() as cur:
        sql="""INSERT INTO teachers(first_name,last_name,father_name,mother_name,dob,address,salary,qualification,timing,course,date_of_joining)Values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        values=(first_name,last_name,father_name,mother_name,dob,address,salary,qualification,timing,course,date_of_joining)
        cur.execute(sql,values)
        conn.commit()

        
    return 1

    
