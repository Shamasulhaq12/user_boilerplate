from datetime import date
from django.conf import settings
from rest_framework import status
from django.db import transaction
from rest_framework import permissions
from apps.core.models import UserActivation
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from utils.threads.email_thread import send_mail
from apps.core.serializers import CreateUserSerializer
from apps.core.utils.reset_email_token_util import reset_email_token
from apps.userprofile.serializers import UserProfileSerializer

User = get_user_model()
email = settings.EMAIL_HOST_USER
react_domain = settings.REACT_DOMAIN
domain = settings.DOMAIN


class RegistrationView(APIView):
    """Register and login api instant """

    permission_classes = (permissions.AllowAny,)
    serializer_class = CreateUserSerializer

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        profile = serializer.validated_data.pop('profile', None)

        serializer.save()
        if profile:
            profile_serializer = UserProfileSerializer(data=profile)
            profile_serializer.is_valid(raise_exception=True)

            profile_serializer.save(
                user=serializer.instance)

        instance = serializer.instance
        secret_key = reset_email_token(50)

        user_activation, _ = UserActivation.objects.get_or_create(
            user=instance)
        user_activation.otp = secret_key
        user_activation.is_expired = False
        user_activation.activated = False
        user_activation.save()

        key = {
            'username': instance.username,
            'otp': None, 'button': react_domain + '/auth/account-verified/' + secret_key,
            'year': date.today().year
        }
        print(key)

        subject = "Verify Your Account"
        template_name = "auth/new_userRegister.html"
        recipient = [request.data['email']]

        send_mail(subject=subject, html_content=template_name,
                  recipient_list=recipient, key=key)

        return Response({
            "message": "User created successfully. Check your email for verification"
        }, status=status.HTTP_201_CREATED)
