# Amazon RedShift Data Werehouse

## Summary
* [Introduction](#Introduction)
* [Project Description](#Project-Description)
* [Getting Started](#Getting-Started)
* [Database Schema](#Database-Schema)
* [Prerequisites](#Prerequisites)
* [Installing](#Installing)
* [Running the tests](#Running-the-tests)
* [Built With](#Built-With)
* [Contributing](#Contributing)
* [Authors](#Authors)
* [License](#License)
* [Acknowledgments](#Acknowledgments)

## Introduction

Sparkify is a music streaming startup that provides free and paid on cloud music streaming plans and there are trying to enquire more users with paid plans. So they need to move from a local postgress analytic data wharehouse to a cloud based anlytics process using Amazon Redshift so that they can be more flexible on the of analyse  their users behavior and how to convert them to paid customers.

## Project Description

The Sparkify currently have a on premisse postgress data werehouse and they want to move there analytics process to the cloud. so they will need to move  there song and log data using  json files to a amazon S3 storage service as a staging area and after that  load on a redshift databese for futher analysis.

### Getting Started
#### Run Python scripts below

create_tables.py: Clean previous schema and creates tables.
sql_queries.py: All queries used in the ETL pipeline.
etl.py: Read JSON logs and JSON metadata and load the data into generated tables.

### Database Schema
  <img src="ERD.png">
  
### Prerequisites

AWS accout provisioned with redshift database instance, S3 bucket,  and IAM role with admin level access to connect a redshift cluster and perform above listed operations.
and python 3.x, (local or cloud based) to run the scripts.

### Installing
Use the etl.ipynd notebook to develop the ETL process for each of tables before completing running the  etl.py file to load the whole datasets to a redshift database.

Each time you run the cells above, remember to restart this notebook to close the connection to your database. Otherwise, you won't be able to run your code in create_tables.py, etl.py, or etl.ipynb files since you can't make multiple connections to the same database.

### Running the tests
Test by running create_tables.py and checking the table schemas on your redshift database. You can use Query Editor in the AWS Redshift console for that.


### Built With

* [Amazon Redshift](https://console.aws.amazon.com/redshift/home?region=us-east-1) - Amazon Cloud Based Database Management System.
* [Amazon IAM ](https://console.aws.amazon.com/iam/home?region=us-east-1) -  Amazon Identity and Access Management System
* [S3 buckets](https://s3.console.aws.amazon.com/s3/home?region=us-east-1#) - Amazon storage service
* [Python](https://www.python.org/) - Scripting Language

### Contributing
* **Teofilo Carlos Chichume ** 


### Authors

* **Teofilo Carlos Chichume** - *Initial work* - [nhatofo](https://github.com/nhatofo/redshiftdw_ud.git)


### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

### Acknowledgments

* Inspiration [AWS Documentation](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_TABLE_NEW.html),
[PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)


