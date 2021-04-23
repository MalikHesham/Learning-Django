# Generated by Django 3.2 on 2021-04-22 12:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=50)),
                ('published_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Book Categories',
            },
        ),
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked', models.IntegerField(blank=True, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(to='books.BookCategory'),
        ),
    ]