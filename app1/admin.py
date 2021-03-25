from django.contrib import admin

# Register your models here.
from .models import marks, sci_marks, art_marks, commerce_marks
admin.site.register(marks)
admin.site.register(sci_marks)
admin.site.register(art_marks)
admin.site.register(commerce_marks)