from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(u"Хаяг", null=True, unique=True, blank=True, allow_unicode=True, max_length=100)

    class Meta:
        verbose_name_plural = u"Төрлүүд"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("category-detail", kwargs={'pk': self.pk})

class Books(models.Model):

    title = models.CharField(u"Номын нэр", max_length=100)
    author = models.CharField(u"Зохиолч", max_length=50)
    published_date = models.DateField(u"Нийтэлсэн он", auto_now=False, auto_now_add=False)
    description = models.TextField(u"Товч тайлбар", blank=True)
    active = models.BooleanField(u"Төлөв", default=True)
    slug = models.SlugField(u"Хаяг", null=True, unique=True, blank=True, allow_unicode=True, max_length=100)
    volume = models.IntegerField(u"Боть", default=0, blank=True, null=True)
    available_number = models.IntegerField(u"Тоо ширхэг", blank=False, null=False, default=1)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = u"Номнууд"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Books, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("web:book-detail", kwargs={'slug': self.slug})

    # computer = 'Компьютер'
    # philosophy = 'Философи ба сэтгэлзүй'
    # niigem = 'Нийгмийн шинжлэх ухаан'
    # gadaad = 'Хэл шинжлэл'
    # tech = 'Техник технологи'
    # science = 'Байгалийн шинжлэх ухаан'
    # art = 'Урлаг'
    # literature = 'Уран зохиол'
    # geo = 'Түүх газарзүй'
    # CATEGORY_CHOICES = [
    #     ('Компьютер', '000'),
    #     ('Философи ба сэтгэлзүй', '100'),
    #     ('Нийгмийн шинжлэх ухаан', '300'),
    #     ('Хэл шинжлэл', '400'),
    #     ('Байгалийн шинжлэх ухаан', '500'),
    #     ('Техник технологи', '600'),
    #     ('Урлаг', '700'),
    #     ('Уран зохиол', '800'),
    #     ('Түүх газарзүй', '900'),
    # ]
