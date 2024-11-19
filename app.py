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

username = ""
password = ""

def checkEnrolled(S_ID, Course_ID, db):
    enrolledtable = fetchEnrolledTable(S_ID, db)
    for i in range(1, 71):
        if int(enrolledtable[i]) == Course_ID:
            return True
    
    return False

# login 
@app.route('/')
def index():
    if 'username' in session:
        render_template('dashboard.html', usernameKept=session['username'])
        return redirect(url_for('dashboard'))
    else:
        return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    username = request.form.get("username",False)
    password = request.form.get("password",False)
    student_data = Search.searchUser(db, username, password)
    if(Search.searchUser(db, username, password)):
        S_ID = student_data[0]
        session['username'] = username
        autoEnrollCourses(S_ID, db)
        render_template('dashboard.html', usernameKept=session['username'])
        return redirect(url_for('dashboard'))
    else:
        flash('Invalid username or password')
        render_template('index.html')
        return redirect(url_for('index'))

# dashboard 
@app.route('/dashboard')
def dashboard():
    print(username)
    return render_template('dashboard.html', usernameKept=session['username'])

@app.route('/handle_course', methods=['POST'])
def handle_course():
    course_id = request.form['course_id']
    S_ID = session.get('username') 
    if(fetchCourseData(course_id, db)):
        if(fetchEnrolledTable(S_ID, db)):
            # check if the course is already enrolled -> drop
            if(enrollment.checkEnrolled(S_ID, course_id, db)):
                drop.dropCourse(S_ID, course_id, db)
                flash('成功退選')
            # check if the course is not enrolled -> enroll
    
    else:
        flash('找不到課程')

    return render_template('dashboard.html', usernameKept=session['username'])
    

@app.route('/logout')
def logout():
    username = ""
    password = ""
    session.clear()
    print("session killed")
    render_template('index.html')
    return redirect(url_for('index'))

def autoEnrollCourses(S_ID, db):
    # 查詢學生班級
    student_class = Search.searchStudentClass(db, S_ID)

    if student_class:
        # 查詢該班級的所有必修課程
        cursor = db.cursor()
        query = """
        SELECT Course_ID 
        FROM Courses 
        WHERE Class = %s AND prereq != 0
        """
        cursor.execute(query, (student_class,))
        mandatory_courses = [row[0] for row in cursor.fetchall()]
        cursor.close()

        # 取得學生的選課記錄
        enrolled_courses = Search.searchEnrolled(db, S_ID)  # 假設此函式會返回學生選修的課程 ID 列表

        # 取得每門課程的上課時間
        for course_id in mandatory_courses:
            if course_id not in enrolled_courses:  # 檢查學生是否已選修該課程
                # 查詢該課程的上課時間
                cursor = db.cursor()
                cursor.execute("SELECT Session_Day, Session_RTime, Session_Time FROM Course_Session WHERE Course_ID = %s;", (course_id,))
                course_sessions = cursor.fetchall()
                cursor.close()

                # 檢查是否有時間衝突
                conflict_found = False
                for session_day, session_rtime, session_time in course_sessions:
                    for i in range(1, 71):  # 假設最多有70門課
                        enrolled_course_id = enrolled_courses[i]
                        if enrolled_course_id != 0:  # 有課程
                            # 查詢已選課程的上課時間
                            cursor = db.cursor()
                            cursor.execute("SELECT Session_Day, Session_RTime, Session_Time FROM Course_Session WHERE Course_ID = %s;", (enrolled_course_id,))
                            enrolled_course_sessions = cursor.fetchall()
                            cursor.close()

                            # 檢查時間是否衝突
                            for enrolled_session_day, enrolled_session_rtime, enrolled_session_time in enrolled_course_sessions:
                                if session_day == enrolled_session_day and session_rtime == enrolled_session_rtime:
                                    conflict_found = True
                                    break
                        if conflict_found:
                            break
                    if conflict_found:
                        break

                # 如果沒有時間衝突，加入課程
                if not conflict_found:
                    for i in range(1, 71):  # 假設最多有70門課
                        if enrolled_courses[i] == 0:  # 空位
                            update_query = f"UPDATE Enrolled_Table SET S{i} = %s WHERE S_ID = %s"
                            cursor.execute(update_query, (course_id, S_ID))
                            db.commit()  # 提交更新
                            flash(f'已自動為你選修課程 {course_id}')
                            break
                else:
                    flash(f'課程 {course_id} 與其他選課時間衝突，無法選課！')
        flash('必修課程自動選修完成！')




if __name__ == '__main__':
    app.run(debug=True)