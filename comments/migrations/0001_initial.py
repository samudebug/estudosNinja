# Generated by Django 2.0.6 on 2018-09-04 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('sites', '0002_alter_domain_unique'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_pk', models.TextField(verbose_name='object ID')),
                ('comment', models.TextField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_type_set_for_comentario', to='contenttypes.ContentType', verbose_name='content type')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]