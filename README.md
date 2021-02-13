# bhavcopy-searchified
An application to make BSE's bhavcopy data searchable.

#### Source of Data: [BSE Bhavcopy](https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx)

#### Tech Stack:   

   - Scraping: python-requests and lxml  
   - Backend API: Django & Django Rest Framework  
   - Storage: Redis  
   - Frontend: Vue.js  
   
#### Live at: [to-do]

(_Note: The setup instructions below assume basic understanding of Pipenv, Django and Vue or in general node environment_ and are specific to ubuntu based environments).
### Setup - Installation:

* Update the system     

      sudo apt-get update
      
* Clone the repository    

      git clone https://github.com/curioswati/bhavcopy-searchified.git

* Create a virtualenv inside the repository root using [Pipenv](https://pipenv.pypa.io/en/latest/) and install requirements   

      cd bhavcopy-searchified
      pipenv install

* Make sure you have latest [node](https://nodejs.org/en/) and `npm` installed and then run following    

      cd frontend
      npm install


### Setup - Configuration

* Update the Django secret key in `bhavcopy_api/bhavcopy_api/settings.py` for production.
* Create a file in `Scraper/` called `settings.py` and add following:   

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

* initialize `airflow`     

      . scheduler/init_airflow.sh
      
* It should create a directory named `airflow` in the current directory, inside that is `airflow.cfg`, open it and edit the following variable

      dags_folder = /path/to/scheduler/tasks

* If you do not want to manage the crawling with `airflow` then create the following directories in the path set in `scraper/settings.py`     

      mkdir -p data/zip data/csv
      
### Setup - Development Run

* To locally scrape and store the data    

      redis-server
      cd scraper
      python downloader.py dd mm yyyy
      python extractor.py dd mm yyyy
      python loader.py dd mm yyyy

* Start Vue   

      cd frontend
      npm run serve
      npm run watch (optionally in a separate terminal to live reload the changes)

* Start Django    

      cd bhavcopy_api
      python manage.py runserver

The App should be live on `localhost: 8000`.

### Setup - Production

* build the frontend

      cd frontend
      npm build

This will create a `build/` directory inside the `frontend` which you can directly use on the production.

* collect static files for django to serve    

      cd bhavcopy-api
      python manage.py collectstatic

### Setup- Deployment

TODO
