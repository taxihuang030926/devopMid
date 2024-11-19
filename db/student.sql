create table Student(
    S_ID VARCHAR(8) primary key,
    Name VARCHAR(20),
    Ttl_Credit INT,
    S_pwd VARCHAR(20),
    dept VARCHAR(20),
    Grade INT,
    Class VARCHAR(8)
);

insert into Student(S_ID, Name, Ttl_Credit, S_pwd, dept, Grade, Class) values("D1149888", "Std_A", 0, "888", "資訊", 3, 2);
insert into Student(S_ID, Name, Ttl_Credit, S_pwd, dept, Grade, Class) values("D1152274", "Std_B", 0, "274", "資訊", 3, 1);
insert into Student(S_ID, Name, Ttl_Credit, S_pwd, dept, Grade, Class) values("D1149782", "Std_C", 0, "782", "資訊", 3, 3);
insert into Student(S_ID, Name, Ttl_Credit, S_pwd, dept, Grade, Class) values("D1150267", "Std_D", 0, "267", "資訊", 3, 2);

select * from Student;