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
