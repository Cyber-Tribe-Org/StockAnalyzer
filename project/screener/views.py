from django.core.cache import cache
from django.http import HttpResponse

def test_redis(request):
    cache.set('my_key', 'Hello Redis!', timeout=40)
    value = cache.get('my_key')

    return HttpResponse(f'The value is: {value}')