from rest_framework import status
from apps.core.models import UserActivation
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny


class AccountActivationAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, secret_key):
        try:
            """
            This api is used to activate user account
            Parameters:
                secret_key

                """

            user_activation = get_object_or_404(
                UserActivation, otp=secret_key)
            if user_activation:
                if user_activation.activated:
                    return Response({"message": "Account already activated", "status": "400"},
                                    status=status.HTTP_400_BAD_REQUEST)
                if user_activation.otp == secret_key and not user_activation.is_expired:
                    user_activation.activated = True
                    user_activation.save()
                    user_activation.user.is_active = True
                    user_activation.user.save()

                    return Response({"message": "Account activated successfully", "status": "200"},
                                    status=status.HTTP_200_OK)
                return Response({"message": "Activation key is not valid", "status": "400"},
                                status=status.HTTP_400_BAD_REQUEST)
            return Response({"message": "Invalid token", "status": "400"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({"message": "User Not Found", "status": "500"}, status.HTTP_500_INTERNAL_SERVER_ERROR)
