from flask import redirect,render_template,request
import pymysql

conn = pymysql.connect(host="localhost" , user='root' , password='' , database='cms')



def enquiry_add(req):
    # form_id=req.form.get("formId")
    student_name=req.form.get("name")
    father_name=req.form.get("father_name")
    mother_name=req.form.get("mother_name")
    dob=req.form.get("dob")
    address=req.form.get("address")
    mobile=req.form.get("mobile")
    email=req.form.get("email")
    course=req.form.get("course")
    # date=req.form.get("date")
    

    with conn.cursor() as cur:
        sql="""INSERT INTO enquiry_forms(student_name,father_name,mother_name,dob,address,mobile,email,course)Values(%s,%s,%s,%s,%s,%s,%s,%s)"""
        Values=(student_name,father_name,mother_name,dob,address,mobile,email,course)
        cur.execute(sql,Values)
        conn.commit()

        
    return 1