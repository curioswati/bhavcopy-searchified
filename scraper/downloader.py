import os
import sys

import requests
from const import COPY_TYPE, SUBMIT_KEY, ZIP_FILENAME_FORMAT
from lxml import etree
from settings import DATA_DIR, HOME_URL, REQUEST_HEADERS
from xpaths import EQUITY_LINK_XPATH, INPUT_XPATH

if __name__ == "__main__":

    if len(sys.argv) < 4:
        print('\nPlease provide date in the format: dd mm yyyy\n')
        sys.exit(1)

    # read input date
    date, month, year = sys.argv[1:]

    filename = ZIP_FILENAME_FORMAT % (date, month, year[2:])
    filepath = os.path.join(DATA_DIR, 'zip', filename)

    if os.path.exists(filepath):
        print('\n Data already downloaded, exiting...\n')
        sys.exit(0)

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
    params['ctl00$ContentPlaceHolder1$fdate1'] = date.lstrip('0')  # strip zero from the beginning
    params['ctl00$ContentPlaceHolder1$fmonth1'] = month.lstrip('0')  # strip zero from beginning
    params['ctl00$ContentPlaceHolder1$fyear1'] = year
    params['ctl00$ContentPlaceHolder1$btnSubmit'] = SUBMIT_KEY
    params['ctl00$ContentPlaceHolder1$DDate'] = f'{year}-{date}-{month}'

    # ----- request the equity file links and extract zip file link ---------- #

    api_response = session.post(HOME_URL, data=params, headers=REQUEST_HEADERS)
    api_dom = etree.HTML(api_response.text)
    equity_link_elem = api_dom.xpath(EQUITY_LINK_XPATH)

    if equity_link_elem:
        equity_link = equity_link_elem[0].get('href')

        # ---- request the zip file and save it to disk ------------------- #

        bhavcopy_zip_resp = session.get(equity_link, headers=REQUEST_HEADERS)

        with open(filepath, 'wb') as zip_file:
            zip_file.write(bhavcopy_zip_resp.content)

        print(f'Downloaded {filename}')
    else:
        print(f'Failed to get the link for zip, response: {api_response.text}')
