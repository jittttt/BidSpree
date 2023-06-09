from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auctionlisting_imageurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='description',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='startBid',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='bid',
            name='bidValue',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='comment',
            name='commentValue',
            field=models.CharField(max_length=250),
        ),
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auctionListing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.AuctionListing')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
