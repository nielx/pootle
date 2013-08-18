#!/usr/bin/env python

#
# Copyright 2013 Niels Sascha Reedijk, niels.reedijk@gmail.com
# All rights reserved. Distributed under the terms of the MIT License.
#
from django.shortcuts import render_to_response
from django.template import RequestContext
from haiku_resourcetranslation.models import Collection

from pootle_app.views.index.index import getprojects, get_items
from pootle_misc.browser import get_table_headings


def getcollections(request):
    def get_last_action(item):
        return ''

    print get_items(request, Collection, get_last_action, lambda name: name)
    return get_items(request, Collection, get_last_action, lambda name: name)


def collections_index(request):
    """page listing all resource collections. No special permissions required"""

    table_fields = ['collection', 'progress', 'activity']
    table = {
        'id': 'collections',
        'proportional': False,
        'fields': table_fields,
        'headings': get_table_headings(table_fields),
        'items': getcollections(request),
    }

    templatevars = {
        'table': table,
    }

    return render_to_response('collection/collections.html', templatevars,
                              RequestContext(request))
