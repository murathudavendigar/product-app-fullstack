# Generated by Django 4.1.5 on 2023-01-17 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_card_product_remove_card_user_and_more'),
        ('user', '0003_alter_profile_cards_alter_profile_favorites_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='cards',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='favorites',
        ),
        migrations.AddField(
            model_name='profile',
            name='cards',
            field=models.ManyToManyField(blank=True, null=True, related_name='cards', to='products.product'),
        ),
        migrations.AddField(
            model_name='profile',
            name='favorites',
            field=models.ManyToManyField(blank=True, null=True, related_name='favorites', to='products.product'),
        ),
    ]
