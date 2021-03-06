from django.db import models
from charsheet.constants import PLAYBOOK_CHOICES, DEMEANOR_CHOICES, TRAINING_CHOICES, BALANCE_PAIRS, BACKGROUND_CHOICES
from django.conf import settings
from campaign.models import Campaign
from django.core.validators import MaxValueValidator, MinValueValidator

def get_readable_playbook(playbook_choice):
    return [playbook_pair[1] for playbook_pair in PLAYBOOK_CHOICES if playbook_pair[0] == playbook_choice][0]

class Character(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    campaign = models.ForeignKey(
        Campaign,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    playbook = models.CharField(
        max_length=15,
        choices=PLAYBOOK_CHOICES
    )
    name = models.CharField(max_length=100)
    demeanor = models.CharField(
        max_length=15,
        choices=DEMEANOR_CHOICES,
    )
    background = models.CharField(
        max_length=15,
        choices=BACKGROUND_CHOICES,
    )
    training = models.CharField(
        max_length=15,
        choices=TRAINING_CHOICES
    )
    creativity = models.IntegerField(
        null=True,
        blank=True,
        )
    focus = models.IntegerField(
        null=True,
        blank=True,
    )
    harmony = models.IntegerField(
        null=True,
        blank=True,
    )
    passion = models.IntegerField(
        null=True,
        blank=True,
    )
    fatigue = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )
    balance = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(3),
            MinValueValidator(-3),
        ]
    )
    afraid = models.BooleanField(default=False)
    angry = models.BooleanField(default=False)
    foolish = models.BooleanField(default=False)
    guilty = models.BooleanField(default=False)
    insecure = models.BooleanField(default=False)
    notes = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        try:
            playbook_full = get_readable_playbook(self.playbook)
            return self.name + ', ' + playbook_full
        except:
            return ''

    def full_name(self):
        return self.__str__()
    
    def balance_high(self):
        try:
            return BALANCE_PAIRS[self.playbook][1]
        except:
            return ''

    def balance_low(self):
        try:
            return BALANCE_PAIRS[self.playbook][0]
        except:
            return ''

    def to_dict(self):
        try:
            playbook = get_readable_playbook(self.playbook)
        except:
            playbook = ''
        return {
            'id': self.id,
            'playbook': playbook,
            'name': self.name,
            'background': self.background,
            'demeanor': self.demeanor,
            'training': self.training,
            'creativity': self.creativity,
            'focus': self.focus,
            'harmony': self.harmony,
            'passion': self.passion,
            'fatigue': self.fatigue,
            'balance': self.balance,
            'balance_high': self.balance_high(),
            'balance_low': self.balance_low(),
            'afraid': self.afraid,
            'angry': self.angry,
            'foolish': self.foolish,
            'guilty': self.guilty,
            'insecure': self.insecure,
            'notes': self.notes,
        }
