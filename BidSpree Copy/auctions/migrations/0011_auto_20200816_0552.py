from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_auto_20200815_0516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='imageUrl',
            field=models.URLField(blank=True),
        ),
    ]
