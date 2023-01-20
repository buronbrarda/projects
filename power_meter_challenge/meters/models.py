from django.db import models
from django.core.validators import RegexValidator, MinValueValidator

# Create your models here.

class Meter(models.Model):

    # If we knew the max or min length we could define a better validator to check the amount of chars.
    alphanum_validator = RegexValidator(r'^[\w\d]+$', 'Only alphanumeric characters are allowed.')


    # null and blank are False by default.
    code = models.CharField(
        primary_key=True, #This implies unique=True
        validators=[alphanum_validator],
        max_length=20
    )

    name = models.CharField(
        unique=False,
        max_length=60
    )

    def __str__(self):
        return self.code


class Measure(models.Model):

    # For this problem it doesn't make sense to have a default value (e.g. now())
    # since meters have their own internal clock.
    # Internal clocks are essenctial since conection could be slow or or unstable.
    timestamp = models.DateTimeField(
        unique=True, #This also implies db_index=True, NICE!
        
    )

    consumption = models.FloatField(
        validators=[MinValueValidator(0)]
    )

    meter = models.ForeignKey(
        'Meter',
        on_delete=models.CASCADE,
        related_name='measures'
    )

    def __str__(self):
        return f'{self.id} - {self.timestamp}'
