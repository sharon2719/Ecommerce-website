from django.db import models


class Category (models.Model):
    title=models.CharField(max_length=300)
    primary_category=models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Product(models.Model):
    main_image=models.ImageField(upload_to='media/',blank=True)
    name=models.CharField(max_length=300)
    slug=models.SlugField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    preview_text=models.TextField(max_length=300,verbose_name=('Preview Text'))
    detail_text=models.TextField(max_length=1000,verbose_name=('Detail Text'))
    price=models.FloatField()

    def __str__(self):
        return self.name
