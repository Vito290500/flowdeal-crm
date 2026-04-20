"""
Models configuration for leads
"""

from django.db import models
from django.conf import settings

class Lead(models.Model):

    class Status(models.TextChoices):
        """Class for check the status for leads"""

        NUOVO =         'nuovo',   'Nuovo'
        CONTATTATO =    'contattato', 'Contattato'
        TRATTATIVA =    'trattativa', 'Trattativa'
        VINTO =         'vinto', 'Vinto'
        PERSO =         'perso', 'Perso'


    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='leads')
    nome = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=30, blank=True)
    azienda = models.CharField(max_length=150, blank=True)
    fonte_lead = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NUOVO)
    valore_potenziale = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.nome} — {self.status}"
    

class Note(models.Model):
    lead       = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='note')
    autore     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    testo      = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Nota su {self.lead.nome} — {self.created_at:%d/%m/%Y}"
    

class FollowUp(models.Model):
    lead            = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='followups')
    data_promemoria = models.DateField()
    completato      = models.BooleanField(default=False)
    nota            = models.CharField(max_length=255, blank=True)
    created_at      = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['data_promemoria']

    def __str__(self):
        stato = "✓" if self.completato else "⏳"
        return f"{stato} FollowUp {self.lead.nome} — {self.data_promemoria}"