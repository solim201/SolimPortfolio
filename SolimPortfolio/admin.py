from django.contrib import admin
from .models import Article
from .models import Ressource
from .models import Cours
from .models import Commentaire

# Register your models here.

admin.site.register(Article)
admin.site.register(Cours)
admin.site.register(Commentaire)
admin.site.register(Ressource)