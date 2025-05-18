from storages.backends.s3boto3 import S3Boto3Storage

class MediaRootS3Boto3Storage(S3Boto3Storage):
    location = 'media'  # Sube todo dentro de la carpeta media/
    file_overwrite = False  # Opcional: evita que se sobreescriban archivos con el mismo nombre
