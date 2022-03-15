from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'intro'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            chosen_app = random.randrange(1, 5)
            chosen_demand = random.randrange(0, 3)
            p.participant.vars['chosen_app'] = chosen_app
            p.participant.vars['chosen_demand'] = chosen_demand
            p.participant.vars['mobilex'] = [1, ]
            p.participant.vars['ip_check'] = [1, ]



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    chosen_app = models.IntegerField()
    chosen_demand = models.IntegerField()
    ip_observed = models.StringField()
