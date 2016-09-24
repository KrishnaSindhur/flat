from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from django.dispatch import receiver
from django.db.models.signals import post_migrate

#hacky solution to ensure custom permissions are introduce on the existing django user model
@receiver(post_migrate)
def add_user_permissions(sender, **kwargs):
    content_type = ContentType.objects.get(app_label='auth', model='user')
    Permission.objects.get_or_create(codename='groupread', name='User may read documents in the namespaces of other users in his/her group(s)', content_type=content_type)
    Permission.objects.get_or_create(codename='groupwrite', name='User may write documents in the namespaces of other users in his/her group(s)', content_type=content_type)
    Permission.objects.get_or_create(codename='allowcopy', name='User may copy documents wherever he/she has write permission', content_type=content_type)
    Permission.objects.get_or_create(codename='allowdelete', name='User may delete documents wherever he/she has write permission', content_type=content_type)
