from flask import redirect,render_template,request
import pymysql

conn = pymysql.connect(host="localhost" , user='root' , password='' , database='cms')



def course_add(req):
    # course_id=req.form.get("courseId")
    name=req.form.get("name")
    duration=req.form.get("duration")
    fees=req.form.get("fee")  
    print(fees)

    with conn.cursor() as cur:
        sql="""INSERT INTO courses(name,duration,fees)Values(%s,%s,%s)"""
        Values=(name,duration,fees)
        cur.execute(sql,Values)
        conn.commit()

    return 1