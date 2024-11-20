from flask import Flask, request, jsonify, render_template, url_for, redirect, session, flash
import mysql
import MySQLdb
import mysql.connector as mc 
import Search, enrollment, drop
from init import fetchStudentData, fetchCourseData, fetchCourseSession, fetchEnrolledTable, fetchCourseSession
import sys

app = Flask(__name__)
app.secret_key = b'5aBMRhcy'


db = mc.connect(host="localhost", port=3306, user="admint", password="12341234", database="mid")
cursor = db.cursor()
print("Connected to database")

username = ""
password = ""

def loadPrereq(db):
    cur = db.cursor()
    cur.execute("SELECT S_ID FROM Student")
    result = cur.fetchall()
    for i in result:
        S_ID = i[0]
        cur.execute("SELECT * FROM Student WHERE S_ID='%s';" % (S_ID))
        result = cur.fetchone()

        grade = result[5]
        classNum = result[6]
        print(grade, classNum)

        prereqlist = []
        cur.execute("SELECT Course_ID FROM Courses WHERE Grade=%s AND Class=%s AND Prereq=1;", (grade, classNum))
        result = cur.fetchall()
        for i in result:
            prereqlist.append(i[0])

        for prereq in prereqlist:
            cur.execute("SELECT Course_Credit FROM Courses WHERE Course_ID=%s;", (prereq,))
            result = cur.fetchone()
            course_credit = result[0]
            cur.execute("SELECT Ttl_Credit FROM Student WHERE S_ID='%s';" % (S_ID))
            result = cur.fetchone()
            student_credit = result[0]
            student_credit += course_credit
            cur.execute("UPDATE Student SET Ttl_Credit=%s WHERE S_ID='%s';" % (student_credit, S_ID))
            cur.execute("SELECT Session_Time FROM Course_Session WHERE Course_ID=%s;" % (prereq,))
            results = cur.fetchall()
            for result in results:
                time = result[0]

                cur.execute("UPDATE Enrolled_Table SET S%s=%s WHERE S_ID='%s' AND S%s=0;" % (time, prereq, S_ID, time))
                db.commit()

# login 
@app.route('/')
def index():
    loadPrereq(db)
    if 'username' in session:
        print("session exists")
        enrolledtable = fetchEnrolledTable(session['username'], db)
        render_template('dashboard.html', usernameKept=session['username'],
                        s1=enrolledtable.S1, s2=enrolledtable.S2, s3=enrolledtable.S3, s4=enrolledtable.S4, s5=enrolledtable.S5,
                        s6=enrolledtable.S6, s7=enrolledtable.S7, s8=enrolledtable.S8, s9=enrolledtable.S9, s10=enrolledtable.S10,
                        s11=enrolledtable.S11, s12=enrolledtable.S12, s13=enrolledtable.S13, s14=enrolledtable.S14, s15=enrolledtable.S15,
                        s16=enrolledtable.S16, s17=enrolledtable.S17, s18=enrolledtable.S18, s19=enrolledtable.S19, s20=enrolledtable.S20,
                        s21=enrolledtable.S21, s22=enrolledtable.S22, s23=enrolledtable.S23, s24=enrolledtable.S24, s25=enrolledtable.S25,
                        s26=enrolledtable.S26, s27=enrolledtable.S27, s28=enrolledtable.S28, s29=enrolledtable.S29, s30=enrolledtable.S30,
                        s31=enrolledtable.S31, s32=enrolledtable.S32, s33=enrolledtable.S33, s34=enrolledtable.S34, s35=enrolledtable.S35,
                        s36=enrolledtable.S36, s37=enrolledtable.S37, s38=enrolledtable.S38, s39=enrolledtable.S39, s40=enrolledtable.S40,
                        s41=enrolledtable.S41, s42=enrolledtable.S42, s43=enrolledtable.S43, s44=enrolledtable.S44, s45=enrolledtable.S45,
                        s46=enrolledtable.S46, s47=enrolledtable.S47, s48=enrolledtable.S48, s49=enrolledtable.S49, s50=enrolledtable.S50,
                        s51=enrolledtable.S51, s52=enrolledtable.S52, s53=enrolledtable.S53, s54=enrolledtable.S54, s55=enrolledtable.S55,
                        s56=enrolledtable.S56, s57=enrolledtable.S57, s58=enrolledtable.S58, s59=enrolledtable.S59, s60=enrolledtable.S60,
                        s61=enrolledtable.S61, s62=enrolledtable.S62, s63=enrolledtable.S63, s64=enrolledtable.S64, s65=enrolledtable.S65,
                        s66=enrolledtable.S66, s67=enrolledtable.S67, s68=enrolledtable.S68, s69=enrolledtable.S69, s70=enrolledtable.S70)
        return redirect(url_for('dashboard'))
    else:
        print("session not exists")
        return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if(Search.searchUser(db, username, password)):
        S_ID = student_data[0]
        session['username'] = username
        enrolledtable = fetchEnrolledTable(session['username'], db)
        render_template('dashboard.html', usernameKept=session['username'],
                        s1=enrolledtable.S1, s2=enrolledtable.S2, s3=enrolledtable.S3, s4=enrolledtable.S4, s5=enrolledtable.S5,
                        s6=enrolledtable.S6, s7=enrolledtable.S7, s8=enrolledtable.S8, s9=enrolledtable.S9, s10=enrolledtable.S10,
                        s11=enrolledtable.S11, s12=enrolledtable.S12, s13=enrolledtable.S13, s14=enrolledtable.S14, s15=enrolledtable.S15,
                        s16=enrolledtable.S16, s17=enrolledtable.S17, s18=enrolledtable.S18, s19=enrolledtable.S19, s20=enrolledtable.S20,
                        s21=enrolledtable.S21, s22=enrolledtable.S22, s23=enrolledtable.S23, s24=enrolledtable.S24, s25=enrolledtable.S25,
                        s26=enrolledtable.S26, s27=enrolledtable.S27, s28=enrolledtable.S28, s29=enrolledtable.S29, s30=enrolledtable.S30,
                        s31=enrolledtable.S31, s32=enrolledtable.S32, s33=enrolledtable.S33, s34=enrolledtable.S34, s35=enrolledtable.S35,
                        s36=enrolledtable.S36, s37=enrolledtable.S37, s38=enrolledtable.S38, s39=enrolledtable.S39, s40=enrolledtable.S40,
                        s41=enrolledtable.S41, s42=enrolledtable.S42, s43=enrolledtable.S43, s44=enrolledtable.S44, s45=enrolledtable.S45,
                        s46=enrolledtable.S46, s47=enrolledtable.S47, s48=enrolledtable.S48, s49=enrolledtable.S49, s50=enrolledtable.S50,
                        s51=enrolledtable.S51, s52=enrolledtable.S52, s53=enrolledtable.S53, s54=enrolledtable.S54, s55=enrolledtable.S55,
                        s56=enrolledtable.S56, s57=enrolledtable.S57, s58=enrolledtable.S58, s59=enrolledtable.S59, s60=enrolledtable.S60,
                        s61=enrolledtable.S61, s62=enrolledtable.S62, s63=enrolledtable.S63, s64=enrolledtable.S64, s65=enrolledtable.S65,
                        s66=enrolledtable.S66, s67=enrolledtable.S67, s68=enrolledtable.S68, s69=enrolledtable.S69, s70=enrolledtable.S70)

        return redirect(url_for('dashboard'))
    else:
        flash('Invalid username or password')
        render_template('index.html')
        return redirect(url_for('index'))

# dashboard 
@app.route('/dashboard')
def dashboard():
    print(username)
    enrolledtable = fetchEnrolledTable(session['username'], db)
    return render_template('dashboard.html', usernameKept=session['username'],
                           s1=enrolledtable.S1, s2=enrolledtable.S2, s3=enrolledtable.S3, s4=enrolledtable.S4, s5=enrolledtable.S5,
                           s6=enrolledtable.S6, s7=enrolledtable.S7, s8=enrolledtable.S8, s9=enrolledtable.S9, s10=enrolledtable.S10,
                           s11=enrolledtable.S11, s12=enrolledtable.S12, s13=enrolledtable.S13, s14=enrolledtable.S14, s15=enrolledtable.S15,
                           s16=enrolledtable.S16, s17=enrolledtable.S17, s18=enrolledtable.S18, s19=enrolledtable.S19, s20=enrolledtable.S20,
                           s21=enrolledtable.S21, s22=enrolledtable.S22, s23=enrolledtable.S23, s24=enrolledtable.S24, s25=enrolledtable.S25,
                           s26=enrolledtable.S26, s27=enrolledtable.S27, s28=enrolledtable.S28, s29=enrolledtable.S29, s30=enrolledtable.S30,
                           s31=enrolledtable.S31, s32=enrolledtable.S32, s33=enrolledtable.S33, s34=enrolledtable.S34, s35=enrolledtable.S35,
                           s36=enrolledtable.S36, s37=enrolledtable.S37, s38=enrolledtable.S38, s39=enrolledtable.S39, s40=enrolledtable.S40,
                           s41=enrolledtable.S41, s42=enrolledtable.S42, s43=enrolledtable.S43, s44=enrolledtable.S44, s45=enrolledtable.S45,
                           s46=enrolledtable.S46, s47=enrolledtable.S47, s48=enrolledtable.S48, s49=enrolledtable.S49, s50=enrolledtable.S50,
                           s51=enrolledtable.S51, s52=enrolledtable.S52, s53=enrolledtable.S53, s54=enrolledtable.S54, s55=enrolledtable.S55,
                           s56=enrolledtable.S56, s57=enrolledtable.S57, s58=enrolledtable.S58, s59=enrolledtable.S59, s60=enrolledtable.S60,
                           s61=enrolledtable.S61, s62=enrolledtable.S62, s63=enrolledtable.S63, s64=enrolledtable.S64, s65=enrolledtable.S65,
                           s66=enrolledtable.S66, s67=enrolledtable.S67, s68=enrolledtable.S68, s69=enrolledtable.S69, s70=enrolledtable.S70)

@app.route('/handle_course', methods=['POST'])
def handle_course():
    course_id = request.form['course_id']
    S_ID = session.get('username') 
    print("course_id: ", course_id)
    if(fetchCourseData(course_id, db)):
        print("course found")
        # check if the course is already enrolled -> drop
        if Enrollment.checkEnrolled(S_ID, course_id, db):
            print("course not enrolled")
            Enrollment.enrollCourse(S_ID, course_id, db)
            print("course enrolled")
        # check if the course is not enrolled -> enroll
        else:
            print("course already enrolled")
            Drop.dropCourse(S_ID, course_id, db)
            print("course dropped")

    else:
        print('找不到課程')

    enrolledtable = fetchEnrolledTable(session['username'], db)
    render_template('dashboard.html', usernameKept=session['username'],
                    s1=enrolledtable.S1, s2=enrolledtable.S2, s3=enrolledtable.S3, s4=enrolledtable.S4, s5=enrolledtable.S5,
                    s6=enrolledtable.S6, s7=enrolledtable.S7, s8=enrolledtable.S8, s9=enrolledtable.S9, s10=enrolledtable.S10,
                    s11=enrolledtable.S11, s12=enrolledtable.S12, s13=enrolledtable.S13, s14=enrolledtable.S14, s15=enrolledtable.S15,
                    s16=enrolledtable.S16, s17=enrolledtable.S17, s18=enrolledtable.S18, s19=enrolledtable.S19, s20=enrolledtable.S20,
                    s21=enrolledtable.S21, s22=enrolledtable.S22, s23=enrolledtable.S23, s24=enrolledtable.S24, s25=enrolledtable.S25,
                    s26=enrolledtable.S26, s27=enrolledtable.S27, s28=enrolledtable.S28, s29=enrolledtable.S29, s30=enrolledtable.S30,
                    s31=enrolledtable.S31, s32=enrolledtable.S32, s33=enrolledtable.S33, s34=enrolledtable.S34, s35=enrolledtable.S35,
                    s36=enrolledtable.S36, s37=enrolledtable.S37, s38=enrolledtable.S38, s39=enrolledtable.S39, s40=enrolledtable.S40,
                    s41=enrolledtable.S41, s42=enrolledtable.S42, s43=enrolledtable.S43, s44=enrolledtable.S44, s45=enrolledtable.S45,
                    s46=enrolledtable.S46, s47=enrolledtable.S47, s48=enrolledtable.S48, s49=enrolledtable.S49, s50=enrolledtable.S50,
                    s51=enrolledtable.S51, s52=enrolledtable.S52, s53=enrolledtable.S53, s54=enrolledtable.S54, s55=enrolledtable.S55,
                    s56=enrolledtable.S56, s57=enrolledtable.S57, s58=enrolledtable.S58, s59=enrolledtable.S59, s60=enrolledtable.S60,
                    s61=enrolledtable.S61, s62=enrolledtable.S62, s63=enrolledtable.S63, s64=enrolledtable.S64, s65=enrolledtable.S65,
                    s66=enrolledtable.S66, s67=enrolledtable.S67, s68=enrolledtable.S68, s69=enrolledtable.S69, s70=enrolledtable.S70)
    return redirect(url_for('dashboard'))
    

@app.route('/logout')
def logout():
    username = ""
    password = ""
    session.clear()
    print("session killed")
    render_template('index.html')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=8888)