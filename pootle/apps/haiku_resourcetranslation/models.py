#!/usr/bin/env python

#
# Copyright 2013 Niels Sascha Reedijk, niels.reedijk@gmail.com
# All rights reserved. Distributed under the terms of the MIT License.
#

from django.db import models
from django.utils.translation import ugettext_lazy as _

from pootle_language.models import Language

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

    source_language = models.ForeignKey('pootle_language.Language',
        db_index=True, verbose_name=_('Source Language'))

    root_path = models.FilePathField(editable=False)

