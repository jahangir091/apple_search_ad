from rest_framework import serializers

from campaign.models import *


class UserConversionEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserConversionEvent
        fields = '__all__'


class UserSubscriptionEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserSubscriptionEvent
        fields = '__all__'
