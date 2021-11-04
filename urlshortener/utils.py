from random import choice
from string import ascii_letters, digits

from django.conf import settings

MAX_URL_SIZE = settings.MAX_URL_SIZE   # shorten url 최대 길이
BASE62 = ascii_letters + digits     # base62 문자들


def make_random_path(length=MAX_URL_SIZE, chars=BASE62):
    """
    :param length: 만들 random_path 길이
    :param chars: url에 포함 가능한 문자
    :return: 랜덤 short url
    """
    random_path = [choice(chars) for _ in range(length)]

    return "".join(random_path)


def make_short_url(url_instance):
    """
    :param url_instance: 줄일 url 인스턴스
    :return: shortened url
    """
    short_path = make_random_path()
    instance_class = url_instance.__class__

    while True:
        # 이미 저장된 path 면 다시 생성
        if instance_class.objects.filter(short_url=short_path).exists():
            short_path = make_random_path()
            continue
        # 새로운 path 면 break
        break

    return short_path
