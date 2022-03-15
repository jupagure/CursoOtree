from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import datetime


class Comprehension(Page):
    form_model = 'player'
    form_fields = ['CQ1', 'CQ2', 'CQ3', 'CQ4']

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        chosen_demand = self.participant.vars['chosen_demand']
        return {
            'chosen_demand': chosen_demand
        }

class Intro(Page):
    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        p = self.player
        p.participant.vars['time_previous'] = datetime.datetime.now()


class Round_1(Page):
    form_model = 'player'
    form_fields = ['forecast_10']

    def before_next_page(self):
        p = self.player
        p.actual_10 = 628

        p.time_spent1 = (datetime.datetime.now() - p.participant.vars['time_previous']).total_seconds()

        p.participant.vars['time_previous'] = datetime.datetime.now()

        p.participant.vars['forecast_10'] = p.forecast_10
        p.participant.vars['actual_10'] = 628
        p.participant.vars['forecast_10_error'] = p.forecast_10 - 628
        p.participant.vars['abs_forecast_10_error'] = abs(p.forecast_10 - 628)


    def vars_for_template(self):
        y1 = Constants.determined_series[self.player.participant.vars['chosen_demand']][:]
        players = self.player.in_previous_rounds()
        new_days = 270 + (self.round_number - 1) * 10
        round_number = self.round_number

        round_operator = 0

        while round_operator < 30:
            round_operator = round_operator + 1
            y1.append(None)

        chosen_demand = self.participant.vars['chosen_demand']

        return {
            'highchart_series1': y1, 'player_in_previous_rounds': players,
            'new_days': new_days, 'round_number': round_number, 'chosen_demand': chosen_demand
        }

class Round_2(Page):
    form_model = 'player'
    form_fields = ['forecast_20']

    def before_next_page(self):
        p = self.player
        p.actual_20 = 592

        p.time_spent2 = (datetime.datetime.now() - p.participant.vars['time_previous']).total_seconds()

        p.participant.vars['time_previous'] = datetime.datetime.now()
        p.participant.vars['forecast_20'] = p.forecast_20
        p.participant.vars['actual_20'] = 592
        p.participant.vars['forecast_20_error'] = p.forecast_20 - 592
        p.participant.vars['abs_forecast_20_error'] = abs(p.forecast_20 - 592)


    def vars_for_template(self):
        y1 = Constants.determined_series[self.player.participant.vars['chosen_demand']][:]
        y2 = []
        players = self.player.in_previous_rounds()
        new_days = 270 + (self.round_number - 1) * 10
        round_number = self.round_number

        forecast_10 = self.player.forecast_10

        round_operator1 = 0

        while round_operator1 < 30:
            round_operator1 = round_operator1 + 1
            y1.append(None)

        chosen_demand = self.participant.vars['chosen_demand']

        return {
            'highchart_series1': y1,  'player_in_previous_rounds': players,
            'new_days': new_days, 'round_number': round_number, 'forecast_10': forecast_10,
            'chosen_demand': chosen_demand
        }

class Round_3(Page):
    form_model = 'player'
    form_fields = ['forecast_30',]

    def before_next_page(self):
        p = self.player
        p.actual_30 = 570

        p.time_spent3 = (datetime.datetime.now() - p.participant.vars['time_previous']).total_seconds()

        p.participant.vars['time_previous'] = datetime.datetime.now()
        p.participant.vars['forecast_30'] = p.forecast_30
        p.participant.vars['actual_30'] = 570
        p.participant.vars['forecast_30_error'] = p.forecast_30 - 570
        p.participant.vars['abs_forecast_30_error'] = abs(p.forecast_30 - 570)


    def vars_for_template(self):
        y1 = Constants.determined_series[self.player.participant.vars['chosen_demand']][:]
        players = self.player.in_previous_rounds()
        new_days = 270 + (self.round_number - 1) * 10
        round_number = self.round_number

        forecast_10 = self.player.forecast_10
        forecast_20 = self.player.forecast_20
        round_operator1 = 0

        while round_operator1 < 30:
            round_operator1 = round_operator1 + 1
            y1.append(None)

        chosen_demand = self.participant.vars['chosen_demand']


        return {
            'highchart_series1': y1,'player_in_previous_rounds': players,
            'new_days': new_days, 'round_number': round_number, 'forecast_10': forecast_10, 'forecast_20': forecast_20,
            'chosen_demand': chosen_demand
        }

class Round_4(Page):
    form_model = 'player'
    form_fields = ['forecast_6m', 'forecast_1y']

    def before_next_page(self):
        p = self.player


        p.time_spent4 = (datetime.datetime.now() - p.participant.vars['time_previous']).total_seconds()

        p.participant.vars['time_previous'] = datetime.datetime.now()



    def vars_for_template(self):
        y1 = Constants.determined_series[self.player.participant.vars['chosen_demand']][:]
        players = self.player.in_previous_rounds()
        new_days = 270 + (self.round_number - 1) * 10
        round_number = self.round_number

        forecast_10 = self.player.forecast_10
        forecast_20 = self.player.forecast_20
        forecast_30 = self.player.forecast_30
        round_operator1 = 0

        while round_operator1 < 30:
            round_operator1 = round_operator1 + 1
            y1.append(None)

        chosen_demand = self.participant.vars['chosen_demand']

        return {
            'highchart_series1': y1,'player_in_previous_rounds': players,
            'new_days': new_days, 'round_number': round_number, 'forecast_10': forecast_10, 'forecast_20': forecast_20,
            'forecast_30': forecast_30, 'chosen_demand': chosen_demand
        }


class Results(Page):
    def app_after_this_page(self, upcoming_apps):
        return upcoming_apps[-1]

    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [
    Comprehension,
    Intro,
    Round_1,
    Round_2,
    Round_3,
    Round_4,
    Results
]
