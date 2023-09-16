from django.db import models
from datetime import datetime, timedelta

class Entreprise(models.Model):
    def __str__(self):
        return self.nom
    nom = models.CharField(max_length=150)
    class Meta:
        verbose_name='Entreprise'
        verbose_name_plural='Entreprises'

class Agence(models.Model):
    def __str__(self):
        return self.nom
    nom = models.CharField(max_length=150)
    adresse = models.CharField(max_length=150)
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    class Meta:
        verbose_name='Agence'
        verbose_name_plural='Agences'

class Voyage(models.Model):
    def __str__(self):
        return self.ville_depart +' '+ self.ville_arrivee
    ville_depart = models.CharField(max_length=105)
    ville_arrivee = models.CharField(max_length=105)
    date = models.DateField()
    heure_depart = models.TimeField()
    heure_arrivee = models.TimeField()
    duree = models.DurationField(null=True, blank=True)
    place = models.PositiveIntegerField(null=True, blank=True)
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    agence = models.ForeignKey(Agence, on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        if self.heure_depart and self.heure_arrivee:
            depart = datetime.combine(datetime.today(), self.heure_depart)
            arrivee = datetime.combine(datetime.today(), self.heure_arrivee)
            if arrivee < depart:
                arrivee += timedelta(days=1)
            self.duree = arrivee - depart
        super().save(*args, **kwargs)
    class Meta:
        verbose_name='Voyage'
        verbose_name_plural='Voyages'
        
        
class Reservation(models.Model):
    def __str__(self):
        return self.voyage.ville_depart+'-'+self.voyage.ville_arrivee
    
    voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE)
    date_reservation = models.DateTimeField(default=datetime.now)
    passager = models.PositiveIntegerField()
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.voyage.place -= self.passager
        self.voyage.save()

    def delete(self, *args, **kwargs):
        self.voyage.place += self.passager
        self.voyage.save()
        super().delete(*args, **kwargs)
    class Meta:
        verbose_name='Reservation'
        verbose_name_plural='Reservations'

# Create your models here.
