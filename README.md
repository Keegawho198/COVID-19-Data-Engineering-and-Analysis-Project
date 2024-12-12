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
The data analysis focused on calculating the maximum and minimum occurrences of COVID-19 cases and deaths globally and locally. Key patterns and insights have been identified and briefly highlighted. These findings were visualized using the matplotlib library in the form of a matrix, providing a clear and concise representation of the trends.</br>
The key patterns have been highlighted briefly and visualised in the for of matrix using "plt" library.</br>

These insights are capable to support informed decision-making in public health, resource allocation, and pandemic management, demonstrating the value of clean, well-processed data in addressing real-world challenges.</br>

#### stage 2 (Amrit Kaur)
##### User interaction (Transformation)
After merging the data but before initiating the cleaning process, a user-interactive function was developed. This function allows users to filter the data based on their specific requirements, enabling a more customized and focused analysis.

##### Data segregation and exportation (Load)
The cleaned data from the previous steps was further categorized based on specific criteria. These subsets were then exported into eight separate .csv files for streamlined analysis and reporting.</br>
1. "Countries.csv"
2. "patient database.csv"
3. "COVID_19_Dataset.csv"
4. "Aggregated country statistics"
5. "Australian Statistics.csv"
6. "Global Statistics.csv"
7. "coordinates_df.csv"
8. "Pivot Summary.csv"

#### Stage 3 (Keegan)
##### ERD
![ERD](https://github.com/user-attachments/assets/773100b7-3c1b-4f12-88d1-49e61211c952)

This ERD serves as a blueprint for our database design, helping us understand how data is structured and how different entities interact with each other. This is essential for both documenting existing databases and planning new ones. </br>

PostgreSQL Coding</br>

Data Importation into PostgreSQL</br>

To create the table into the Postgres SQL use the COVID-19-ETL_Tables.sql.

Then, proceed to import the CSV files and use the Retrieve-Data-Statements.sql file to see the output of each table with the CSV files imported.


##### Ethical Considerations

In our project analyzing COVID-19 cases globally, we prioritize ethical considerations by ensuring that all data sourced is obtained through legitimate and transparent means, respecting the privacy and confidentiality of individuals. We reviewed our dataset for any personally identifiable information (PII) and took necessary steps to anonymize it, as it is crucial to protect the identities of those affected by the pandemic. 

Additionally, We aimed to ensure that our analysis represent a diverse population, considering factors such as geographical disparities, to avoid biases or excluding vulnerable groups. By adhering to these ethical principles, we aimed to safeguard the rights of individuals represented in our data.


#### Stage 4 (Patrick Z)
Flask web application that enables users to interact with the data intuitively.

-Create an index.html file  
-Create an app.py file  

Save both files and run the app.py on a browser html (http://127.0.0.1:5000)

![Flask1](https://github.com/user-attachments/assets/36486335-6699-47fc-a51f-7426771a4211)
![Flask2](https://github.com/user-attachments/assets/df3f9048-424f-48f6-aebe-bc1a60bf838d)

Users can search for data by country, or view the results in a pandas DataFrame.


Resources:
Kaggle




