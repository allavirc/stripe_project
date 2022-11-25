from django.db import models
from django.db.models import (
    Model,
    CharField,
    IntegerField,
    ImageField
)


class Item(Model):

    name = CharField(
        verbose_name='Название',
        max_length=255,
        null=False,
    )
    description = CharField(
        verbose_name='Описание',
        max_length=500,
        null=False,
    )
    img = ImageField(
        verbose_name='Фото',
        null=True,
        upload_to='products'
    )
    price = IntegerField(
        verbose_name='Стоимость товара',
        null=False,
    )

    def __str__(self) -> str:
        return f'{self.name}->{self.price}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
