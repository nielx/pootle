#!/usr/bin/env python

#
# Copyright 2013 Niels Sascha Reedijk, niels.reedijk@gmail.com
# All rights reserved. Distributed under the terms of the MIT License.
#
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from haiku_resourcetranslation.models import Collection
from pootle.i18n.gettext import ungettext

from pootle_app.views.index.index import getprojects, get_items
from pootle_misc.browser import get_table_headings
from pootle_project.views import make_language_item


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


def collection_language_index(request, collection_code):
    """page listing all languages added to the resource collection"""
    collection = get_object_or_404(Collection, code=collection_code)

    # TODO: check permission for editing
    # can_edit = check_permission('administrate', request)

    translation_collections = collection.translationcollection_set.all()

    items = {}

    table_fields = ['name']  # TODO: more, 'progress', 'total', 'need-translation', 'activity']
    table = {
        'id': 'collection',
        'proportional': False,
        'fields': table_fields,
        'headings': get_table_headings(table_fields),
        'items': items,
    }

    templatevars = {
        'collection': {
            'code': collection.code,
            'name': collection.fullname,
        },
        'table': table,
    }

#    if can_edit:
#       from pootle_project.forms import DescriptionForm
#        templatevars['form'] = DescriptionForm(instance=project)

    return render_to_response('collection/collection.html', templatevars,
                              context_instance=RequestContext(request))

