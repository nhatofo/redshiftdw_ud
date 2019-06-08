# Data Modeling with Postgres

## Introduction

Sparkify is a music streaming startup that provides free and paid on cloud music streaming plans and there are trying to enquire more users with paid plans. So they need any analytic data wharehouse so that they can learn more about their users and how to convert them to paid customers.



## Project Description

Currently, Sparkify is storing there data on json format which is very deficult to extract insights from. So as solution for the need, they dicided to implement a data wharehouse to support their data analytics process sinse the data still grouying and ramain on silos. so they will need to extract the data from json files, transform and load on a postgress data wherehouse for futher analysis.

### Getting Started
#### Run Python scripts below

create_tables.py: Clean previous schema and creates tables.
sql_queries.py: All queries used in the ETL pipeline.
etl.py: Read JSON logs and JSON metadata and load the data into generated tables.

### Database Schema
  <img src="ERD.png">
  
### Prerequisites

AWS accout provisioned with postgress database instance and python 3.x installed on doker  or linux Ubuntu 14.04 or above

### Installing
Use the etl.ipynd notebook to develop the ETL process for each of tables before completing running the  etl.py file to load the whole datasets.

Each time you run the cells above, remember to restart this notebook to close the connection to your database. Otherwise, you won't be able to run your code in create_tables.py, etl.py, or etl.ipynb files since you can't make multiple connections to the same database (in this case, sparkifydb).

### Running the tests
To test if the etl job run as pretended use the test.ipynd notebook which contein a serie off sql statements to verify the efectiveness of 
the etl process.



### Built With

* [Postgress](https://www.postgresql.org/) - Database Management System
* [Python](https://www.python.org/) - Scripting Language

### Contributing
* **Teofilo Carlos Chichume ** 


### Authors

* **Teofilo Carlos Chichume** - *Initial work* - [nhatofo](https://github.com/nhatofo/udacity_de.git)


### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

### Acknowledgments

* Inspiration [yuralim](https://github.com/yuralim/udacity_dend_project1),
[PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)


