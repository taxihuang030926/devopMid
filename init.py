import mysql.connector as mc

class Students:
    def __init__(self, S_ID, Name, Ttl_Credit, S_pwd, dept, Grade, Class):
        self.sid = S_ID
        self.name = Name
        self.credit = Ttl_Credit
        self.password = S_pwd
        self.dept = dept
        self.grade = Grade
        self.classNum = Class

class Courses:
    def __init__(self, Course_ID, Course_Name, dept, prereq, Class, Instructor, Course_Credit):
        self.cid = Course_ID
        self.name = Course_Name
        self.dept = dept
        self.prereq = prereq
        self.classNum = Class
        self.instructor = Instructor
        self.credit = Course_Credit

class Course_Session:
    def __init__(self, Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom):
        self.session_id = Session_ID
        self.Course_id = Course_ID
        self.day = Session_Day
        self.session_rtime = Session_RTime
        self.session_time = Session_Time
        self.classroom = Classroom

class EnrolledTable:
    def __init__(self, S_ID,S1,S2,S3,S4,S5,S6,S7,S8,S9,S10,
                 S11,S12,S13,S14,S15,S16,S17,S18,S19,S20,
                 S21,S22,S23,S24,S25,S26,S27,S28,S29,S30,
                 S31,S32,S33,S34,S35,S36,S37,S38,S39,S40,
                 S41,S42,S43,S44,S45,S46,S47,S48,S49,S50,
                 S51,S52,S53,S54,S55,S56,S57,S58,S59,S60,
                 S61,S62,S63,S64,S65,S66,S67,S68,S69,S70):
        self.S_ID = S_ID
        self.S1 =   S1; self.S2 =   S2; self.S3 =   S3; self.S4 =   S4; self.S5 =   S5
        self.S6 =   S6; self.S7 =   S7; self.S8 =   S8; self.S9 =   S9; self.S10 = S10
        self.S11 = S11; self.S12 = S12; self.S13 = S13; self.S14 = S14; self.S15 = S15
        self.S16 = S16; self.S17 = S17; self.S18 = S18; self.S19 = S19; self.S20 = S20
        self.S21 = S21; self.S22 = S22; self.S23 = S23; self.S24 = S24; self.S25 = S25
        self.S26 = S26; self.S27 = S27; self.S28 = S28; self.S29 = S29; self.S30 = S30
        self.S31 = S31; self.S32 = S32; self.S33 = S33; self.S34 = S34; self.S35 = S35
        self.S36 = S36; self.S37 = S37; self.S38 = S38; self.S39 = S39; self.S40 = S40
        self.S41 = S41; self.S42 = S42; self.S43 = S43; self.S44 = S44; self.S45 = S45
        self.S46 = S46; self.S47 = S47; self.S48 = S48; self.S49 = S49; self.S50 = S50
        self.S51 = S51; self.S52 = S52; self.S53 = S53; self.S54 = S54; self.S55 = S55
        self.S56 = S56; self.S57 = S57; self.S58 = S58; self.S59 = S59; self.S60 = S60
        self.S61 = S61; self.S62 = S62; self.S63 = S63; self.S64 = S64; self.S65 = S65
        self.S66 = S66; self.S67 = S67; self.S68 = S68; self.S69 = S69; self.S70 = S70

def fetchStudentData(db, S_ID):
    cur = db.cursor()
    cur.execute("SELECT * FROM Student WHERE S_ID=%s;", (S_ID,))
    result = cur.fetchone()
    
    if result:
        student = Students(S_ID=result[0], Name=result[1], Ttl_Credit=result[2], S_pwd=result[3], dept=result[4], Grade=result[5], Class=result[6])
        cur.close()
        return student
    else:
        cur.close()
        return None

def fetchCourseData(C_ID, db):
    cur = db.cursor()
    cur.execute("SELECT * FROM Courses WHERE course_id=%s", (C_ID,))
    result = cur.fetchone()
    
    if result:
        course = Courses(Course_ID=result[0], Course_Name=result[1], dept=result[2], prereq=result[3], Class=result[4], Instructor=result[5], Course_Credit=result[6])
        cur.close()
        return course
    else:
        cur.close()
        return None
    
def fetchCourseSession(C_ID, db):
    cur = db.cursor()
    cur.execute("SELECT * FROM Course_Session WHERE Course_ID=%s;", (C_ID,))
    results = cur.fetchall()
    
    session_list = []
    for result in results:
        session = Course_Session(Session_ID=result[0], Course_ID=result[1], Session_Day=result[2], Session_RTime=result[3], Session_Time=result[4], Classroom=result[5])
        session_list.append(session)
    
    cur.close()
    return session_list 

def fetchEnrolledTable(S_ID, connectServer):
    # print("fetchEnrolledTable")
    cur = connectServer.cursor()
    cur.execute("SELECT * FROM Enrolled_Table WHERE S_ID=%s;",(S_ID,))
    results = cur.fetchone()

    enrolledtable = EnrolledTable(S_ID=results[0], S1=results[1], S2=results[2], S3=results[3], S4=results[4], S5=results[5],
                                  S6=results[6], S7=results[7], S8=results[8], S9=results[9], S10=results[10],
                                  S11=results[11], S12=results[12], S13=results[13], S14=results[14], S15=results[15],
                                  S16=results[16], S17=results[17], S18=results[18], S19=results[19], S20=results[20],
                                  S21=results[21], S22=results[22], S23=results[23], S24=results[24], S25=results[25],
                                  S26=results[26], S27=results[27], S28=results[28], S29=results[29], S30=results[30],
                                  S31=results[31], S32=results[32], S33=results[33], S34=results[34], S35=results[35],
                                  S36=results[36], S37=results[37], S38=results[38], S39=results[39], S40=results[40],
                                  S41=results[41], S42=results[42], S43=results[43], S44=results[44], S45=results[45],
                                  S46=results[46], S47=results[47], S48=results[48], S49=results[49], S50=results[50],
                                  S51=results[51], S52=results[52], S53=results[53], S54=results[54], S55=results[55],
                                  S56=results[56], S57=results[57], S58=results[58], S59=results[59], S60=results[60],
                                  S61=results[61], S62=results[62], S63=results[63], S64=results[64], S65=results[65],
                                  S66=results[66], S67=results[67], S68=results[68], S69=results[69], S70=results[70])

    cur.close()
    return enrolledtable
