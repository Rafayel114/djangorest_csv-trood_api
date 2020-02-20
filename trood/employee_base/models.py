from django.db import models

class Employee(models.Model):

    name       = models.CharField(max_length=200)
    surname    = models.CharField(max_length=200)
    birth_date = models.DateField(auto_now_add=False, auto_now=False)
    position   = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        ordering = ['name']

    def __str__(self):
        return '{} {}'.format(self.surname, self.name)



class Employee_Base(models.Model):
    file = models.FileField(upload_to='emp_base/')
