from flask import Flask, request, render_template, redirect
from init import student_data, courses_data, enrolledtable_data, Session


def get_course_sessions(Course_ID, connectServer):
    cur = connectServer.cursor()
    cur.execute("SELECT Session_Time FROM Course_Session WHERE Course_ID = %s", (Course_ID,))
    results = cur.fetchall()
    cur.close()
    return results


def check_scheduale(S_ID, Course_ID):
    
    # 獲取新課程的所有上課時間
    new_course_sessions = get_course_sessions(Course_ID) 

    # 獲取學生的 Enrolled_Table 資料
    enrolled_data = enrolledtable_data(S_ID)
    if not enrolled_data:
        # 如果沒有任何已登記的時間段，則無衝突
        return True
    
    # 假設 enrolled_data 返回的列表中只有一筆紀錄
    enrollment_record = enrolled_data[0]

    # 檢查新課程的每個 Session_Time 是否與現有時段衝突
    for session in new_course_sessions:
        session_time = session["Session_Time"]
        
        # 根據 Session_Time 檢查對應的時段欄位 (S1 到 S70)
        if getattr(enrollment_record, f"S{session_time}") is not None:
            # 如果該時段已有課程，表示衝堂
            return False

    return True  # 無衝突
    
def get_enrolled_course_ids(S_ID, connectServer):
    
    # 取得已選課程的所有非空課程 ID
    enrolled_data = enrolledtable_data(S_ID, connectServer)
    if not enrolled_data:
        return []
    
    #假設以選課表裡只有一筆資料
    enrollment_record = enrolled_data[0]
    course_ids = []
    
    # 檢查每個 S1 到 S70 欄位，收集所有非 None 的課程 ID
    for i in range(1, 71):
        course_id = getattr(enrollment_record, f"S{i}")
        if course_id is not None:
            course_ids.append(course_id)
    
    return course_ids

def check_course_name_conflict(Course_ID, S_ID, connectServer):
    # 取得學生已選課程的課程 ID
    enrolled_course_ids = get_enrolled_course_ids(S_ID, connectServer)
    if not enrolled_course_ids:
        return False  # 沒有已選課程，無同名衝突

    # 根據課程 ID 查詢課程名稱
    cur = connectServer.cursor()
    query = "SELECT Course_Name FROM Courses WHERE Course_ID IN %s;"
    cur.execute(query, (tuple(enrolled_course_ids),))
    enrolled_course_names = [row[0] for row in cur.fetchall()]
    cur.close()
    
    # 檢查新課程名稱是否在已選課程名稱中
    return Course_ID in enrolled_course_names

def add_course(S_ID,Course_ID):
    student = student_data(S_ID)
    course =  courses_data(Course_ID)

    #判斷學分是否超過上限
    if course.Course_Credit + student.Ttl_Credit > 25:
        wrong = '學分已達上限'
        return False, wrong
    
    #判斷是否衝堂
    elif not check_scheduale(S_ID, Course_ID):
        wrong = '選課時間衝堂'
        return False,wrong

    #判斷是否有同名的課程
    elif check_course_name_conflict(Course_ID, S_ID):
        wrong = '已選課表中已有同名課程'
        return False, wrong
    
    else:
        