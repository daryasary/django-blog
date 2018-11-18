# djano-blog
A simple multi language blog engine based on django. This project is a part of [Inprobes](https://inprobes.com) project. Use free forever.

### requirements
* `python 2.7`
* `django 1.11.16`

### How to use
To enable extra admin panel or change its title/header,... should modify this default fields inside your app settings:

```
DEFAULT_BLOG_SETTINGS = {
    'ENABLE_CUSTOM_PANEL': False,
    'ADMIN_PANEL_URL': "^admin/",
    'SITE_HEADER': "Blog administration panel",
    'SITE_TITLE': "Blog panel",
    'INDEX_TITLE': "Welcome to Blog admin panel",
}
```
