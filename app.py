from flask import Flask,redirect,url_for,render_template,request
import pymysql
from function.guardian import guardian_add
from function.attendance import attendance_add
from function.teachers import teachers_add
from function.students import students_add
from function.staff import staff_add
from function.enquiry import enquiry_add
from function.course import course_add



conn = pymysql.connect(host="localhost" , user='root' , password='' , database='cms')


app=Flask(__name__)


@app.route("/")
def index():
    return render_template("base.html")


@app.route('/attendance1')
def attendanceform():  
    return render_template("attendance.html" )

@app.route("/attendance2")
def attendance2():
    with conn.cursor() as cur:
        sql="select * from attendance"
        cur.execute(sql)
        data = cur.fetchall()
    return render_template("attendancetable.html", datas=data)

@app.route("/delete/<id>")
def attendance3(id):  
    with conn.cursor() as cur:
        sql="delete from attendance where attendance_id=%s"
        values=(id)
        cur.execute(sql,values)
        conn.commit()
        return redirect("/attendance2")


@app.route('/course1')
def courseform():
    return render_template("course.html")

@app.route("/course2")
def course2():
    with conn.cursor() as cur:
        sql="select * from courses"
        cur.execute(sql)
        data = cur.fetchall()
    return render_template("coursetable.html", datas=data)


@app.route("/course3/<id>")
def course3(id):  
    with conn.cursor() as cur:
        sql="delete from courses where id=%s"
        values=(id)
        cur.execute(sql,values)
    return redirect("/course2")


@app.route('/enquiry1')
def enquiryform():
    return render_template("enquiry.html")

@app.route("/enquiry2")
def enquiry2():
    with conn.cursor() as cur:
        sql="select * from enquiry_forms"
        cur.execute(sql)
        data = cur.fetchall()
    return render_template("enquirytable.html", datas=data)


@app.route("/delete/<id>")
def enquiry3(id):  
    with conn.cursor() as cur:
        sql="delete from enquiry_forms where id=%s"
        values=(id)
        cur.execute(sql,values)
        return redirect("/enquiry2")


@app.route('/guardian1')
def guardianform():
    return render_template("guardian.html")

@app.route("/guardian2")
def guardian2():
    with conn.cursor() as cur:
        sql="select * from guardians"
        cur.execute(sql)
        data = cur.fetchall()
    return render_template("guardiantable.html", datas=data)

@app.route("/delete/<id>")
def guardian3(id):  
    with conn.cursor() as cur:
        sql="delete from guardians where id=%s"
        values=(id)
        cur.execute(sql,values)
        return redirect("/guardian2")


@app.route('/staff1')
def staffform():
    return render_template("staff.html")

@app.route("/staff2")
def staff2():
    with conn.cursor() as cur:
        sql="select * from staff"
        cur.execute(sql)
        data = cur.fetchall()
    return render_template("stafftable.html", datas=data)

@app.route("/delete/<id>")
def staff3(id):  
    with conn.cursor() as cur:
        sql="delete from staff where id=%s"
        values=(id)
        cur.execute(sql,values)
        return redirect("/staff2")


@app.route('/student1')
def studentform():
    return render_template("students.html")

@app.route("/student2")
def student2():
    with conn.cursor() as cur:
        sql="select * from students"
        cur.execute(sql)
        data = cur.fetchall()
    return render_template("studentstable.html", datas=data)

@app.route("/delete/<id>")
def student3(id):
   
    with conn.cursor() as cur:
        sql="delete from students where id=%s"
        values=(id)
        cur.execute(sql,values)
        return redirect("/student2")


@app.route('/teacher1')
def teachersform():
    return render_template("teachers.html")

@app.route("/teacher2")
def teacher2():
    with conn.cursor() as cur:
        sql="select * from teachers"
        cur.execute(sql)
        data = cur.fetchall()
    return render_template("teacherstable.html", datas=data)

@app.route("/delete/<id>")
def teacher3(id):  
    with conn.cursor() as cur:
        sql="delete from teachers where id=%s"
        values=(id)
        cur.execute(sql,values)
        return redirect("/teacher2")

@app.route('/attendance', methods=["POST"])
def attendance():
    status= attendance_add(request)
    if status==1:
        return redirect("/attendance2") 
    else:
        return "ID Does Not Exist."
    
    
@app.route('/course', methods=["POST"])
def course():
    status= course_add(request)
    if status==1:
        return redirect("/course2")
    else:
        return "Error"


@app.route('/enquiry', methods=["POST"])
def enquiry():
      
    status= enquiry_add(request)
    if status==1:
        return redirect("/enquiry2")
    else:
        return "Error"
  

@app.route('/guardian', methods=["POST"])
def guardian():
    # guardian_id=request.form.get("guardian_id")
    status= guardian_add(request)
    if status==1:
        return redirect("/guardian2") 
    else:
        return "ID does not Exist"
    

@app.route('/staff', methods=["POST"])
def staff():
  
    status= staff_add(request)
    if status==1:
        return redirect("/staff2")
    else:
        return "Error"
    

@app.route('/student', methods=["POST"])
def student():
    
    status= students_add(request)
    if status==1:
        return redirect("/student2")
    else:
        return "Error"

@app.route('/teachers', methods=["POST"])
def teachers():
    
    status= teachers_add(request)
    if status==1:
        return redirect("/teacher2")
    else:
        return "Error"

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)