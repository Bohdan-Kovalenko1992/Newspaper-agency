from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Redactor, Newspaper


class RedactorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "years_of_experience",
        )


class NewspaperForm(forms.ModelForm):
    publishers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Newspaper
        fields = "__all__"


class RedactorUpdateForm(forms.ModelForm):
    class Meta:
        model = Redactor
        fields = ["first_name", "last_name", "years_of_experience"]


class NewspaperSearchForm(forms.Form):
    title = forms.CharField(
        required=False,
        max_length=255,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by title..."}),
    )


class TopicSearchForm(forms.Form):
    name = forms.CharField(
        required=False,
        max_length=255,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by topic name..."}),
    )


