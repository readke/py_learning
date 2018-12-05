from django.contrib import admin

from .models import Question,Choice
# Register your models here.



class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('disc',               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_data'],'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('id','question_text','pub_data','was_published_recently')
    list_filter = ['pub_data']
    search_fields = ['question_text','pub_data']

admin.site.register(Question,QuestionAdmin)
