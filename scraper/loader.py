import os
import redis
import sys
from csv import reader as CSVReader

from const import CSV_FILENAME_FORMAT
from settings import DATA_DIR

if __name__ == "__main__":

    if len(sys.argv) < 4:
        print('\nPlease provide date in the format: dd mm yyyy\n')
        sys.exit(1)

    # read input date
    date, month, year = sys.argv[1:]

    fulldate = f'{date}-{month}-{year}'

    csv_filename = CSV_FILENAME_FORMAT % (date, month, year[2:])
    csv_filepath = os.path.join(DATA_DIR, 'csv', csv_filename)

    try:
        reader = CSVReader(open(csv_filepath, 'r'), delimiter=',')
    except FileNotFoundError:
        print('\nNo CSV file found for the given date\n')
        sys.exit(1)

    redis_instance = redis.Redis()

    with redis_instance.pipeline() as pipe:

        for row in reader:

            stock_name = row[1].strip()

            # ---- for each stock prepare a set with the dates it has entries ---- #
            # stock_name: {dd1-mm1-yyyy1, dd2-mm2-yyyy2}

            pipe.sadd(stock_name, fulldate)

            # -- create sets of stock_names containing the specific search term -- #
            # term1: {stock_name1, stock_name2}
            # term2: {stock_name1}

            # all substrings from the stock_name starting with the first three letters
            possible_search_terms = [stock_name[:x] for x in range(2, len(stock_name))]

            for term in possible_search_terms:
                pipe.sadd(term, stock_name)

            code = row[0]

            # -- create a hash to store all the data
            # stock_name:date = {'code': xxxxxx, 'open': num, 'high': num, 'low': num, 'close': num}

            pipe.hmset(
                f'{stock_name}:{fulldate}',
                {'code': row[0], 'open': row[4], 'high': row[5],
                 'low': row[6], 'close': row[7]}
            )

            pipe.execute()
            print(row)
