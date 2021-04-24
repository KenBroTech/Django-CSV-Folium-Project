from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from . models import Data


class DataImportExportAdmin(ImportExportModelAdmin):
    list_display = ('country', 'latitude', 'longitude', 'population')


admin.site.register(Data, DataImportExportAdmin)
