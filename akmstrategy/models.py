from django.db import models


class BaseTitleTextModel(models.Model):
    """
    title, text
    """

    title = models.CharField("Заголовок", max_length=255)
    text = models.TextField("Описание")

    class Meta:
        abstract = True


class Ad(BaseTitleTextModel, models.Model):
    """
    Модель рекламы (Обычная или Яндекс.Дзен)
    """

    SIMPLE = 'SIMPLE_AD_'
    DZEN = 'YANDEX_DZEN_AD_'
    TYPE_CHOICES = (
        (SIMPLE, 'Обычная'),
        (DZEN, 'Яндекс.Дзен'),
    )

    ad_type = models.CharField("Тип рекламы",
                               choices=TYPE_CHOICES,
                               default=SIMPLE,
                               max_length=255,
                               help_text="Тип рекламы: Обычная или Яндекс.Дзен")

    class Meta:
        verbose_name = 'Реклама'
        verbose_name_plural = 'Рекламы'

    def __str__(self) -> str:
        return f'{self.title} - {self.ad_type}'


class Advantage(BaseTitleTextModel, models.Model):
    """
    Наши преимущества в блоке (Специализируемся на Яндекс.Дзене)
    """

    LEFT = 'LEFT_SIDE_'
    RIGHT = 'RIGHT_SIDE_'
    PLACE_CHOICES = (
        (LEFT, "Слева"),
        (RIGHT, "Справа"),
    )

    img = models.URLField("Фото", help_text='Ссылка на SVG')
    img_place = models.CharField("Место фото",
                                 max_length=255, 
                                 help_text='Сторона на которой будет стоять фото.', 
                                 choices=PLACE_CHOICES, 
                                 default=LEFT)
    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'

    def __str__(self) -> str:
        return self.title


class Goal(BaseTitleTextModel, models.Model):
    """
    Модель целей для блока (Работаем с разными целями)
    """

    class Meta:
        verbose_name = 'Цель'
        verbose_name_plural = 'Цели'

    def __str__(self) -> str:
        return self.title