# Data Engineering Track  

## Project Overview  
This project focuses on demonstrating a comprehensive understanding of data engineering principles by following a structured workflow involving data extraction, transformation, loading (ETL), and retrieval. The project’s purpose is to design a functional data pipeline that stores and transforms data into meaningful structures, showcasing its usability through accessible output formats.  

## Key Features  
- **Database Integration:**  
  Data is stored in a SQL database using PostgresSQL Platform. 

- **ETL Workflow:**  
  Data is extracted from csv files stored in 'resources' directory, transformed to meet predefined requirements, and loaded into the database.  

- **Data Retrieval:**  
  The project enables data retrieval using a method known as Pandas Dataframe.  

- **Additional Data Engineering Library:**  
  Integration of an advanced library known as'PyArrow' has been used for the data exportation.  

---

## Instructions  
 
- Clone the repository:  
git clone <https://github.com/Keegawho198/COVID-19-Data-Engineering-and-Analysis-Project>
  cd <PANDAS-Jupyter Notebook/COVID-19-ETL-Project.ipynb/></br></br>
and run the code in Pandas Jupyter Notebook.

## Data Engineering process
This data engineering project has been divided in 4 stages.</br>
#### Stage 1 (Mandeep Sohi)
#### Data selection
As a team we decieded to use COVID-19 statistics on a global scale to perform comprehensive data engineering and analysis. 

##### Data importation (Extraction)
This project uses pandas library to read the csv files.</br>
<pre> 
# read the 'countries.csv' files and store into panadas DataFrame
countries_dataset = pd.read_csv("Resources/countries.csv")
countries_dataset.head()</pre>
<pre># read the 'WHO COVID-19 cases.csv' files and store into panadas DataFrame
covid_cases_dataset = pd.read_csv("Resources/WHO COVID-19 cases.csv")
covid_cases_dataset.head()</pre>

##### Data cleaning (Transformation)
The data was cleaned using following steps:

- Rename the common columns for merging process
- Merge the csv file to form a complete dataset
- Drop unnecessary columns
- Handle missing and duplicate data
- Check and adjust datatypes

##### Data Anlysis (Transformation)
The data analysis was archesterated by calculating maximum and minimum COVID-19 cases and deaths (related to it) occurences globally and locally (Autralian Data)</br>
The key patterns have been highlighted briefly and visualised in the for of matrix using "plt" library.</br>

These insights are capable to support informed decision-making in public health, resource allocation, and pandemic management, demonstrating the value of clean, well-processed data in addressing real-world challenges.</br>

#### stage 2 (Amrit Kaur)
##### User interaction (Transformation)
After the data merge and before the cleaning process, a user-interactive function has been developed to provide the user with an opportunity to filter the data based upon their requirement. 

##### Data segregation and exportation (Load)
The cleaned data, from previous steps, has been further divided according to their specifications and exported in the form of eight .csv files:</br>
1. "Countries.csv"
2. "patient database.csv"
3. "COVID_19_Dataset.csv"
4. "Aggregated country statistics"
5. "Australian Statistics.csv"
6. "Global Statistics.csv"
7. "coordinates_df.csv"
8. "Pivot Summary.csv"

#### Stage 3 (Keegan)
ERD
![ERD](https://github.com/user-attachments/assets/773100b7-3c1b-4f12-88d1-49e61211c952)

PostgreSQL Coding
-E
-T
-L

Data Importation into PostgreSQL
Ethical Considerations
#### Stage 4 (Patrick Z)
Final check of the ETL process above
Presentation slides






Resources:
Kaggle




