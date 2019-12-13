from django.contrib import admin
from .models import QuestionModel, AnswerModel, CategoryModel, UserModel
# Register your models here.

admin.site.register(QuestionModel)
admin.site.register(AnswerModel)
admin.site.register(CategoryModel)
admin.site.register(UserModel)