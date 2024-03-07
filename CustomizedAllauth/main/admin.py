from django.contrib import admin
from .models import *

# Register your models here.

class BookQuestionAdmin(admin.ModelAdmin):
    search_fields= ['body', 'answer']
    filter_horizontal= ('options', 'correct_options')


class BookQuestionOptionAdmin(admin.ModelAdmin):
    search_fields= ['content']

class ExamQuestionIntermidiateAdmin(admin.ModelAdmin):
    search_fields= ['exam__name']

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)

        # Customize the search behavior for the 'author__name' field
        queryset |= self.model.objects.filter(exam__name__icontains=search_term)

        return queryset, use_distinct

class ExerciseQuestionIntermidiateAdmin(admin.ModelAdmin):
    search_fields= ['exercise__name']
    
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)

        # Customize the search behavior for the 'author__name' field
        queryset |= self.model.objects.filter(exercise__name__icontains=search_term)

        return queryset, use_distinct

admin.site.register(ExamQuestionOptions)
admin.site.register(ExamQuestion)
admin.site.register(Exam)
admin.site.register(ExamQuestionIntermidiate, ExamQuestionIntermidiateAdmin)

admin.site.register(BookQuestionOption, BookQuestionOptionAdmin)
admin.site.register(BookQuestion, BookQuestionAdmin)
admin.site.register(Exercise)
admin.site.register(Chapter)
admin.site.register(Book)
admin.site.register(ExerciseQuestionIntermidiate, ExerciseQuestionIntermidiateAdmin)

admin.site.register(UserSubmittedBookAnswer)
admin.site.register(BookQuestionFeedback)