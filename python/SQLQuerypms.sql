CREATE DATABASE PMS_db --creating database

USE PMS_db 

CREATE TABLE Patient_details(
	patientID INT PRIMARY KEY,
	patientName VARCHAR(50),
	gender VARCHAR(20),
	age INT,
	bloodGroup VARCHAR(10)
)

SELECT * FROM Patient_details
DELETE FROM Patient_details WHERE patientName="roshni"

            