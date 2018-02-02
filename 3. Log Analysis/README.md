# Log Analysis

The project is a collection of queries to analysis the database and produce reports

### Technologies Used :
* Python 3
* PostgreSQL

### The Database consist of 3 tables as following:
  * The **authors** table includes information about the authors of articles.
  * The **articles** table includes the articles.
  * The **log** table includes one entry for each time a user has accessed the site indicates whether the request succeeded or failed.
 
### The views used in this project:
  * The **articles_views** is used to have the articles and it's view count, created as following:
      ```
      CREATE OR REPLACE VIEW articles_views AS
             (SELECT slug as id, COUNT(path) AS views
             FROM articles
             LEFT JOIN log ON slug = substring(path from 10)
             GROUP BY slug);
      ```

### The project consist of 3 main functions as following:
  * The **get_top_articles** to get the top 3 articles in number of views.
  * The **get_top_authors** to get the authors ordered by the number of the views of their articles.
  * The **get_requests_fail_days** to get the days on which the requests lead to more than 1% errors.

### How to run the project:
  1. You should have the Postgresql installed on your machine download it from [here](https://www.postgresql.org/download/).
  2. You need to create a database and the 3 tables and the view download this [archieve](https://github.com/EslamTK/Log-Analysis/blob/master/newsdata.zip) extract the sql file which contains the statements for creating the tables then execute the create view statement.
  3. You need to have python 3 installed download from [here](https://www.python.org/downloads/).
  4. From the command line cd to the project location and run "python3 main.py".
