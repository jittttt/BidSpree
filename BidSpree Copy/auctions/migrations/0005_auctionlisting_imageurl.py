from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20200810_0608'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='imageUrl',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
