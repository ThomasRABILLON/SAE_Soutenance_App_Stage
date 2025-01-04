from django.db import models
from django.utils import timezone

class DateHoraire(models.Model):
    class Meta:
        verbose_name = "DateHoraire"

    id_date_horaire = models.AutoField(primary_key=True, default=0)
    dt_date = models.DateField(default=timezone.now)
    heure = models.TimeField(default=timezone.now)
    duree = models.IntegerField(default=60)

    def __str__(self):
        return f'DateHoraire(id={self.id_date_horaire}[date={self.dt_date},heure={self.heure},duree={self.duree}])'
