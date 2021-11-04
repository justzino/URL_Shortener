from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from .forms import ShortenerForm
from .models import URLMap


def index_view(request):
    template = 'urlshortener/index.html'
    context = dict()
    context['form'] = ShortenerForm()  # original_url 받아올 ShortenerForm

    if request.method == 'GET':
        # render: httpResponse객체를 반환하는 함수로, template을 context과 엮어 httpResponse로 쉽게 반환
        return render(request, template, context)

    if request.method == 'POST':
        form = ShortenerForm(request.POST)

        # form 을 통해 넘어온 데이터들의 각 field 유효성 검사
        if not form.is_valid():
            # 유효하지 않은 경우
            context['errors'] = form.errors
            return render(request, template, context)

        # original_url 에 대한 중복성 검사
        original_url = form.cleaned_data.get('original_url', None)  # 유효성 검증된 cleaned_data
        url = URLMap.objects.filter(original_url=original_url)
        if url.exists():
            new_url = request.build_absolute_uri('/') + url.first().short_url
            context['new_url'] = new_url
            context['original_url'] = original_url
            return render(request, template, context)

        # 처음 들어온 url 이면 short url 생성후 object 저장
        url_map_object = form.save()  # short url 자동 생성후 저장됨
        new_url = request.build_absolute_uri('/') + url_map_object.short_url
        original_url = url_map_object.original_url
        context['new_url'] = new_url
        context['original_url'] = original_url

        return render(request, template, context)


def redirect_view(request, short_path):
    try:
        shortener = URLMap.objects.get(short_url=short_path)
        shortener.save()

        return HttpResponseRedirect(shortener.original_url)

    # URLMap.DoesNotExist
    except:
        raise Http404('유효하지 않은 url 입니다.')
