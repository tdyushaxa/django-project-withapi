from django import forms
from projects.models import Project, Review


class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description', 'tags', 'image',
                  'source_link', 'demo_link', 'vote_total', 'vote_ratio')
        widgets = {
            'tags': forms.CheckboxSelectMultiple
        }


class CommentCreationForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('value', 'body')


class EditReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('value', 'body')
