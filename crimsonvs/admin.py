from django.contrib import admin

# Register your models here.

from crimsonvs.models import User, Card, Deck, Gallery

admin.site.register(User)
admin.site.register(Card)
admin.site.register(Deck)
admin.site.register(Gallery)
