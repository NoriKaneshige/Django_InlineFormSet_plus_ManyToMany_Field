# Django_InlineFormSet_plus_ManyToMany_Field


[referred blog](https://narito.ninja/blog/detail/33/)

![inlineformset-plus-manytomany-fi](inlineformset-plus-manytomany-fi.gif)

> ## models.py
``` python
from django.db import models
from django.utils import timezone

class Tag(models.Model):
    name = models.CharField('Tag Name', max_length=30)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField('Title', max_length=200)
    text = models.TextField('Content')
    date = models.DateTimeField('Date', default=timezone.now)
    tag = models.ManyToManyField(Tag, verbose_name='Tag', blank=True)

    def __str__(self):
        return self.title
```

> ## forms.py
``` python
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
```


> ## views.py
``` python

```

> ## urls.py
``` python

```

> ## admin.py
``` python

```

> ## post_form.html
``` python

```
