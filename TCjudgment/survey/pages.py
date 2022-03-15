from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from statistics import mean


class Demographic(Page):
    form_model = 'player'
    form_fields = ['gender', 'age', 'edu', 'job', 'exp', 'ethnic']


class AQp1(Page):
    form_model = 'player'
    form_fields = ['AQ1', 'AQ2',]


class AQp2(Page):
    form_model = 'player'
    form_fields = ['AQ3', 'AQ4', 'AQ5']


class AQp3(Page):
    form_model = 'player'
    form_fields = ['AQ6']


class after_Demographic(Page):
    form_model = 'player'
    form_fields = ['ad1', 'ad2', 'ad3']

    def error_message(self, values):
        if values['ad2'] == 'Yes' and values['ad3'] == '':
            return 'Please answer for question 3.'


class Results(Page):
    def vars_for_template(self):

        y5 = self.participant.vars['abs_forecast_10_error']
        y6 = self.participant.vars['abs_forecast_20_error']
        y7 = self.participant.vars['abs_forecast_30_error']


        abs_forecast_10_error = y5
        abs_forecast_20_error = y6
        abs_forecast_30_error = y7

        mfe_pre = (y5 + y6 + y7) / 3
        mfe = round(mfe_pre, 2)


        bonus = round(1.5 - 0.009 * mfe, 2)



        if bonus > 0:
            self.participant.payoff = c(bonus)
        else:
            self.participant.payoff = c(0)

        final_payoff = self.participant.payoff_plus_participation_fee()

        forecast_10 = self.participant.vars['forecast_10']
        forecast_20 = self.participant.vars['forecast_20']
        forecast_30 = self.participant.vars['forecast_30']

        actual_10 = self.participant.vars['actual_10']
        actual_20 = self.participant.vars['actual_20']
        actual_30 = self.participant.vars['actual_30']

        return {
            'abs_forecast_10_error': abs_forecast_10_error, 'abs_forecast_20_error': abs_forecast_20_error,
            'abs_forecast_30_error': abs_forecast_30_error,
            'mfe': mfe, 'bonus': bonus, 'final_payoff': final_payoff,
            'forecast_10': forecast_10, 'forecast_20': forecast_20, 'forecast_30': forecast_30,
            'actual_10': actual_10, 'actual_20': actual_20, 'actual_30': actual_30,
        }


class Final(Page):
    pass


page_sequence = [
    AQp1,
    AQp2,
    AQp3,
    Demographic,
    after_Demographic,
    Results,
    Final
]
