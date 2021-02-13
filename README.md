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


### Setup - Development

See the detailed instructions in [Development-Setup](https://github.com/curioswati/bhavcopy-searchified/wiki/Development-Setup) guide.


### Setup - Deployment

* Update the Django secret key in `bhavcopy_api/bhavcopy_api/settings.py` for production.

* build the frontend

      cd frontend
      npm build

This will create a `build/` directory inside the `frontend` which you can directly use on the production.

* collect static files for django to serve    

      cd bhavcopy-api
      python manage.py collectstatic

* For setting up airflow, follow the [Airflow production automation](https://github.com/curioswati/bhavcopy-searchified/wiki/Aifrlow-production-automation) guide.
