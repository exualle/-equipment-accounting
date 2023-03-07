from django.db import models

# Create your models here.
class ItemModel(models.Model):
    YEAR_IN_SCHOOL_CHOICES = [
        ('OWNER', 'Собственность самой организации'),
        ('OTHER', 'Сторонний офис'),
    ]
    equipment_type = models.CharField(max_length=256)
    manufacturer = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    price = models.IntegerField()
    owner = models.CharField(max_length=256, default='')
    belonging = models.CharField(max_length=256)
    number = models.IntegerField()
    date_in = models.DateField()
    date_out = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Оборудование"
        verbose_name_plural = "Оборудование"


class ItemRelationModel(models.Model):
    from_item = models.ForeignKey(ItemModel, models.CASCADE, related_name='equipment')
    to_item = models.ForeignKey(ItemModel, models.CASCADE, related_name='to')

    def __str__(self):
        return f"{self.from_item} - {self.to_item}"

    class Meta:
        verbose_name = "Связь элементов"
        verbose_name_plural = "Связи элементов"
