from flask import redirect,render_template,request
import pymysql

conn = pymysql.connect(host="localhost" , user='root' , password='' , database='cms')



def staff_add(req):
    first_name=req.form.get("first_name")
    last_name=req.form.get("last_name")
    father_name=req.form.get("father_name")
    mother_name=req.form.get("mother_name")
    dob=req.form.get("dob")
    address=req.form.get("address")
    qualification=req.form.get("qualification")
    timing=req.form.get("timing")
    # course=req.form.get("course")
    date_of_joining=req.form.get("date_of_joining")
    
    with conn.cursor() as cur:
        sql="""INSERT INTO staff(first_name,last_name,father_name,mother_name,dob,address,qualification,timing,date_of_joining)Values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        values=(first_name,last_name,father_name,mother_name,dob,address,qualification,timing,date_of_joining)
        cur.execute(sql,values)
        conn.commit()

    return 1