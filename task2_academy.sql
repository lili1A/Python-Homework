CREATE DATABASE IF NOT EXISTS University;
USE University;

-- корпуса
CREATE TABLE buildings (
	building_id INT AUTO_INCREMENT PRIMARY KEY,
	building_name VARCHAR(50) NOT NULL
);
-- кафедры
CREATE TABLE departments (
	department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL,
    building_id INT,
    funding decimal(15, 2) NOT NULL, 
    FOREIGN KEY (building_id) REFERENCES buildings(building_id)
    );
-- преподаватели
CREATE TABLE teachers (
	teacher_id INT AUTO_INCREMENT PRIMARY KEY,
	teacher_name VARCHAR(100) NOT NULL,
	salary DECIMAL(10, 2) NOT NULL,
	department_id INT,
	FOREIGN KEY (department_id) REFERENCES departments(department_id)
);
-- студенческие группы 
CREATE TABLE student_groups (
    group_id INT AUTO_INCREMENT PRIMARY KEY,
    group_name VARCHAR(50) NOT NULL,
    curator_id INT,
    FOREIGN KEY (curator_id) REFERENCES teachers(teacher_id)
);
-- студенты
CREATE TABLE students (
	student_id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    group_id INT,
    rating DECIMAL(5, 2) NOT NULL,
    FOREIGN KEY (group_id) REFERENCES student_groups(group_id)
);
-- расписание лекций
CREATE TABLE  lectures (
	lecture_id INT AUTO_INCREMENT PRIMARY KEY,
    lecture_name VARCHAR(100) NOT NULL,
    teacher_id INT,
    group_id INT,
    week_number INT,
    lecture_day VARCHAR(10),
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
);
    
    
