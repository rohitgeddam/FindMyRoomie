from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    """Token generator for email reset link."""

    def _make_hash_value(self, user, timestamp):
        """generate hash values for email reset link."""
        return (
            six.text_type(user.pk)
            + six.text_type(timestamp)
            + six.text_type(user.profile.email_confirmed)
        )


account_activation_token = AccountActivationTokenGenerator()
