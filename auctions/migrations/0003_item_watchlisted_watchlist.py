# Generated by Django 4.2.3 on 2024-06-22 10:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_item_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='watchlisted',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Item_Watchlist', to='auctions.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User_Watchlist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]