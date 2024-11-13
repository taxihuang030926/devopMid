from flask import Flask, request, render_template, redirect, flash
from init import student_data, courses_data, Session

app = Flask(__name__)

def can_drop_course(S_ID, Course_ID):
    """
    判斷學生是否可以退選指定的課程。
    退選條件：
    1. 退選後的總學分數需大於 9。
    2. 不可退選必修課程。
    """
    student = student_data(S_ID)
    course = courses_data(Course_ID)

    # 檢查退選後的學分數
    if student.Ttl_Credit - course.Course_Credit < 9:
        return False, '退選後總學分數需大於 9'
    
    # 檢查是否為必修課程
    if course.prereq == 1:  # 假設 `prereq` 欄位表示是否為必修 (1 為必修)
        return False, '此課程為必修，不可退選'
    
    return True, '可退選'

@app.route('/drop_course', methods=['POST'])
def drop_course():
    S_ID = request.form.get('S_ID')
    Course_ID = request.form.get('Course_ID')
    session = Session()

    can_drop, message = can_drop_course(S_ID, Course_ID)
    if can_drop:
        try:
            # 執行退選操作
            session.query(EnrolledTable).filter_by(S_ID=S_ID, Course_ID=Course_ID).delete()
            session.commit()
            flash('退選成功', 'success')
        except Exception as e:
            session.rollback()
            flash(f'退選失敗: {str(e)}', 'danger')
        finally:
            session.close()
    else:
        flash(message, 'warning')
    
    return redirect('/')  # 修改成實際頁面名稱

if __name__ == '__main__':
    app.run(debug=True)
