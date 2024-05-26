# -*- coding: utf-8 -*-

# Standard Library
import logging

# Third Party Stuff
from django.utils.translation import gettext as _
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers
from Home.models import Profile
from django.contrib.auth.models import User


# Phone Auth Stuff
from .backends import get_sms_backend

logger = logging.getLogger(__name__)


class PhoneSerializer(serializers.Serializer):
    phone_number = PhoneNumberField()


class SMSVerificationSerializer(serializers.Serializer):
    phone_number = PhoneNumberField(required=True)
    session_token = serializers.CharField(required=True)
    user_id = serializers.CharField(required=True)
    security_code = serializers.CharField(required=True)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        phone_number = attrs.get("phone_number", None)
        security_code, session_token, user = (
            attrs.get("security_code", None),
            attrs.get("session_token", None),
            attrs.get("user_id", None)
        )
        backend = get_sms_backend(phone_number=phone_number)
        verification, token_validatation = backend.validate_security_code(
            security_code=security_code,
            phone_number=phone_number,
            session_token=session_token,
        )

        if verification is None:
            print('Security code is not valid')

        elif token_validatation == backend.SESSION_TOKEN_INVALID:
            print('Session Token mis-match')

        elif token_validatation == backend.SECURITY_CODE_EXPIRED:
            print('Security code has expired')

        elif token_validatation == backend.SECURITY_CODE_VERIFIED:
            print('Security code is already verified')

        else:
            print('Security Code Verified Successfully')
            get_user = User.objects.get(username=user)
            user_num = Profile(phone_number=phone_number, user=get_user)
            user_num.save()

        return attrs
