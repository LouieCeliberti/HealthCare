CREATE DATABASE Pharmacy;

CREATE TABLE PharmacyName (

pharmName VARCHAR(25)

);

CREATE TABLE Address (

address VARCHAR(50)

);

CREATE TABLE PhoneNumber (

num VARCHAR(25)

);

SELECT * FROM PharmacyName, Address, PhoneNumber;

INSERT INTO PharmacyName VALUES('CVS');
INSERT INTO PharmacyName VALUES('Duane Reade');
INSERT INTO PharmacyName VALUES('Rite Aid');
INSERT INTO PharmacyName VALUES('CVS');

SELECT * FROM PharmacyName;

DROP TABLE Pharmacy
