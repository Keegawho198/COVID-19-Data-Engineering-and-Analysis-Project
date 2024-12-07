-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.
--To avoid the import/export error, please imort the csv files in following order: Patient_Database -> coordinates-> Countries->COVID_19_Database


CREATE TABLE "COVID_19_Dataset" (
    "id" int   NOT NULL,
    "Date" timestamp   NOT NULL,
    "Country_Code" varchar(30)   NOT NULL,
    "Country" varchar(100)   NOT NULL,
    "Continent" varchar(50)   NOT NULL,
    "WHO_Region" varchar(10)   NOT NULL,
    "New_Cases" float   NOT NULL,
    "Cumulative_Cases" float   NOT NULL,
    "New_Deaths" float   NOT NULL,
    "Cumulative_Deaths" float   NOT NULL,
    "Coordinates" varchar(30)   NOT NULL,
    "Case_ID" varchar(50)   NOT NULL,
    CONSTRAINT "pk_COVID_19_Dataset" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "Countries" (
    "Country_Code" varchar(30)   NOT NULL,
    "Country" varchar(100)   NOT NULL,
    CONSTRAINT "pk_Countries" PRIMARY KEY (
        "Country_Code"
     )
);

CREATE TABLE "Patient_Database" (
    "Case_id" varchar(50)   NOT NULL,
    "Date" timestamp   NOT NULL,
    "Country_Code" varchar(30)   NOT NULL,
    "New_Cases" float   NOT NULL,
    "Cumulative_Cases" float   NOT NULL,
    "New_Deaths" float   NOT NULL,
    "Cumulative_Deaths" float   NOT NULL,
    CONSTRAINT "pk_Patient_Database" PRIMARY KEY (
        "Case_id"
     )
);

CREATE TABLE "Coordinates" (
    "Country_code" varchar(300)   NOT NULL,
    "Latitude" float   NOT NULL,
    "Longitude" float   NOT NULL,
    "Coordinates" varchar(30)   NOT NULL,
    CONSTRAINT "pk_Coordinates" PRIMARY KEY (
        "Country_code"
     )
);

ALTER TABLE "COVID_19_Dataset" ADD CONSTRAINT "fk_COVID_19_Dataset_Country_Code" FOREIGN KEY("Country_Code")
REFERENCES "Countries" ("Country_Code");

ALTER TABLE "COVID_19_Dataset" ADD CONSTRAINT "fk_COVID_19_Dataset_Case_ID" FOREIGN KEY("Case_ID")
REFERENCES "Patient_Database" ("Case_id");

ALTER TABLE "Countries" ADD CONSTRAINT "fk_Countries_Country_Code" FOREIGN KEY("Country_Code")
REFERENCES "Coordinates" ("Country_code");

