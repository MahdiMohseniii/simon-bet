# exam/forms.py
from django import forms
from .models import Answer

class AnswerForm(forms.Form):
    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question', None)
        super().__init__(*args, **kwargs)
        if question:
            self.fields['answer'] = forms.ChoiceField(
                choices=[(a.id, a.text) for a in question.answer_set.all()],
                widget=forms.RadioSelect
            )
