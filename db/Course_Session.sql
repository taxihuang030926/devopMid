CREATE TABLE Course_Session (
    Session_ID varchar(8) primary key,
    Course_ID INT,
    Session_Day VARCHAR(20),
    Session_RTime INT,
    Session_Time INT,
    Classroom VARCHAR(20),
    foreign key(Course_ID) references Courses(Course_ID)
);


insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom) values("1312-1", 1312, "Monday", 3, 3, "資電402");
insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom) values("1312-2", 1312, "Monday", 4, 4, "資電402");
insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom) values("1312-3", 1312, "Wednesday", 4, 32, "資電402");

insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom) values("1314-1", 1314, "Monday", 6, 6, "科航207");
insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom) values("1314-2", 1314, "Monday", 7, 7, "科航207");
insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom) values("1314-3", 1314, "Tuesday", 3, 17, "資電504");

insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom) values("1313-1", 1313, "Monday", 8, 8, "土水304");
insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom) values("1313-2", 1313, "Monday", 9, 9, "土水304");

insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom) values("1318-1", 1318, "Tuesday", 6, 20, "資電403");
insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom) values("1318-2", 1318, "Tuesday", 7, 21, "資電403");
insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom) values("1318-3", 1318, "Friday", 4, 60, "資電403");

insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom) values("1323-1", 1323, "Wednesday", 6, 34, "資電234");
insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom) values("1323-2", 1323, "Wednesday", 7, 35, "資電234");
insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom) values("1323-3", 1323, "Wednesday", 8, 36, "資電234");

insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom) values("1439-1", 1439, "Monday", 1, 1, "資電415");
insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom) values("1439-2", 1439, "Monday", 2, 2, "資電415");

insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom) values("1440-1", 1440, "Tuesday", 8, 22, "資電415");
insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom) values("1440-2", 1440, "Tuesday", 9, 23, "資電415");

insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom) values("1323-1", 1323, "Wednesday", 2, 30, "資電402");
insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom) values("1323-2", 1323, "Wednesday", 3, 31, "資電402");

insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom) values("2911-1", 2911, "Friday", 6, 62, "語文202");
insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom) values("2911-2", 2911, "Friday", 7, 63, "語文202");

insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom) values("3026-1", 3026, "Friday", 3, 59, "語文202");
insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom) values("3026-2", 3026, "Friday", 4, 60, "語文202");

insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom) values("3055-1", 3055, "Thursday", 3, 45, "人言507");
insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom) values("3055-2", 3055, "Thursday", 4, 46, "人言507");

insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom) values("2984-1", 2984, "Monday", 11, 11, "商學204");
insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom) values("2984-2", 2984, "Monday", 12, 12, "商學204");

insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom) values("3077-1", 3077, "Friday", 1, 57, "商學205");
insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom) values("3077-2", 3077, "Friday", 2, 58, "商學205");

insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom) values("3079-1", 3079, "Monday", 8, 64, "商學304");
insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom) values("3079-2", 3079, "Monday", 9, 65, "商學304");

insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom) values("3083-1", 2984, "Thursday", 6, 47, "商學207");
insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom) values("3083-2", 2984, "Thursday", 7, 48, "商學207");

insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom) values("3084-1", 3084, "Thursday", 8, 11, "商學208");
insert into Course_Session(Session_ID, Course_ID, Session_Day, Session_RTime, Session_Time, Classroom) values("3084-2", 3084, "Thursday", 9, 12, "商學208");