from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField()
    def age_error_message(self, value):
        if value < 1900 or value > 2020:
            return 'Year you were born is not given in yyyy format. Please revise your information.'

    gender = models.StringField(
        choices=['Male', 'Female'],
        widget=widgets.RadioSelect
    )
    edu = models.StringField(
        choices=['No schooling completed', 'High school diploma','Some college credit (No degree)',
                 'Bachelor\'s degree (e.g. BA, BEng, BSc)', 'Master\'s degree (e.g. MA, MEng, MSc, MBA)',
                 'Professional degree (e.g. MD, JD)', 'Doctorate degree (e.g. Phd)'],
        widget=widgets.RadioSelect
    )
    job = models.StringField(
        choices=['Employed full time', 'Employed part time','Unemployed looking for work','Unemployed not looking for work','Retired','Student','Retired','Disabled'],
        widget=widgets.RadioSelect
    )
    exp = models.IntegerField()
    ethnic = models.StringField(
        choices=['White', 'Mixed/Multiple ethnic groups','Asian', 'Black/African','Other ethnic group'],
        widget=widgets.RadioSelect
    )

    AQ1 = models.StringField(
        choices = ['1', '2', '3', '4', '5', '6', '7'],
        widget = widgets.RadioSelect
    )
    AQ2 =  models.StringField(
        choices=['At a slower rate than during the first wave',
                 'At the same rate as during the first wave',
                 'At a faster rate than during the first wave'],
        widget=widgets.RadioSelect
    )
    AQ3 = models.StringField(
        choices=['1', '2', '3', '4', '5', '6', '7'],
        widget=widgets.RadioSelect
    )
    AQ4 = models.StringField(
        choices=['1', '2', '3', '4', '5', '6', '7'],
        widget=widgets.RadioSelect
    )

    AQ5 = models.StringField(
        choices=['1', '2', '3', '4', '5', '6', '7'],
        widget=widgets.RadioSelect
    )

    AQ6 = models.StringField(
        choices=['Now',
                 '6 months',
                 '1 year',
                 'Never', ],
        widget=widgets.RadioSelect
    )

    ad1 = models.StringField(
        choices=['I have taken part in the experiment seriously.', 'I have just clicked through. Please throw my data away! Your payment will not be affected by clicking this answer.'],
        widget = widgets.RadioSelect
    )

    ad2 = models.StringField(
        choices=['Yes', 'No'],
        widget=widgets.RadioSelect
    )

    ad3 = models.LongStringField(
        blank=True,
    )