CREATE TABLE Courses(
    Course_ID INT primary key,
    Course_Name VARCHAR(40),
    dept VARCHAR(20),
    prereq INT,
    Grade INT,
    Class INT,
    Instructor VARCHAR(100),
    Course_Credit INT
);

insert into Courses(Course_ID, Course_Name, dept, prereq, Grade, Class, Instructor, Course_Credit) values(1312, "作業系統", "資訊", 1, 3, 2, "林志敏", 3);
insert into Courses(Course_ID, Course_Name, dept, prereq, Grade, Class, Instructor, Course_Credit) values(1314, "微處理機系統", "資訊", 1, 3, 2, "郭崇韋", 3);
insert into Courses(Course_ID, Course_Name, dept, prereq, Grade, Class, Instructor, Course_Credit) values(1313, "微處理器系統實習", "資訊", 1, 3, 2, "郭崇韋", 1);
insert into Courses(Course_ID, Course_Name, dept, prereq, Grade, Class, Instructor, Course_Credit) values(1318, "系統程式", "資訊", 1, 3, 2, "劉宗杰", 3);
insert into Courses(Course_ID, Course_Name, dept, prereq, Grade, Class, Instructor, Course_Credit) values(1323, "軟體工程開發實務", "資訊", 0, 3, 2, "許懷中", 3);
insert into Courses(Course_ID, Course_Name, dept, prereq, Grade, Class, Instructor, Course_Credit) values(1439, "編譯器", "資訊", 0, 3, 2, "陳青文", 3);
insert into Courses(Course_ID, Course_Name, dept, prereq, Grade, Class, Instructor, Course_Credit) values(1440, "資訊與網路安全", "資訊", 0, 3, 2, "張舜賢", 3);
insert into Courses(Course_ID, Course_Name, dept, prereq, Grade, Class, Instructor, Course_Credit) values(1323, "寬頻網路", "資訊", 0, 3, 2, "竇其仁", 3);
insert into Courses(Course_ID, Course_Name, dept, prereq, Grade, Class, Instructor, Course_Credit) values(2911, "德文（一）", "外語", 0, 0, 0, "游曉嵐", 2);
insert into Courses(Course_ID, Course_Name, dept, prereq, Grade, Class, Instructor, Course_Credit) values(3026, "德文（一）", "外語", 0, 0, 0, "王允闐", 2);
insert into Courses(Course_ID, Course_Name, dept, prereq, Grade, Class, Instructor, Course_Credit) values(2984, "音樂行旅 - 巡訪古典音樂大師", "通識", 0, 0, 0, "曾韻心", 2);
insert into Courses(Course_ID, Course_Name, dept, prereq, Grade, Class, Instructor, Course_Credit) values(3055, "台灣環境與永續發展", "通識", 0, 0, 0, "鄭翰", 2);
insert into Courses(Course_ID, Course_Name, dept, prereq, Grade, Class, Instructor, Course_Credit) values(3077, "環境教育", "通識", 0, 0, 0, "葉怡巖", 2);
insert into Courses(Course_ID, Course_Name, dept, prereq, Grade, Class, Instructor, Course_Credit) values(3079, "人生哲學", "通識", 0, 0, 0, "經觀榮", 2);
insert into Courses(Course_ID, Course_Name, dept, prereq, Grade, Class, Instructor, Course_Credit) values(3083, "中國文物欣賞", "通識", 0, 0, 0, "戴瑞坤", 2);
insert into Courses(Course_ID, Course_Name, dept, prereq, Grade, Class, Instructor, Course_Credit) values(3084, "佛家思想", "通識", 0, 0, 0, "鄭保村", 2);