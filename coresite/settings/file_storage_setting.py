import os
import logging
from .environment_setting import env, BASE_DIR, env_to_enum

from coresite.files import FileUploadStrategy, FileUploadStorage

FILE_UPLOAD_STRATEGY = env_to_enum(
    FileUploadStrategy,
    env("FILE_UPLOAD_STRATEGY", default="standard")
)
FILE_UPLOAD_STORAGE = env_to_enum(
    FileUploadStorage,
    env("FILE_UPLOAD_STORAGE", default="local")
)

FILE_MAX_SIZE = env.int("FILE_MAX_SIZE", default=10485760)  # 10 MiB

if FILE_UPLOAD_STORAGE == FileUploadStorage.LOCAL:
    MEDIA_ROOT_NAME = "media"
    MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_ROOT_NAME)
    MEDIA_URL = f"/{MEDIA_ROOT_NAME}/"

if FILE_UPLOAD_STORAGE == FileUploadStorage.S3:
    logging.info("Using S3 for file storage")
    # Using django-storages

    AWS_S3_ACCESS_KEY_ID = env("AWS_S3_ACCESS_KEY_ID")
    AWS_S3_SECRET_ACCESS_KEY = env("AWS_S3_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_REGION_NAME = 'me-south-1'
    AWS_S3_SIGNATURE_VERSION = env("AWS_S3_SIGNATURE_VERSION", default="s3v4")
    AWS_DEFAULT_ACL = 'public-read'
    AWS_S3_CUSTOM_DOMAIN = "thesupportify-backend-bucket.s3.me-south-1.amazonaws.com"
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }
    # s3 static settings
    AWS_LOCATION = 'static'

    STATIC_URL = "thesupportify-backend-bucket.s3.me-south-1.amazonaws.com/static/"
    STATICFILES_STORAGE = 'coresite.storage_backends.StaticStorage'
    # s3 public media settings
    PUBLIC_MEDIA_LOCATION = 'media'
    MEDIA_URL = "thesupportify-backend-bucket.s3.me-south-1.amazonaws.com/media/"
    DEFAULT_FILE_STORAGE = 'coresite.storage_backends.PublicMediaStorage'
    # s3 private media settings
    PRIVATE_MEDIA_LOCATION = 'private'
    PRIVATE_FILE_STORAGE = 'coresite.storage_backends.PrivateMediaStorage'

    # https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#canned-acl

    AWS_PRESIGNED_EXPIRY = env.int(
        "AWS_PRESIGNED_EXPIRY", default=10)  # seconds

    _AWS_S3_CUSTOM_DOMAIN = env("AWS_S3_CUSTOM_DOMAIN", default="")

    if _AWS_S3_CUSTOM_DOMAIN:
        AWS_S3_CUSTOM_DOMAIN = _AWS_S3_CUSTOM_DOMAIN
