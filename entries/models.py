from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


WORD_LENGTH = 50

ROMANIZE = {
    "ā": "a",
    "ī": "i",
    "ū": "u",
    "ṃ": "m",
    "ṅ": "n",
    "ñ": "n",
    "ṭ": "t",
    "ḍ": "d",
    "ṇ": "n",
    "ḷ": "l",
}


class Entry(models.Model):
    """Pali Entry"""

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    pali = models.CharField(max_length=WORD_LENGTH)
    sanskrit = models.CharField(max_length=WORD_LENGTH, null=True, blank=True)
    roman = models.CharField(max_length=WORD_LENGTH)
    content = models.TextField(blank=True)

    class Meta:
        ordering = ["pali"]
        verbose_name_plural = "Entries"
        constraints = [models.UniqueConstraint(name="unique_sanskrit", fields=["pali", "sanskrit"])]

    def __str__(self) -> str:
        return self.pali


@receiver(pre_save, sender=Entry)
def pre_save_entry_latin(instance, **kwargs):
    """Generate Entry's roman"""

    pali = instance.pali
    roman = [ROMANIZE[c] if c in ROMANIZE else c for c in pali]
    instance.roman = "".join(roman)
