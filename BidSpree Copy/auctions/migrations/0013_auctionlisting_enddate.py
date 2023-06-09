from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_alter_user_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='endDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
