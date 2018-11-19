from __future__ import unicode_literals

from djangoseo import seo


class BasicMetadata(seo.Metadata):
    title = seo.Tag(max_length=68, head=True)
    keywords = seo.KeywordTag()
    description = seo.MetaTag(max_length=155)
    heading = seo.Tag(name="h1")
    subheading = seo.Tag(name="h2")
    extra = seo.Raw(head=True)

    # Adding some fields for facebook (opengraph)
    og_title = seo.MetaTag(
        name="og:title", populate_from="title", verbose_name="facebook title"
    )
    og_description = seo.MetaTag(
        name="og:description", populate_from="description",
        verbose_name='facebook description'
    )
