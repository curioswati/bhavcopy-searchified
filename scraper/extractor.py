import os
import sys
from zipfile import ZipFile

from const import CSV_FILENAME_FORMAT, ZIP_FILENAME_FORMAT
from settings import DATA_DIR

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print('\nPlease provide date in the format: dd mm yyyy\n')
        sys.exit(1)

    # read input date
    date, month, year = sys.argv[1:]

    zip_name = ZIP_FILENAME_FORMAT % (date, month, year[2:])
    zip_path = os.path.join(DATA_DIR, 'zip', zip_name)

    if not os.path.exists(zip_path):
        print('\nNo zip file found for the given date\n')
        sys.exit(1)

    # ----------- exit if already extracted --------------- #

    # Here we assume that all our zip has only one CSV file with a particular name format
    filename = CSV_FILENAME_FORMAT % (date, month, year[2:])
    filepath = os.path.join(DATA_DIR, 'csv', filename)
    if os.path.exists(filepath):
        print(f'\nAlready extracted {zip_name}, exiting...\n')
        sys.exit(0)

    # ------------- Read the zip and extract CSV file --------- #

    # Ref: https://www.geeksforgeeks.org/working-zip-files-python/
    with ZipFile(zip_path, 'r') as zipfile:
        for name in zipfile.namelist():
            zipfile.extract(name, os.path.join(DATA_DIR, 'csv'))
            print(filename)

    print('Done!')
