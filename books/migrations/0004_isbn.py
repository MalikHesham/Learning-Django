# Generated by Django 3.2 on 2021-04-22 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0003_book_metrics'),
    ]

    operations = [
        migrations.CreateModel(
            name='ISBN',
            fields=[
                ('isbn_number', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('author_title', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('book_name', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.book')),
            ],
        ),
    ]
