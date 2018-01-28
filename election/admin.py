from django.contrib import admin
from election.models import Survey
from import_export import resources
from election.models import Survey, Question
from import_export.admin import ImportExportModelAdmin
from django.dispatch import receiver
from import_export.signals import post_import, post_export

class SurveyResource(resources.ModelResource):

    class Meta:
        model = Survey
        fields = ('name', 'active', 'created_at',)


class SurveyAdmin(admin.ModelAdmin):
    resource_class = SurveyResource
    list_display = ('name', 'active', 'created_at')
    list_filter = ('active',)
    search_fields = ('name',)

admin.site.register(Survey, SurveyAdmin)
"""
@receiver(post_import, dispatch_uid='balabala...')
def _post_import(model, **kwargs):
    # model is the actual model instance which after import
    pass

@receiver(post_export, dispatch_uid='balabala...')
def _post_export(model, **kwargs):
    # model is the actual model instance which after export
    pass"""

class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "survey", "choice_one", "choice_two" )
    search_fields = ("title",)

admin.site.register(Question, QuestionAdmin)
