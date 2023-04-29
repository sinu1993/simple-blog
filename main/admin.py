from django.contrib import admin
from .models import *

admin.site.register(Blog_category)
admin.site.register(Tags)
admin.site.register(Author_category)
admin.site.register(Author)
admin.site.register(Blog)

