from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage
from .serializers import ContactMessageSerializer
import logging

logger = logging.getLogger(__name__)


class ContactAPIView(APIView):
    """
    POST /api/contact/
    Saves the message to DB and sends email notification to Atul.
    """

    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                {"success": False, "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 1. Save to database
        contact = serializer.save()

        # 2. Send email notification
        try:
            send_mail(
                subject=f"New Portfolio Message from {contact.name}",
                message=(
                    f"You received a new message from your portfolio!\n\n"
                    f"Name    : {contact.name}\n"
                    f"Email   : {contact.email}\n"
                    f"Message :\n{contact.message}\n\n"
                    f"---\nReply directly to: {contact.email}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_RECEIVER_EMAIL],
                fail_silently=False,
            )
        except Exception as e:
            logger.error(f"Email send failed for contact id={contact.id}: {e}")

        return Response(
            {
                "success": True,
                "message": "Thanks for reaching out! I'll get back to you soon."
            },
            status=status.HTTP_201_CREATED
        )


class ContactListAPIView(APIView):
    """
    GET /api/contact/messages/
    Returns all saved messages (protected by secret key).
    """

    def get(self, request):
        secret = request.headers.get("X-Admin-Secret", "")
        if secret != settings.ADMIN_SECRET_KEY:
            return Response(
                {"detail": "Unauthorized."},
                status=status.HTTP_401_UNAUTHORIZED
            )
        messages = ContactMessage.objects.all()
        serializer = ContactMessageSerializer(messages, many=True)
        return Response({"count": messages.count(), "results": serializer.data})
