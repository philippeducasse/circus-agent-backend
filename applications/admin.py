from django.contrib import admin

from applications.models import Application


class ApplicationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Application, ApplicationAdmin)
