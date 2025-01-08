from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Attendee
from django.conf import settings

@receiver(post_save, sender=Attendee)
def send_registration_email(sender, instance, created, **kwargs):
    if created:                     # Only send the email when a new registration is created
        subject = f"Registration Confirmation for {instance.event.title}"
        message = f"Hello {instance.user.username},\n\nYou have successfully registered for {instance.event.title}.\n\nEvent Date: {instance.event.date_time}\nLocation: {instance.event.location}\n\nBest regards,\nEvent Team"
        recipient_list = [instance.user.email]
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)

