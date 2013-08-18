#!/usr/bin/env python

#
# Copyright 2013 Niels Sascha Reedijk, niels.reedijk@gmail.com
# All rights reserved. Distributed under the terms of the MIT License.
#

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('haiku_resourcetranslation.views',
    # Listing of all collections
    (r'^$',
        'collections_index'),

    # Specific collection
    url(r'^(?P<collection_code>[^/]*)/?$',
        'collection_language_index', name='collection.overview'),

)
