# Bhavcopy Searchified
An application to make BSE's bhavcopy data searchable.

#### Source of Data: [BSE Bhavcopy](https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx)

#### Tech Stack:   

   - Scraping: python-requests and lxml  
   - Backend API: Django & Django Rest Framework  
   - Storage: Redis  
   - Frontend: Vue.js  
   
#### Live at: [http://bhavcopy.swatij.me/](http://bhavcopy.swatij.me/)

### Usage Instruction

* The homepage by default shows the latest BSE stock values for the last working day.
* Start typing a stock name and you will get suggestions in a drop down.
* Click on any of the stock and you can see the results below the search box. These are sorted by date.
* You can also download the result as a CSV by cliking on the 'Download' button there on top right.

#### Search API

You can access the API at: http://bhavcopy.swatij.me/api/

Endpoints:

      * http://bhavcopy.swatij.me/api/record?name=<name_of_stock>&date=<dd-m-yyyy>
      * http://bhavcopy.swatij.me/api/records?name=<name_of_stock>
      * http://bhavcopy.swatij.me/api

### Setup

Note: The setup instructions can be found in the [README](https://github.com/curioswati/bhavcopy-searchified/tree/master#readme).

### Support or Contact

If you want to report the software, need help or want to suggest changes you can [raise an issue](https://github.com/curioswati/bhavcopy-searchified/issues/new) on github.
