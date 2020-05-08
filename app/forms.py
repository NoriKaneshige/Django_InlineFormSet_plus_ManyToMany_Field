from django import forms
from .models import Post, Tag


class PostCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Post
        exclude = ('tag',)

# We use inlineformset for tag. When we add new post, tags are listed by inlineformset
TagInlineFormSet = forms.inlineformset_factory(
    Post, Post.tag.through, fields='__all__', can_delete=False
)

# This is easy way of creating a simple form for tag.
TagCreateForm = forms.modelform_factory(Tag, fields='__all__')

# We also use inlineformset for posts. When we add new tag, posts are listed by inlineformset.
PostInlineFormSet = forms.inlineformset_factory(
    Tag, Post.tag.through, fields='__all__', can_delete=False
)