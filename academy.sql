CREATE DATABASE IF NOT EXISTS Academy;

USE Academy;

-- Таблица преподавателей (teachers) — для хранения информации о преподавателях, id, предмете, аудитории, группе. 
-- Таблица преподавателей (students) — для хранения информации о студентах, id, основном предмете, группе. 
-- Таблица расписания лекций (lectures) — для хранения информации о том, какие лекции проводятся, в какие дни, и в каких аудиториях.
-- Таблица ставок преподавателей (teacher_salaries) — для хранения информации о ставках преподавателей.
-- Обновление существующих таблиц преподавателей (teachers) и студентов (students) — для хранения данных о количестве дисциплин и кафедрах.


-- Таблица преподавателей (teachers) - преподаватели, предметы, аудитории
CREATE TABLE IF NOT EXISTS teachers (
    teacher_id INT AUTO_INCREMENT PRIMARY KEY,
    teacher_name VARCHAR(100) NOT NULL,
    subject_name VARCHAR(50),
    department VARCHAR(50),
    auditorium VARCHAR(10) NOT NULL
);

INSERT INTO teachers (teacher_name, subject_name, department, auditorium)
VALUES 
('Dave McQueen', 'Python', 'School of Computer Science', 'D201'),
('Anastasia Lee', 'Accounting', 'School of Business', 'D202'),
('Ben Smith', 'Java', 'School of Computer Science', 'D203'),
('Nathan Kim', 'International Relations', 'School of Business', 'D204'),
('Jack Underhill', 'Cyber Security', 'School of Computer Science', 'D205');

-- Таблица студентов (students) - студенты, их группы и специализации
CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    major VARCHAR(50),
    student_group VARCHAR(10) NOT NULL
);

INSERT INTO students (student_name, major, student_group)
VALUES
('Marie Sui', 'Computer Science', 'CS001'),
('Alice Jane', 'Computer Science', 'CS001'),
('Kate Ri', 'Computer Science', 'CS001'),
('Kim Ling', 'Software Engineering', 'SE001'),
('Sam Pittersen', 'Software Engineering', 'SE001'),
('Inna Ten', 'Software Engineering', 'SE001');

-- промежуточная таблица  для связи преподавателей и студентов через группы
CREATE TABLE IF NOT EXISTS student_teacher_groups (
    group_id INT AUTO_INCREMENT PRIMARY KEY,
    student_group VARCHAR(10) NOT NULL,
    teacher_id INT NOT NULL,
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
);

INSERT INTO student_teacher_groups (student_group, teacher_id)
VALUES
('CS001', 1),  -- Dave McQueen
('CS001', 2),  -- Anastasia Lee
('CS001', 3),  -- Ben Smith
('SE001', 4),  -- Nathan Kim
('SE001', 5);  -- Jack Underhill

-- Таблица расписания лекций (lectures) - лекции, аудтории, дни
CREATE TABLE IF NOT EXISTS lectures (
    lecture_id INT AUTO_INCREMENT PRIMARY KEY,
    teacher_id INT, 
    subject_name VARCHAR(50),  
    auditorium VARCHAR(10), 
    lecture_day VARCHAR(10),  
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
);

INSERT INTO lectures (teacher_id, subject_name, auditorium, lecture_day)
VALUES
(1, 'Python', 'D201', 'Monday'),
(2, 'Accounting', 'D202', 'Tuesday'),
(3, 'Java', 'D203', 'Wednesday'),
(4, 'International Relations', 'D204', 'Thursday'),
(5, 'Cyber Security', 'D205', 'Friday');

-- Таблица ставок преподавателей (teacher_salaries)
CREATE TABLE IF NOT EXISTS teacher_salaries (
    teacher_id INT PRIMARY KEY,
    salary DECIMAL(10, 2),
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
);

INSERT INTO teacher_salaries (teacher_id, salary)
VALUES 
(1, 6000.00),
(2, 7000.00),
(3, 6500.00),
(4, 5500.00),
(5, 6200.00);


-- кол-во преподов Software Engineering - через связь между student_group
-- колво лекций Dave McQueen 
-- количество занятий, проводимых в ауди- тории “D201”.
-- Вывести названия аудиторий и количество лекций, проводимых в них.
-- количество студентов, посещающих лекции преподавателя “Jack Underhill”
-- Вывести среднюю ставку преподавателей факультета “Computer Science”.
-- минимальное и максимальное количество студентов среди всех групп.
-- Вывести полные имена преподавателей и количество читаемых ими дисциплин.
-- Вывести количество лекций в каждый день недели.
-- Вывести номера аудиторий и количество кафедр, чьи лекции в них читаются
-- Вывести количество лекций для каждой пары преподаватель-аудитория.

    






