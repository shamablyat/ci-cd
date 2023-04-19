from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(CommentModel)
admin.site.register(CommentFromUsers)
admin.site.register(TeamModel)
admin.site.register(DesignModel)
admin.site.register(Design_projectsModel)
admin.site.register(Cat)