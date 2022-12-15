from django.contrib import admin
from .models import Test, Category, Question, Answer, Kit


class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'difficulty', )
    list_display_links = ('id', 'title', 'difficulty')
    search_fields = ('title', 'description')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', )


# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ('id', 'description', 'test_id')
#     list_display_links = ('id', 'description', 'test_id')
#     search_fields = ('description', )
#
#
# class AnswerAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'question_id', 'right_false')
#     list_display_links = ('id', 'title', 'question_id', 'right_false')
#     search_fields = ('title', )


admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Kit)
admin.site.register(Test, TestAdmin)
admin.site.register(Category, CategoryAdmin)