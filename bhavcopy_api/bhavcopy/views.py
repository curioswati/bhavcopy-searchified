import redis
from rest_framework.decorators import api_view
from rest_framework.response import Response

redis_instance = redis.Redis()


def get_record_for_keys(keys):
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

        # if we received the key as a result of autocomplete search, it is going to be bytes.
        # need to utf decode it first and extract date
        if not isinstance(key, str):
            key = key.decode('utf-8')
            date = key.split(':')[-1]

        # fetch field:value pairs for the key from the redis hash.
        values = redis_instance.hgetall(key.upper())

        # decode all values(i.e. numbers only, we don't need the field names) and store in a list.
        values_list = [item.decode('utf-8') for item in values.values()]
        values_list.insert(0, date)
        all_values.append(values_list)

    # explicitly putting date in the result, as we don't store it in the hash's data.
    keys = [key.decode('utf-8') for key in values.keys()]
    keys.insert(0, 'date')

    return keys, all_values


@api_view(['GET'])
def get_record(request, *args, **kwargs):
    '''
    Returns all details for one stock record on one given date.
    '''
    code = request.GET.get('code')
    name = request.GET.get('name')
    date = request.GET.get('date')

    item_key = f'{code}:{name}:{date}'

    keys, values = get_record_for_keys([item_key])
    return Response({"name": name, "records": [keys, values]}, status=200)


@api_view(['GET'])
def get_stock_records(request, *args, **kwargs):
    '''
    Returns all details for one stock on all recorded dates.
    '''
    name = request.GET.get('name')

    keys = redis_instance.keys(f'*{name.upper()}*')
    keys, values = get_record_for_keys(keys)

    return Response({"name": name, "records": [keys, values]}, status=200)


@api_view(['GET'])
def autocomplete(request, *args, **kwargs):
    '''
    Return stock names for the input term.
    '''
    term = request.GET.get('term')

    # get all matching keys from redis for the input term.
    keys = redis_instance.keys(f'*{term.upper()}*')

    stock_names = []

    for key in keys:
        name = key.decode('utf-8').split(':')[-2]
        if name not in stock_names:
            stock_names.append(name)

    return Response(stock_names, status=200)
