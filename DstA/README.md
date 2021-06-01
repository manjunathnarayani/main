 # Project Overview
 Within a scope of Sparkify music streaming app, this project will create a database schema and ETL pipeline that takes data from song data files and log data files in JSON format.It performs the appropriate transformation and loads the data into newly created PosstgreSQl database.
 For this analysis, we used the following:
     1.Create a database design comprising the Fact and Dimensions tables in star schema.
     2.create a ETL process to read the JSON files from two local directories.
     3.Transform the extracted data to appropraite form and load the data into Sparkify database
     
# Resources
Data soruce - 
    /data/song_data
    /data/log_data
    
# Database scehma
The database Sparkify is designed into star schema. This will help analytics team to query the data with ease and efficent and avoiding duplicity, by making joins between Fact and Dimensions tables. This will help getting relevant data like which song , user is listening to.

## Fact Table
    1. songplays - records in log data associated with song plays i.e. records with page NextSong

## Dimension Tables
    1. users - users in the app
    2. songs - songs in music database
    3. artists - artists in music database
    4. time - timestamps of records in songplays broken down into specific units

# Instructions and steps
Run file create_tables.py in command line/terminal. This will create database and table schema
`python create_tables.py`

Run file etl.py in command line/terminal - This has main ETL methods to insert data into table schema.
`python etl.py`

# Result
test.ipynb - this file has a list of tables in select which can be used to test the required data from Facts and Dimension tables.

  