from apps.profiles.models import AuthProvider
from json import dumps

__author__ = '@masterfung'

def save_profile(strategy, details, user=None, *args, **kwargs):

    if user:
        print kwargs
        user.birthday = kwargs['response'].get('birthday', 'NA')
        user.profile_updated_time = kwargs['response'].get('updated_time', 'NA')
        user.city = kwargs['response'].get('city', 'San Francisco')
        user.phone = kwargs['response'].get('phone', '000.000.0000')
        # user.zipcode = kwargs['response'].get('zip', '00000')
        user.fib = kwargs['response'].get('id', 0)

        user.raw = dumps(kwargs['response'])
        if user.provider is None and kwargs.get('backend'):
            backend = kwargs['backend'].name
            provider, is_created = AuthProvider.objects.get_or_create(provider=backend)
            user.provider = provider
        try:
            image_url = None
            if user.provider.provider == "facebook":
                image_url = "https://graph.facebook.com/{0}/picture?type=large".format(kwargs['uid'])

            if image_url:
                user.picture_url = image_url
        except (KeyError, AttributeError):
            pass

        user.save()
        return

# kwargs['response']['birthday']
# profile = Profile(user=request.user,
#     birthday = kwargs['response'].get('birthday'),
#
# )
# kwargs['response'].get('birthday')

#for k, v in kwargs['response'].iteritems():
#    print k, v