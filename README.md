# bhavcopy-searchified
An application to make BSE's bhavcopy data searchable.

#### Source of Data: [BSE Bhavcopy](https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx)

#### Tech Stack:   

   - Scraping: python-requests and lxml  
   - Backend API: Django & Django Rest Framework  
   - Storage: Redis  
   - Frontend: Vue.js  
   
#### Live at: [http://bhavcopy-searchified.herokuapp.com/](http://bhavcopy-searchified.herokuapp.com/)

#### Search API

You can access the API at: http://bhavcopy.swatij.me/api/

Endpoints:

      * http://bhavcopy.swatij.me/api/record?name=<name_of_stock>&date=<dd-m-yyyy>
      * http://bhavcopy.swatij.me/api/records?name=<name_of_stock>
      * http://bhavcopy.swatij.me/api

(_Note: The setup instructions below assume basic understanding of Pipenv, Django and Vue or in general node environment_ and are specific to ubuntu based environments).
### Setup - Installation:

* Update the system     

      sudo apt-get update
      
* Install base dependencies

      sudo apt-get install python3-dev python-pip
      sudo pip install pipenv
      
* Redis installation: https://redis.io/topics/quickstart

      wget http://download.redis.io/redis-stable.tar.gz
      tar xvzf redis-stable.tar.gz
      cd redis-stable
      make
      make install
      sudo mkdir /etc/redis
      sudo mkdir /var/redis
      sudo cp utils/redis_init_script /etc/init.d/redis_6379
      sudo cp redis.conf /etc/redis/6379.conf
      sudo mkdir /var/redis/6379

* Clone the repository    

      git clone https://github.com/curioswati/bhavcopy-searchified.git

* Create a virtualenv inside the repository root using [Pipenv](https://pipenv.pypa.io/en/latest/) and install requirements   

      cd bhavcopy-searchified
      pipenv install

* Make sure you have latest [node](https://node.dev/node-binary) and `npm` installed and then run following    

      cd frontend
      npm install

### Setup - Configuration

* Create a file `scraper/settings.py` and add following:

      HOME_URL = https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx
      DATA_DIR = /path/to/data/directory     # This should be the path of the location where you want to store the data, appended with the name 'data'.
      REQUEST_HEADERS = {
         'User-Agent': '<Your User Agent>',
         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
         'Accept-Language': 'en-US,en;q=0.5',
         'Referer': 'https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx',
         'Connection': 'keep-alive',
         'Upgrade-Insecure-Requests': '1',
         'Cache-Control': 'max-age=0',
         'TE': 'Trailers',
      }

* Create a file `.env` in the current directory i.e. repository root and add following

      AIRFLOW_HOME=airflow
      AIRFLOW_ADMIN=<username-for-airflow-admin>
      AIRFLOW_ADMIN_FNAME=<Firstname for airflow admin>
      AIRFLOW_ADMIN_LNAME=<Lastname for airflow admin>
      AIRFLOW_ADMIN_EMAIL=<admin email for airflow>
      SCRAPER_DATA_DIR=/path/to/data   # same as set in scraper/settings.py

* After creating the above file, deactivate the env and reactivate

      exit
      pipenv shell

* Redis: update /etc/redis/6379.conf

      daemonize yes
      logfile /var/log/redis_6379.log
      dir /var/redis/6379

### Setup - Development

See the detailed instructions in [Development-Setup](https://github.com/curioswati/bhavcopy-searchified/wiki/Development-Setup) guide.


### Setup - Deployment

See the detailed instructions in [Production-Setup](https://github.com/curioswati/bhavcopy-searchified/wiki/Production-Setup) guide.
