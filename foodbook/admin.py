from django.contrib import admin

from foodbook.models import Image
from foodbook.models import Restaurant
from foodbook.models import UserProfile
from foodbook.models import Tag


admin.site.register(Image)
admin.site.register(Restaurant)
admin.site.register(UserProfile)
admin.site.register(Tag)
