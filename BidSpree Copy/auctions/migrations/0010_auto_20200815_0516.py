from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auctionlisting_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='watchlist',
            field=models.ManyToManyField(blank=True, related_name='userWatchlist', to='auctions.AuctionListing'),
        ),
        migrations.DeleteModel(
            name='Watchlist',
        ),
    ]
