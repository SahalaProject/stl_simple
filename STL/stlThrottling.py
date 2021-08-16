from rest_framework.throttling import SimpleRateThrottle


class AnonThrottle(SimpleRateThrottle):
    scope = 'anon'

    def get_cache_key(self, request, view):
        if request.user:
            if request.user.user_type == 2:
                ident = request.user.pk
                return self.cache_format % {
                    'scope': self.scope,
                    'ident': ident
                }


class UserThrottle(SimpleRateThrottle):
    scope = 'user'

    def get_cache_key(self, request, view):
        if request.user:
            ident = request.user.pk
        else:
            ident = self.get_ident(request)

        return self.cache_format % {
            'scope': self.scope,
            'ident': ident
        }

