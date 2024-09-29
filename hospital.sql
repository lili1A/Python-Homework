-- Employees:
-- EmployeeID (Primary Key)
-- FirstName
-- LastName
-- Position
-- DepartmentID: Идентификатор отделения, в котором работает сотрудник (Foreign Key)

-- Patients:
-- PatientID (Primary Key)
-- FirstName
-- LastName
-- DateOFbirth
-- Sex
-- Address
-- PhoneNumber

-- Departments:
-- DepartmentID (Primary Key)
-- DepartmentName
-- HeadDoctorID: Идентификатор главного врача отделения (Foreign Key, ссылается на EmployeeID)

-- Отношения между таблицами:
-- Employees и Departments через DepartmentID.
-- Departments и Employees через HeadDoctorID.

-- BCNF:
-- X содержит ключ таблицы
-- Y - часть ключа таблицы 
-- EmployeeID -> FirstName, LastName, Position, DepartmentID
-- PatientID -> FirstName, LastName, DateOfBirth, Gender, Address, PhoneNumber
-- DepartmentID -> DepartmentName, HeadDoctorID
SHOW DATABASES;
USE Hospital;


CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    Position VARCHAR(255),
    DepartmentID INT
);

CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(255),
    HeadDoctorID INT,
    FOREIGN KEY (HeadDoctorID) REFERENCES Employees(EmployeeID)
);

INSERT INTO Employees (EmployeeID, FirstName, LastName, Position, DepartmentID)
VALUES 
(001, 'Sam', 'Pitterson', 'Head doctor', 1),
(002, 'Kate', 'Smitt', 'Head surgeon', 2),
(003, 'Mike', 'Myers', 'Surgeon', 3),
(004, 'Ivan', 'Petrov', 'Nurse', 4),
(005, 'Natalie', 'Kim', 'Anesthetist', 5),
(006, 'Ami', 'Nakayama', 'Surgeon', 6),
(007, 'Ben', 'Harris', 'Nurse', 7),
(008, 'Minji', 'Lee', 'Surgeon', 8),
(009, 'Oleg', 'Malinin', 'Therapist', 9);

INSERT INTO Departments (DepartmentID, DepartmentName, HeadDoctorID)
VALUES 
(1, 'Cardiology', 001),
(2, 'Surgery', 002),
(3, 'Dentistry', 003);

CREATE TABLE Patients (
    patientID INT PRIMARY KEY,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    DateOfBirth DATE,
    Sex CHAR(1),
    Address VARCHAR(255),
    PhoneNumber VARCHAR(20)
);

INSERT INTO Patients (PatientID, FirstName, LastName, DateOfBirth, Sex, Address, PhoneNumber)
VALUES 
(1, 'Ken', 'Tanaka', '1983-01-01', 'M', 'Tokyo', '+7352464864'),
(2, 'Alex', 'Mirov', '1967-02-04', 'M', 'Los Angeles', '+3468345667'),
(3, 'Irina', 'Miller', '2004-12-11', 'F', 'Moscow', '+2364376754');
SHOW TABLES;
