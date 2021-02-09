import sys
from csv import reader as CSVReader
from io import BytesIO, TextIOWrapper
from zipfile import ZipFile

import requests
from const import COPY_TYPE, SUBMIT_KEY
from lxml import etree
from settings import HOME_URL, REQUEST_HEADERS
from xpaths import EQUITY_LINK_XPATH, INPUT_XPATH

if __name__ == "__main__":

    if len(sys.argv) < 4:
        print('''\nPlease provide date(dd), month(mm), year(yyyy)
              \rNote: if date and month are single digits then put single digits only.\n''')
        sys.exit(1)

    # read input date
    date, month, year = sys.argv[1:]

    # - setup request session, we use it throughout all subsequent requests -- #
    session = requests.Session()

    # --------- collect parameters for bhavcopy request ---------------------- #

    response = session.get(HOME_URL, headers=REQUEST_HEADERS)
    dom = etree.HTML(response.text)
    viewstate_params = dom.xpath(INPUT_XPATH)

    params = {}

    for item in viewstate_params:
        name, value = item.get('name'), item.get('value')
        params[name] = value

    params['ctl00$ContentPlaceHolder1$Debt'] = COPY_TYPE
    params['ctl00$ContentPlaceHolder1$fdate1'] = date
    params['ctl00$ContentPlaceHolder1$fmonth1'] = month
    params['ctl00$ContentPlaceHolder1$fyear1'] = year
    params['ctl00$ContentPlaceHolder1$btnSubmit'] = SUBMIT_KEY
    params['ctl00$ContentPlaceHolder1$DDate'] = f'{year}-{date}-{month}'

    # ----- request the equity file links and extract zip file link ---------- #

    api_response = session.post(HOME_URL, data=params, headers=REQUEST_HEADERS)
    api_dom = etree.HTML(api_response.text)
    equity_link = api_dom.xpath(EQUITY_LINK_XPATH)[0].get('href')

    # ---- request the zip file, extract files and read the required CSV ----- #

    bhavcopy_zip_resp = session.get(equity_link, headers=REQUEST_HEADERS)

    if len(date) < 2:
        date = f"0{date}"
    if len(month) < 2:
        month = f"0{month}"
    FILENAME = f'EQ{date}{month}{year[2:]}.CSV'

    # Ref: https://stackoverflow.com/a/66003133/3860168
    zip_ref = ZipFile(BytesIO(bhavcopy_zip_resp.content))

    with zip_ref.open(FILENAME) as file_contents:
        reader = CSVReader(TextIOWrapper(file_contents, 'utf-8'), delimiter=',')
        for row in reader:
            print(row)
