CREATE DATABASE IF NOT EXISTS AircraftSales;
USE AircraftSales;
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL
);
CREATE TABLE IF NOT EXISTS airplanes (
	airplane_id INT AUTO_INCREMENT PRIMARY KEY,
	model VARCHAR(100) NOT NULL
);
CREATE TABLE IF NOT EXISTS sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    airplane_id INT,
    sale_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (airplane_id) REFERENCES airplanes(airplane_id)
);



INSERT INTO customers (customer_name)
VALUES 
('Jane Smith'),
('John Doe'),
('Emma Watson'),
('Michael Myers');

INSERT INTO airplanes (model)
VALUES 
('Boeing 737'),
('Airbus A320'),
('Cessna 172'),
('Gulfstream G650');

INSERT INTO sales (customer_id, airplane_id, sale_date)
VALUES 
(1, 1, '2006-01-15'),
(2, 2, '2008-02-20'),
(3, 3, '2010-03-30');
