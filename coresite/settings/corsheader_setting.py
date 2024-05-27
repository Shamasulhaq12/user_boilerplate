CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = False
CORS_ALLOW_METHODS = (
    'GET',
    'PUT',
    'POST',
    'PATCH',
    'DELETE',
    'OPTIONS',
)

CORS_ALLOW_HEADERS = (
    'dnt',
    'accept',
    'origin',
    'user-agent',
    'x-csrftoken',
    'Content-Type',
    'content-type',
    'authorization',
    'accept-encoding',
    'x-requested-with',
    'access-control-allow-origin',
    'Access-Control-Allow-Origin',
)

CORS_ORIGIN_WHITELIST = ['http://localhost:3000', "https://staging.thesupportify.com", 'http://localhost:3001',
                         'https://localhost:3000', 'https://localhost:3001',
                         'https://supportify-staging.beyonderissolutions.com']
