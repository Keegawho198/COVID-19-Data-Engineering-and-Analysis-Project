-- Create the Countries Table
CREATE TABLE "Countries" (
    "Country Code" VARCHAR(30) PRIMARY KEY NOT NULL,
    "Country" VARCHAR(100) NOT NULL
);

-- Create the Coordinates Table
CREATE TABLE "Coordinates" (
    "Country Code" VARCHAR(30) NOT NULL,
    "Latitude" FLOAT NOT NULL,
    "Longitude" FLOAT NOT NULL,
    "Coordinates" VARCHAR(30) PRIMARY KEY NOT NULL,
    FOREIGN KEY("Country Code") REFERENCES "Countries"("Country Code")
);

-- Create the COVID-19 Dataset Table
CREATE TABLE "COVID-19_Dataset" (
    "id" INT PRIMARY KEY NOT NULL,
    "Date" TIMESTAMP NOT NULL,
    "Country Code" VARCHAR(30) NOT NULL,
    "Country" VARCHAR(100) NOT NULL,
    "Continent" VARCHAR(50),
    "WHO Region" VARCHAR(10),
    "New Cases" FLOAT,
    "Cumulative Cases" FLOAT,
    "New Deaths" FLOAT,
    "Cumulative Deaths" FLOAT,
    "Coordinates" VARCHAR(30),
    "Case ID" VARCHAR(50) UNIQUE NOT NULL,
    FOREIGN KEY("Country Code") REFERENCES "Countries"("Country Code"),
    FOREIGN KEY("Coordinates") REFERENCES "Coordinates"("Coordinates")
);

-- Create the Patient Database Table
CREATE TABLE "Patient_Database" (
    "Case ID" VARCHAR(50) PRIMARY KEY NOT NULL,
    "Date" TIMESTAMP NOT NULL,
    "Country Code" VARCHAR(30) NOT NULL,
    "New Cases" FLOAT,
    "Cumulative Cases" FLOAT,
    "New Deaths" FLOAT,
    "Cumulative Deaths" FLOAT,
    FOREIGN KEY("Country Code") REFERENCES "Countries"("Country Code")
);