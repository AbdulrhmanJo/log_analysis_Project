# log_analysis_Project
first project in Udacity's full stack web development nanodegree program.
## Getting Started
the task in this project is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.
## Prerequisites
1. install [Python 3](https://www.python.org/download/releases/3.0/)
2. install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
3. install [Vagrant](https://www.vagrantup.com/downloads.html)
4. Download the Udacity [Virtual Machine Configuration](https://d17h27t6h515a5.cloudfront.net/topher/2017/April/58fe3483_fsnd-virtual-machine/fsnd-virtual-machine.zip)
## How to prepare your computer to use and run the tool:
1. Clone this repository:
`$ git clone from https://github.com/AbdulrhmanJo/log_analysis_Project.git`
2. open your tirmenal and make inside vagrant folder by use cd.
3. launch the virtual machine with`vagrant up`
4. after Vagrant installs necessary files use `vagrant ssh` to continue.
5. now the command line start with vagrant. go inside vagrant by use cd into the /vagrant folder.      
6. load the database by type `psql -d news -f newsdata.sql`
7. run the database by type `psql -d news`
8. Use command `news.py` to run the python program that fetches query results.
## Create View
I have created tow view to deal with thired query the first one to collect the total requset and the second to collect the error request 

The first view:

    CREATE VIEW total_status AS SELECT date(time), count(*) AS status 
    FROM log GROUP BY date(time) ORDER BY status DESC;


The Second view:
  
    CREAtE VIEW error_status AS SELECT date(time), count(*) AS error 
    FROM log WHERE log.status = '404 NOT FOUND'
    GROUP BY date(time)
    ORDER BY error desc;
  

## Authors

* **Abdulrhman Aljohani** - [AbdulrhmanJo](https://github.com/AbdulrhmanJo)
