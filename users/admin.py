from django.apps import apps
from django.contrib import admin

from users.models import ExtendUser

# Register your models here.
admin.site.register(ExtendUser)

app = apps.get_app_config('graphql_auth')

for model_name, model in app.models.items():
    admin.site.register(model)