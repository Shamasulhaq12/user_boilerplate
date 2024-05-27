from .environment_setting import env



# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = env('EMAIL_HOST')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
print(EMAIL_HOST_USER)
FROM_EMAIL = env('FROM_EMAIL')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
# EMAIL_PORT = int(env('EMAIL_PORT'))
EMAIL_FROM = env('FROM_EMAIL')
# EMAIL_USE_SSL = False
# EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

