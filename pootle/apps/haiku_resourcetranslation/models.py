#!/usr/bin/env python

#
# Copyright 2013 Niels Sascha Reedijk, niels.reedijk@gmail.com
# All rights reserved. Distributed under the terms of the MIT License.
#

import os

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from pootle_language.models import Language
from pootle_store.util import empty_quickstats

class Collection(models.Model):
    """
    A collection is the equivalent to a project, but then for resources (images). A collection is the top-level
    identifier.
    """
    code_help_text = _('A short code for the project. This should only contain '
            'ASCII characters, numbers, and the underscore (_) character.')
    code = models.CharField(max_length=255, null=False, unique=True,
            db_index=True, verbose_name=_('Code'), help_text=code_help_text)

    fullname = models.CharField(max_length=255, null=False,
        verbose_name=_("Full Name"))

    source_language = models.ForeignKey(Language,
        db_index=True, verbose_name=_('Source Language'))

    root_path = models.FilePathField(editable=False)

    def __unicode__(self):
        return self.fullname

    def save(self, *args, **kwargs):
        # TODO: move with code change?
        # Create file system directory if needed
        project_path = os.path.join(settings.RESOURCEDIRECTORY, self.code)

        if not os.path.exists(project_path):
            # will raise an exception if it does not work, so our bases are covered
            os.makedirs(project_path)

        self.root_path = project_path

        super(Collection, self).save(*args, **kwargs)

    def getquickstats(self):
        # TODO: implement properly
        return empty_quickstats


class TranslationCollection(models.Model):
    """
    This class is the equivalent to a translationproject, but then for resources (images).
    """

    class Meta:
        unique_together = ('language', 'collection')

    language = models.ForeignKey(Language, db_index=True)
    collection = models.ForeignKey(Collection, db_index=True)
    real_path = models.FilePathField(editable=False)


# class Resource(models.Model):
#     """
#     A resource is an image that is translatable. Every image is part of a project.
#     """
#     translation_collection = None