from .models import QuestionModel, AnswerModel
from django import forms

class QuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionModel
        fields = '__all__'