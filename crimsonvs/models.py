from django.db import models

# Create your models here.


class Card(models.Model):
    id = models.IntegerField(primary_key=True, db_index=True)
    type = models.TextField(db_index=True)
    name = models.TextField(db_index=True)
    trinity = models.TextField()
    junction = models.TextField(null=True)
    junction_function = models.TextField(null=True)
    charisma = models.IntegerField(null=True)
    cost = models.IntegerField(null=True)
    hp = models.IntegerField(null=True)
    ap = models.IntegerField(null=True)
    characters = models.TextField(null=True)
    rarity = models.TextField(db_index=True)

    def __str__(self):
        return str(self.id) + ". " + self.name


class Deck(models.Model):
    id = models.IntegerField(primary_key=True)
    deck_id = models.IntegerField(db_index=True)
    card_id = models.IntegerField(null=True)
    user_id = models.IntegerField(db_index=True)

    def __str__(self):
        return 'Deck with id {} of user with id {}'.format(self.id, self.user_id)


class User(models.Model):
    id = models.IntegerField(primary_key=True, db_index=True)
    username = models.TextField(db_index=True)
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField(db_index=True)
    date_joined = models.TimeField()
    last_login = models.TimeField(null=True)
    deck_1_id = models.IntegerField(name='first deck id', null=True)
    deck_2_id = models.IntegerField(name='second deck id', null=True)
    deck_3_id = models.IntegerField(name='third deck id', null=True)
    rank = models.IntegerField(default=0)
    champion = models.BooleanField(False)

    def __str__(self):
        return 'User with information concerning her'


class Gallery(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(db_index=True)
    card_id = models.IntegerField()
    count = models.IntegerField()

    def __str__(self):
        return 'List of card ids that user {} has, including how many of each'.format(self.id)
