from datetime import datetime, timedelta

import redis
from rest_framework.decorators import api_view
from rest_framework.response import Response

redis_instance = redis.Redis()


def get_record_for_stocks(keys):
    '''
    Given a list of keys,
    Returns all field:value pairs for those keys.

    Input:
    [key1, key2]

    Output:
    [
            "date",
            "open",
            "high",
            "low",
            "close",
    ],
    [
            "dd-mm-yyyy",
            "value1",
            "value2",
            "value3",
            "value4",
    ]
    '''
    all_values = []

    for key in keys:

        if isinstance(key, bytes):
            key = key.decode('utf-8')

        date = key.split(':')[-1]

        # fetch field:value pairs for the key from the redis hash.
        values = redis_instance.hgetall(key)

        # decode all values(i.e. numbers only, we don't need the field names) and store in a list.
        values_list = [item.decode('utf-8') for item in values.values()]
        values_list.insert(0, date)
        all_values.append(values_list)

    # explicitly putting date in the result, as we don't store it in the hash's data.
    keys = [key.decode('utf-8') for key in values.keys()]
    keys.insert(0, 'date')

    return keys, all_values


def get_record_for_dates(keys):
    '''
    Given a list of keys,
    Returns all field:value pairs for those keys.

    Input:
    [key1, key2]

    Output:
    [
            "name",
            "open",
            "high",
            "low",
            "close",
    ],
    [
            "name1",
            "value1",
            "value2",
            "value3",
            "value4",
    ]
    '''
    all_values = []

    for key in keys:

        if isinstance(key, bytes):
            key = key.decode('utf-8')

        name = key.split(':')[0]

        # fetch field:value pairs for the key from the redis hash.
        values = redis_instance.hgetall(key)

        # decode all values(i.e. numbers only, we don't need the field names) and store in a list.
        values_list = [item.decode('utf-8') for item in values.values()]
        values_list.insert(0, name)
        all_values.append(values_list)

    # explicitly putting date in the result, as we don't store it in the hash's data.
    keys = [key.decode('utf-8') for key in values.keys()]
    keys.insert(0, 'name')

    return keys, all_values


@api_view(['GET'])
def get_record(request, *args, **kwargs):
    '''
    Returns all details for one stock record on one given date.
    '''
    name = request.GET.get('name')
    name = name.upper()
    date = request.GET.get('date')

    item_key = f'{name}:{date}'

    keys, values = get_record_for_stocks([item_key])
    return Response({"name": name, "records": [keys, values]}, status=200)


@api_view(['GET'])
def get_stock_records(request, *args, **kwargs):
    '''
    Returns all details for one stock on all recorded dates.
    '''
    name = request.GET.get('name')
    name = name.upper()

    dates = redis_instance.smembers(f'{name}')

    # sort the dates
    dates = sorted(dates, key=lambda date: datetime.strptime(date.decode('utf-8'), '%d-%m-%Y'))

    keys = [f"{name}:{date.decode('utf-8')}" for date in dates]
    keys, values = get_record_for_stocks(keys)

    return Response({"name": name, "records": [keys, values]}, status=200)


@api_view(['GET'])
def get_latest_records(request, *args, **kwargs):
    '''
    Returns all details for all the stocks latest available.
    '''
    now = datetime.now()
    day = now.weekday()

    # If it's weekend
    if day in [5, 6]:

        # We show last friday's records
        date = now + timedelta(days=(4-day))

    # If it's monday
    elif day == 0:

        # We show last friday's records
        date = now + timedelta(days=-3)

    else:

        # We show yesterday's records
        date = now - timedelta(days=1)

    date = datetime.strftime(date, '%d-%m-%Y')

    keys = redis_instance.keys(f'*{date}*')

    # if no records for the given date.
    if not keys:
        data = {"name": '', "records": []}
    else:
        keys, values = get_record_for_dates(keys[:20])
        data = {"name": '', "records": [keys, values]}

    return Response(data, status=200)


@api_view(['GET'])
def autocomplete(request, *args, **kwargs):
    '''
    Return stock names for the input term.
    '''
    term = request.GET.get('term')

    # get all matching keys from redis for the input term.
    stock_names = redis_instance.smembers(f'{term.upper()}')

    stock_names = [name.decode('utf-8') for name in stock_names]

    return Response(stock_names, status=200)
