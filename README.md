# bhavcopy-searchified
An application to make BSE's bhavcopy data searchable.

#### Source of Data: [BSE Bhavcopy](https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx)

#### Tech Stack:   

   - Scraping: python-requests and lxml  
   - Backend API: Django & Django Rest Framework  
   - Storage: Redis  
   - Frontend: Vue.js  
   
#### Live at: [to-do]

(_Note: The setup instructions below assume basic understanding of Pipenv, Django and Vue or in general node environment_).
### Setup - Installation:

* Clone the repository    

      git clone https://github.com/curioswati/bhavcopy-searchified.git

* Create a virtualenv inside the repository root using [Pipenv](https://pipenv.pypa.io/en/latest/)    

      cd bhavcopy-searchified
      pipenv install

* Make sure you have latest [node](https://nodejs.org/en/) and `npm` installed and then run following    

      cd frontend
      npm install


### Setup - Configuration

* Update the Django secret key in `bhavcopy_api/bhavcopy_api/settings.py` for production.
* Create a file in `Scraper/` called `settings.py` and add following:   

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

### Setup - Development Run

* To locally scrape and store the data    

      redis-server
      cd scraper
      python downloader.py dd-mm-yyyy

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
