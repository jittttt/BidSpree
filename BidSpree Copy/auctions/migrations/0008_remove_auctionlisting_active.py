from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auctionlisting_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionlisting',
            name='active',
        ),
    ]
