from django.contrib import admin
from django.template.loader import render_to_string
from django.core.mail import send_mail
from .models import Invitation

# Register your models here.

def send_invitation_email(modeladmin, request, queryset):
    for invitation in queryset:

        # Generate the invitation link with the unique token
            # invitation_link = "https://yourdomain.com/accept-invite/?token=" + str(invitation.token)
        invitation_link = "http://localhost:8000/accept-invite/?token=" + str(invitation.token)

        # Render the email content using the template
        email_content = render_to_string('email/invitation_email.html', {'invitation_link': invitation_link})
        
        send_mail(
            'Your Invitation to Our Platform',
            email_content,
            'noreply@yourdomain.com',
            [invitation.email],
            fail_silently=False,
            html_message=email_content
        )

class InvitationAdmin(admin.ModelAdmin):
    list_display = ('email', 'sent_on', 'used')
    actions = [send_invitation_email]


admin.site.register(Invitation, InvitationAdmin)
