from django.db import models

# Create your models here.




class ImbaSteamItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    appid = models.IntegerField()
    name = models.CharField(max_length=255)
    quality = models.CharField(max_length=45)
    rarity = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    price = models.IntegerField()
    tags = models.CharField(max_length=512, blank=True, null=True)
    ban = models.CharField(max_length=10)
    hero = models.CharField(max_length=45)
    exterior = models.CharField(max_length=45, blank=True, null=True)
    weight = models.SmallIntegerField()
    tradable = models.SmallIntegerField()
    image_url = models.CharField(max_length=500, blank=True, null=True)
    create_time = models.IntegerField()
    update_time = models.IntegerField()
    custom_price = models.IntegerField(blank=True, null=True)
    market_hash_name = models.CharField(max_length=255)
    category_id = models.BigIntegerField(blank=True, null=True)
    flag = models.IntegerField(blank=True, null=True)
    game = models.CharField(max_length=50, blank=True, null=True)
    cardborder = models.CharField(max_length=50, blank=True, null=True)
    item_class = models.CharField(max_length=50, blank=True, null=True)
    comment_num = models.IntegerField()
    rmb_price = models.IntegerField()
    compensate_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'imba_steam_item'
        unique_together = (('appid', 'market_hash_name'),)


class ImbaSteamItemPrice(models.Model):
    id = models.BigAutoField(primary_key=True)
    priceDate = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    item_id = models.ForeignKey(ImbaSteamItem)


