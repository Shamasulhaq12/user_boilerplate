from datetime import date
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from apps.core.models import UserActivation
from apps.core.utils.reset_email_token_util import reset_email_token
from utils.threads.email_thread import send_mail
from apps.core.serializers import ResendActivationSerializer
from django.conf import settings

email = settings.EMAIL_HOST_USER
react_domain = settings.REACT_DOMAIN
domain = settings.DOMAIN


class ResendActivationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = ResendActivationSerializer

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')

        if email is None:
            return Response({"message": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user_activation = get_object_or_404(UserActivation, user__email=email)
            if user_activation.activated:
                return Response({"message": "Account already activated"}, status=status.HTTP_400_BAD_REQUEST)

            secret_key = reset_email_token(50, True)
            user_activation.otp = secret_key
            user_activation.is_expired = False
            user_activation.save()
            key = {
                'username': user_activation.user.username,
                'otp': None,
                'button': react_domain + 'auth/account-verified/' + secret_key,
                'year': date.today().year
            }

            subject = "Verify Your Account"
            template_name = "auth/new_userRegister.html"
            recipient = [email]

            send_mail(subject=subject, html_content=template_name,
                      recipient_list=recipient, key=key)

            return Response({"message": "New OTP sent successfully. Check your email for verification"},
                            status=status.HTTP_200_OK)
        except UserActivation.DoesNotExist:
            return Response({"message": "User not found or account already activated"},
                            status=status.HTTP_400_BAD_REQUEST)
