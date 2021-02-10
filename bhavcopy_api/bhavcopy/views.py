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
    {
        "key1": {
            "field1": "value1",
            "field2": "value2",
        },
        "key2": {
            "field1": "value1",
            "field2": "value2",
        }
    }
    '''
    all_values = {}
    for key in keys:
        if not isinstance(key, str):
            key = key.decode('utf-8')

        values = redis_instance.hgetall(key.upper())
        values = {key.decode('utf-8'): value.decode('utf-8') for (key, value) in values.items()}
        all_values[key] = values
    return all_values


@api_view(['GET'])
def get_record(request, *args, **kwargs):
    '''
    Returns all details for one stock record on one given date.
    '''
    code = request.GET.get('code')
    name = request.GET.get('name')
    date = request.GET.get('date')

    item_key = f'{code}:{name}:{date}'

    values = get_record_for_keys([item_key])
    return Response(values, status=200)


@api_view(['GET'])
def get_stock_records(request, *args, **kwargs):
    '''
    Returns all details for one stock on all recorded dates.
    '''
    name = request.GET.get('name')

    keys = redis_instance.keys(f'*{name.upper()}*')
    values = get_record_for_keys(keys)

    return Response(values, status=200)
