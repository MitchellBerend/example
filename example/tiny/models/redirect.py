from datetime import date, datetime
import random
import string

from django.db import models


def generate_random_shortcode():
    # underscores are also valid
    pool = string.ascii_letters + string.digits + '_'

    return ''.join([random.choice(pool) for _ in range(6)])


class Redirect(models.Model):

    url = models.URLField(
        max_length=200,
    )

    shortcode = models.CharField(
        max_length=6,
        unique=True,
    )

    created_date = models.DateField(
        default=date.today,
    )

    last_accessed_date = models.DateTimeField(
        default=datetime.now
    )
    
    redirect_count = models.IntegerField(
        default=0,
    )
    
    @staticmethod
    def generate_random_shortcode():
        # underscores are also valid
        pool = string.ascii_letters + string.digits + '_'

        return ''.join([random.choice(pool) for _ in range(6)])
