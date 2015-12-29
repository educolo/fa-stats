from django.db import models


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating ``created`` and ``modified``
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Base(TimeStampedModel):
    """
    An abstract base class model that provides basic functionality
    """

    def save(self, *args, **kwargs):
        validate = kwargs.get('validate', False)
        if validate:
            self.full_clean()
        super(Base, self).save(*args, **kwargs)

    class Meta:
        abstract = True
