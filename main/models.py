from django.db import models

class TodoList(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    purpose = models.CharField(max_length=64, verbose_name='Цель')

    class Meta:
        verbose_name = ("Цель")
        verbose_name_plural = ("Цели")

    def __str__(self):
        return f"{self.name} {self.purpose}"