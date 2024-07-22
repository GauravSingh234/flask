from flask import redirect,render_template,request
import pymysql

conn = pymysql.connect(host="localhost" , user='root' , password='' , database='cms')



def students_add(req):
    # student_id=request.form.get("student_id")
    first_name=req.form.get("first_name")
    last_name=req.form.get("last_name")
    father_name=req.form.get("father_name")
    mother_name=req.form.get("mother_name")
    dob=req.form.get("dob")
    address=req.form.get("address")
    course=req.form.get("course")
    mobile=req.form.get("mobile")
    email=req.form.get("email")
    photo=req.form.get("photo")
    print(photo)   

    with conn.cursor() as cur:
        sql="""INSERT INTO students(first_name,last_name,father_name,mother_name,dob,address,courses,mobile,email,photo)Values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        values=(first_name,last_name,father_name,mother_name,dob,address,course,mobile,email,photo)
        cur.execute(sql,values)
        name=cur.fetchall()
        conn.commit()
        
    return 1