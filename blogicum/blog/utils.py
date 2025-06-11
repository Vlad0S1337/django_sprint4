from django.core.paginator import Paginator


def get_paginator(request, queryset,
                  number_of_pages=10):
    paginator = Paginator(queryset, number_of_pages)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)
