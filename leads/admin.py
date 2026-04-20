"""
Admin configuration for leads
"""

from django.contrib import admin
from .models import Lead, Note, FollowUp

admin.site.register(Lead)
admin.site.register(Note)
admin.site.register(FollowUp)