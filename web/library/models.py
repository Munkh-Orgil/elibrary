from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Books(models.Model):
    title = models.CharField(u"Номын нэр", max_length=50)
    author = models.CharField(u"Зохиолч", max_length=50)
    published_date = models.DateField(u"Нийтэлсэн он", auto_now=False, auto_now_add=False)
    description = models.TextField(u"Товч тайлбар")
    active = models.BooleanField(u"Төлөв", default=True)
    slug = models.SlugField(u"Хаяг", null=True, unique=True, blank=True, allow_unicode=True)
    volume = models.IntegerField(u"Боть", default=0, blank=True, null=True)
    class_number = models.IntegerField(u"Ангилалын дугаар", blank=False, null=True)
    available_number = models.IntegerField(u"Тоо ширхэг", blank=False, null=False, default=1)


    class Meta:
        verbose_name_plural = u"Номнууд"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Books, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("web:book-detail", kwargs={'slug': self.slug})

