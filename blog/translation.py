from __future__ import unicode_literals

from modeltranslation.translator import translator, TranslationOptions
from blog.models import Author


class AuthorTranslationOptions(TranslationOptions):
    fields = ('display_name', )


translator.register(Author, AuthorTranslationOptions)
