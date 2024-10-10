-- Создание базы данных (если не создано)
CREATE DATABASE IF NOT EXISTS Cars;

-- Использование базы данных
USE Cars;

-- Создание таблицы сотрудников (Employees)
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    position VARCHAR(50),
    hire_date DATE
);

-- Вставка данных в таблицу сотрудников
INSERT INTO employees (name, position, hire_date)
VALUES 
('Alexander Petrov', 'Sales Manager', '2022-04-15'),
('Natalie Kim', 'Sales Representative', '2020-02-01'),
('Berry Dylan', 'Sales Associate', '2013-10-23');

-- Создание таблицы типов машин (Car_Types)
CREATE TABLE IF NOT EXISTS car_types (
    id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL
);

-- Вставка данных в таблицу типов машин
INSERT INTO car_types (type_name)
VALUES ('Classic Cars'), ('Van'), ('Sports Car'), ('Station Wagon');

-- Создание таблицы машин (Cars)
CREATE TABLE IF NOT EXISTS cars (
    id INT AUTO_INCREMENT PRIMARY KEY,
    model VARCHAR(100) NOT NULL,
    brand VARCHAR(50) NOT NULL,
    car_type_id INT, 
    price DECIMAL(10, 2) NOT NULL,
    production_year YEAR,
    FOREIGN KEY (car_type_id) REFERENCES car_types(id)
);

-- Вставка данных в таблицу машин
INSERT INTO cars (model, brand, car_type_id, price, production_year)
VALUES 
('Model S', 'Tesla', 1, 79999.99, 2023),
('Civic', 'Honda', 1, 25000.00, 2022),
('Mustang', 'Ford', 3, 55000.00, 2021),
('F-150', 'Ford', 4, 45000.00, 2020);

-- Создание таблицы продаж (Sales)
CREATE TABLE IF NOT EXISTS sales (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    employee_id INT,
    car_id INT, 
    sale_date DATE, 
    sale_price DECIMAL (10, 2) NOT NULL, 
    FOREIGN KEY (employee_id) REFERENCES employees(id), 
    FOREIGN KEY (car_id) REFERENCES cars(id)
);

-- Вставка данных в таблицу продаж
INSERT INTO sales (employee_id, car_id, sale_date, sale_price)
VALUES 
(1, 1, '2023-03-15', 79999.99),
(2, 2, '2023-04-20', 24000.00),
(3, 3, '2024-03-10', 53000.00),
(1, 4, '2024-04-25', 44000.00);
