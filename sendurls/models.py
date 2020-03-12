from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

from pygments import highlight
from pygments.formatters.html import HtmlFormatter

#LEXERS = [item for item in get_all_lexers() if item[1]]



class Urlinput(models.Model):
    url_input = models.CharField( max_length=100)





# def save(self, *args, **kwargs):
#     options = self.url_input and {'url_input': self.url_input} or {}
#     formatter = HtmlFormatter( full=True, **options)
#     self.highlighted = highlight(self.url_input, formatter)
#     super(Urlinput, self).save(*args, **kwargs)
