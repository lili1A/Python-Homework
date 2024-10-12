CREATE DATABASE IF NOT EXISTS University;
USE University;

-- корпуса
CREATE TABLE buildings (
	building_id INT AUTO_INCREMENT PRIMARY KEY,
	building_name VARCHAR(50) NOT NULL
);

INSERT INTO buildings (building_name)
VALUES 
('Building A'),
('Building B'),
('Building C');

-- кафедры
CREATE TABLE departments (
	department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL,
    building_id INT,
    funding decimal(15, 2) NOT NULL, 
    FOREIGN KEY (building_id) REFERENCES buildings(building_id)
    );
    
    INSERT INTO departments (department_name, building_id, funding)
VALUES 
('Computer Science', 1, 120000.00),
('Mathematics', 1, 80000.00),
('Business', 2, 90000.00),
('Physics', 2, 95000.00),
('Literature', 3, 60000.00),
('Engineering', 3, 105000.00);

-- преподаватели
CREATE TABLE teachers (
	teacher_id INT AUTO_INCREMENT PRIMARY KEY,
	teacher_name VARCHAR(100) NOT NULL,
	salary DECIMAL(10, 2) NOT NULL,
	department_id INT,
	FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

INSERT INTO teachers (teacher_name, salary, department_id)
VALUES 
('John Doe', 6000.00, 1),
('Jane Smith', 5500.00, 2),
('Mike Johnson', 7000.00, 3),
('Emily Davis', 7500.00, 4),
('William Brown', 8000.00, 5),
('Sophia Miller', 6200.00, 6);

-- студенческие группы 
CREATE TABLE student_groups (
    group_id INT AUTO_INCREMENT PRIMARY KEY,
    group_name VARCHAR(50) NOT NULL,
    curator_id INT,
    FOREIGN KEY (curator_id) REFERENCES teachers(teacher_id)
);

INSERT INTO student_groups (group_name, curator_id)
VALUES 
('CS101', 1),
('MATH102', 2),
('BUS103', 3),
('PHY104', 4),
('D221', 5),
('ENG106', 6);

-- студенты
CREATE TABLE students (
	student_id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    group_id INT,
    rating DECIMAL(5, 2) NOT NULL,
    FOREIGN KEY (group_id) REFERENCES student_groups(group_id)
);

INSERT INTO students (student_name, group_id, rating)
VALUES 
('Alice Cooper', 1, 4.5),
('Bob Marley', 1, 4.8),
('Charlie Parker', 2, 4.1),
('Diana Ross', 3, 4.7),
('Ella Fitzgerald', 4, 3.9),
('Frank Sinatra', 5, 4.3),
('George Benson', 6, 4.0);

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

INSERT INTO lectures (lecture_name, teacher_id, group_id, week_number, lecture_day)
VALUES 
('Advanced Python', 1, 1, 1, 'Monday'),
('Linear Algebra', 2, 2, 1, 'Tuesday'),
('Marketing Basics', 3, 3, 1, 'Wednesday'),
('Quantum Mechanics', 4, 4, 1, 'Thursday'),
('World Literature', 5, 5, 1, 'Friday'),
('Mechanical Engineering', 6, 6, 1, 'Monday'),
('Data Structures', 1, 1, 2, 'Tuesday'),
('Abstract Algebra', 2, 2, 2, 'Wednesday');

    
