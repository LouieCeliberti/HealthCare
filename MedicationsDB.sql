CREATE DATABASE Medications;


CREATE TABLE MedicationName (

medName VARCHAR(20)

);

CREATE TABLE Dosage (

dose FLOAT

);

INSERT INTO MedicationName VALUES('Mychophenolate');
INSERT INTO MedicationName VALUES('Cyclosporine');
INSERT INTO MedicationName VALUES('Prednisone');
INSERT INTO MedicationName VALUES('Clonodine');
INSERT INTO MedicationName VALUES('Niphedimine');
INSERT INTO MedicationName VALUES('Sodium Bicarbonate');
INSERT INTO MedicationName VALUES('Glycopyrolate');
INSERT INTO MedicationName VALUES('Pantoprezol');

INSERT INTO Dosage VALUES(500);
INSERT INTO Dosage VALUES(275);
INSERT INTO Dosage VALUES(10);
INSERT INTO Dosage VALUES(0.1);
INSERT INTO Dosage VALUES(30);
INSERT INTO Dosage VALUES(625);
INSERT INTO Dosage VALUES(1);
INSERT INTO Dosage VALUES(40);


SELECT * FROM MedicationName, Dosage;

DROP TABLE MedicationName
DROP TABLE Dosage
