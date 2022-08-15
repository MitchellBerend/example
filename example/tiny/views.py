from datetime import datetime
import json

from django.shortcuts import render
from django.http.response import (
        JsonResponse,
        HttpResponse,
        HttpResponseRedirect,
    ) 

from .models import Redirect


def shorten_post(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        response = HttpResponse('Body is not valid json')
        response.status_code=400

        return response
    

    # quick json validation
    if 'url' not in data:
        response = HttpResponse('Url not present')
        response.status_code=400
        return response

    if 'shortcode' in data and len(data.get('shortcode', '1')) != 6:
        response = HttpResponse('The provided shortcode is invalid')
        response.status_code=409
        return response

    if 'shortcode' in data and Redirect.objects.filter(shortcode=data.get('shortcode')).exists():
        response = HttpResponse('Shortcode already in use')
        response.status_code=409
        return response
    
    shortcode =  data.get('shortcode', Redirect.generate_random_shortcode())
    redirect = Redirect(url=data.get('url'), shortcode=shortcode)
    redirect.save()

    response = JsonResponse(data={
        'shortcode': redirect.shortcode,
    })
    response.status_code = 201

    return response


def short_code_get_stats(request, short_code):
    redirect = Redirect.objects.filter(shortcode=short_code)
    if redirect.exists():
        redirect = redirect[0]
        last_accessed_date = redirect.last_accessed_date or redirect.created_date
        response = JsonResponse(
            data={
                'created': redirect.created_date.strftime('%Y-%m-%dT%H:%M:%sZ'),
                'lastRedirect': last_accessed_date.strftime('%Y-%m-%dT%H:%M:%sZ'),
                'redirectCount': redirect.redirect_count,
            }
        )
        response.status_code = 200
    else:
        response = HttpResponse('Shortcode not found')
        response.status_code = 404

    return response


def short_code_get(request, short_code):
    redirect = Redirect.objects.filter(shortcode=short_code)
    if redirect.exists():
        redirect = redirect[0]
        redirect.redirect_count += 1
        redirect.last_accessed_date = datetime.now()
        redirect.save()
        response = HttpResponseRedirect(redirect.url)
    else:
        response = HttpResponse('Shortcode not found')
        response.status_code = 404

    return response
