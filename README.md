# Capstone: Diabetes Patient Hospitalization 1999-2008
Cory Chitwood, Keith-Jordan Wilkinson, Kai Gui, and Eddy Doering

## Abstract

As of 2020, diabetes is a disease that afflicts approximately 10% of the US population, and is the 8th leading cause of death.<sup>1, 2</sup> It is not uncommon for patients to be hospitalized due to diabetes or reasons relating to diabetes. Ideally upon discharge from the hospital, a patient would have their major symptoms addressed and be able to manage their disease. However, a few patients will have to be readmitted due to continuing complications, which is associated with unfavorable patient outcomes and high financial costs.<sup>3</sup> In our project, we utilize a dataset of approximately 100,000 anonymized electronic health records (EHR) from hospitilizations of diabetes patients from 1999-2008 compiled by Virginia Commonwealth University researchers from the CERNER Health Facts Database.<sup>4</sup> We First explore and visualize the demographics of diabetes patients represetnted within the dataset, comparing our findings to 2008 national demographics identified from census data.<sup>5</sup> Next, we apply machine learning models to predict if diabetes patients will experience hospital readmission based on features of their original hospital stay. Predictions like these could improve patient outcomes by empowering primary healthcare workers to better identify and monitor at-risk patients.

## References
1. Ahmad FB, Anderson RN. The Leading Causes of Death in the US for 2020. JAMA. 2021;325(18):1829–1830. DOI: [10.1001/jama.2021.5469](http://doi.org/10.1001/jama.2021.5469)
2. Centers for Disease Control and Prevention. National Diabetes Statistics Report, 2020. Atlanta, GA: Centers for Disease Control and Prevention, U.S. Dept of Health and Human Services; 2020. [Link](https://www.cdc.gov/diabetes/data/statistics-report/index.html)
3. McIlvennan CK, Eapen ZJ , Allen LA. Hospital Readmissions Reduction Program. Circulation. 2015;131:1796–1803. DOI: [10.1161/CIRCULATIONAHA.114.010270](doi.org/10.1161/CIRCULATIONAHA.114.010270)
4. Strack B, DeShazo JP, Gennings C, Olmo JL, Ventura S, Cios KJ, Clore JN. Impact of HbA1c Measurement on Hospital Readmission Rates: Analysis of 70,000 Clinical Database Patient Records. Biomed Res Int. 2014:781670. DOI: [10.1155/2014/781670](doi.org/10.1155/2014/781670)
5. U.S. Census Bureau. HIC-9_ACS. Population Without Health Insurance Coverage by Race and Hispanic Origin: 2008 to 2019. Health Insurance Historical Tables - HHI Series. [Link](https://www.census.gov/data/tables/time-series/demo/health-insurance/historical-series/hic.html)

## Repository File Guide:

### Code

* #### Cloud
  * **config_sample.py:** Sample configuration file for included code
  * **datafactory_csv_to_sql.ipynb:** Databricks Notebook. Uses Pyspark and JDBC api to lean and push datalake csv files into SQL databases
  * **kafka_consumer.ipynb:** Databricks Notebook. Saves Kafka messages as csv files into datalake.
  * **kafka_producer.ipynb:** Databricks Notebook. Simulates live streaming data through sending rows of csv file as Kafka messages.
  * **kafka_topic.ipynb:** Create topic for Kafka producer and consumer.
* #### Datasets
  * **2008_race_uninsured_census.csv:** Census Dataset. Population Without Health Insurance Coverage by Race and Hispanic Origin: 2008 to 2019.
  * **diabetic_data.csv:** Diabetes EHR Dataset. Impact of HbA1c Measurement on Hospital Readmission Rates: Analysis of 70,000 Clinical Database Patient Records.

* #### SQL
  * **sample_sql_query_powerbi.sql:** Sample PowerBI SQL query for python visualization
  
* #### Visualizations
  * **python_visualization_powerBI.ipynb:** Jupyter Notebook. Python visualization comparing demographics of Diabetes EHR dataset and US Census Bureau. Includes code to copy/paste into PowerBI PyScript Visualization

### ML Documentation
* **documentation.xlsx:** Tracks optimization of ML models 

### Project Specifications
* **CapstoneERD.drawio.pdf:** SQL Database ERD diagram
* **Data Platform.pdf:** Project Cloud Data diagram
* **Data Sources.pdf:** Annotated biliography of utilized datasets
* **Executive Summary.pdf:** Project summary and proposed questions
* **Project Management Plan.pdf:** Project plan task division and schedule
* **VisualizationsNapkinsandFeedback.pdf:** Proposed visualizations and received feedback
