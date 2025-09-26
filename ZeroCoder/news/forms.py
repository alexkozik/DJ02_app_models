from .models import NewsPost
from django import forms
# ModelForm, TextInput, DateTimeInput, Textarea, DateField, DateInput, TimeField, TimeInput
from datetime import datetime




class NewsPostForm(forms.ModelForm):
    # дополнительные поля для формы
    pub_date_date = forms.DateField(
        widget = forms.DateInput(attrs={'type': 'date', 'id': 'date', 'class': 'form-control'}),
    )
    pub_date_time = forms.TimeField(
        widget= forms.TimeInput(attrs={'type': 'time', 'id': 'time', 'class': 'form-control'}),
    )

    class Meta:
        model = NewsPost
        fields = ['title', 'short_description', 'text','author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'header', 'name': 'header', 'placeholder': 'Введите заголовок новости', 'required': 'required'}),
            'short_description': forms.TextInput(attrs={'class': 'form-control', 'id': 'shortDescription', 'name': 'shortDescription',  'placeholder': 'Введите краткое описание новости', 'required': 'required'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'id': 'content', 'name': 'content', 'rows': '5', 'placeholder': 'Напишите полное содержание здесь ...', 'required': 'required'}),
            'author': forms.Select(attrs={'class': 'form-select', 'id': 'author', 'name': 'author'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # если редактируем новость — подставляем существующее значение даты и времени
        if self.instance and self.instance.pub_date:
            self.fields['pub_date_date'].initial = self.instance.pub_date.date()
            self.fields['pub_date_time'].initial = self.instance.pub_date.time().strftime('%H:%M')

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("pub_date_date")
        time = cleaned_data.get("pub_date_time")

        if date and time:
            cleaned_data["pub_date"] = datetime.combine(date, time)
        else:
            # Если дата/время не заданы → ошибка
            raise forms.ValidationError("Нужно указать дату и время публикации")

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.pub_date = self.cleaned_data["pub_date"]
        # print(f"Alex print {instance.pub_date}")
        if commit:
            instance.save()
        return instance

