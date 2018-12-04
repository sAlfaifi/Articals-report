# ArticalsReoprt

Articals Reoprt is a reporting tool that help you understand what are
the most articles that the users like
you can get a statics about:
- What are the most popular three articles of all time?
- Who are the most popular article authors of all time?
- On which days did more than 1% of requests lead to errors?

The database used in this project is PostgreSQL
database scheme nams : news
there are 3 tables in new scheme :
1- authors : contains an author information, columns are (name, bio, id)
2- articles : contains an articles info (), columns are (authos, title, slug, lead, body, time, id)
3- log : contains the requests (succeed, failed), columns are (path, ip, method, status, time, id)

python file contain only on one method "main method" that connect to the db and execute
three queries the print the final result.
all variables written in lowerCamelCase

#project requirments
you have to download the following :
- PostgreSQL v9.5.14
- Python3
- VirtualBox v5.1.38
- Psycopg2 v2.7.5
- Vagrant v2.2.0


#setup
first download and unzip ArticlesReport.zip
you have now a floder named ArticlesReport and inside this folder there are two files :
1- report.py
2- README.md

now move the vagrant file into ArticlesReport folder open the terminal inside that folder
then run this command :
vagerant up
and white until finish downloading.

before you can run report.py, you have to download and unzip newsdata.zip
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
then copy newsdata.sql into ArticlesReport folder
to import the data from newsdata.sql file
open the terminal and cd to the project folder and run these commands :
vagerant up
psql -d news -f newsdata.sql
now data is ready

to see these statics you have to run this file report.py
you can run file through python3:
python3 report.py

after run the command you have to get the following result:
1- The most popular three articles of all time
"Candidate is jerk, alleges rival" - 338647 views
"Bears love berries, alleges bear" - 253801 views
"Bad things gone, say good people" - 170098 views
--------------- end of report -----------------


2- The most popular article authors of all time
Ursula La Multa - 507594 views
Rudolf von Treppenwitz - 423457 views
Anonymous Contributor - 170098 views
Markoff Chaney - 84557 views
--------------- end of report -----------------


3- The days with more than 1% of errors requests
2016-07-17 - 2.26% errors
--------------- end of report -----------------
