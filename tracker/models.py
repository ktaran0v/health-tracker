from django.db import models


class HealthRecord(models.Model):
    patient_name = models.CharField("Имя пациента", max_length=100)
    date = models.DateField("Дата измерения")
    weight = models.FloatField("Вес (кг)")
    blood_pressure = models.CharField("Артериальное давление", max_length=7, help_text="Формат: 120/80")
    pulse = models.IntegerField("Пульс (уд/мин)")
    notes = models.TextField("Комментарий", blank=True, null=True)
    
    def __str__(self):
        return f"{self.patient_name} — {self.date}"


    class Meta:
        ordering = ['-date']
        verbose_name = "Запись о здоровье"
        verbose_name_plural = "Записи о здоровье"

             

