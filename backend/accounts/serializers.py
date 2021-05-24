from dj_rest_auth.serializers import UserDetailsSerializer


class ExtendedUserDetailsSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        fields = (*UserDetailsSerializer.Meta.fields, 'is_staff')
