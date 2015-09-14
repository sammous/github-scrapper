Scrapping Github Profiles
=========================

A quick scrapy project to get profiles of different users based on their programming languages

### Usage

This scrapy project parses the result of a search in github for a specific *location* and *programming language*.
#### Output

* username
* name
* email
* language
* location
* avatar
* date of subscription

#### Proxy list

Do not forget to specify the path of the proxy list `/github_scrapper/list_proxy.txt`


### Database

* The project uses a **MySQL** database named **github**.

* Run the sql file in `/github_scrapper/db/mysql.sql` with the command `source mysql.sql`. 

* Change credentials of your own database in `pipelines.py`. Default is username: **root** password: **root**. 


#### Add a new table

You can add tables associated to a language respecting the syntax :

* users_`language`

### Requirements

* Python
* Scrapy
* MySQL-python
* Twisted

### References

* <https://github.com/aivarsk/scrapy-proxies>
* <http://tangww.com/2013/06/UsingRandomAgent/>
 