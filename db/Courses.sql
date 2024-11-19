CREATE TABLE Courses(
    Course_ID INT primary key,
    Course_Name VARCHAR(40),
    dept VARCHAR(20),
    prereq INT,
    Class VARCHAR(10),
    Instructor VARCHAR(100),
    Course_Credit INT
);

insert into Courses(Course_ID, Course_Name, dept, prereq, Class, Instructor, Course_Credit) values(1312, "作業系統", "資訊", 1, "三乙", "林志敏", 3);
insert into Courses(Course_ID, Course_Name, dept, prereq, Class, Instructor, Course_Credit) values(1314, "微處理機系統", "資訊", 1, "三乙", "郭崇韋", 3);
insert into Courses(Course_ID, Course_Name, dept, prereq, Class, Instructor, Course_Credit) values(1313, "微處理器系統實習", "資訊", 1, "三乙", "郭崇韋", 1);
insert into Courses(Course_ID, Course_Name, dept, prereq, Class, Instructor, Course_Credit) values(1313, "系統程式", "資訊", 1, "三乙", "劉宗杰", 3);
insert into Courses(Course_ID, Course_Name, dept, prereq, Class, Instructor, Course_Credit) values(1323, "軟體工程開發實務", "資訊", 0, "三乙", "許懷中", 3);
insert into Courses(Course_ID, Course_Name, dept, prereq, Class, Instructor, Course_Credit) values(2911, "德文（一）", "外語", 0, NULL, "游曉嵐", 2);
insert into Courses(Course_ID, Course_Name, dept, prereq, Class, Instructor, Course_Credit) values(3026, "德文（一）", "外語", 0, NULL, "王允闐", 2);
insert into Courses(Course_ID, Course_Name, dept, prereq, Class, Instructor, Course_Credit) values(2984, "音樂行旅 - 巡訪古典音樂大師", "通識", 0, NULL, "曾韻心", 2);
select * from Courses;