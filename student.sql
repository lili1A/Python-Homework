CREATE DATABASE student;
USE student;
CREATE TABLE student (
	id INT AUTO_INCREMENT PRIMARY KEY, 
	first_name VARCHAR(100),
    last_name VARCHAR(100),
    birth_date DATE,
    email VARCHAR(100)
);

INSERT INTO student (first_name, last_name, birth_date, email)
VALUES ('Jane', 'Doe', '2001-03-23', 'janed03@mailcom'),
('Ken', 'Sakamoto', '2002-04-22', 'sakam2t@mailcom'),
('Alice', 'Kim', '1999-12-02', 'a11cekim@mailcom');
