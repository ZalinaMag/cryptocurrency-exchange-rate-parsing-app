from tortoise import fields, models

class KeyJson(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    kash = fields.JSONField()
    difference = fields.DecimalField(max_digits=20, decimal_places=8)
    total_amount = fields.DecimalField(max_digits=20, decimal_places=8)
    date = fields.DatetimeField(auto_now_add=True)
    coins = fields.JSONField()

    class Meta:
        table = "key_json"