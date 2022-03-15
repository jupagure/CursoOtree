from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class First(Page):
    timeout_seconds = 0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001
    def before_next_page(self):


        self.participant.vars['forecasting'] = []
        self.participant.vars['demand'] = []
        self.participant.vars['ferror'] = []
        self.participant.vars['period'] = []
        self.participant.vars['absferror'] = []

        p = self.player
        p.ip_observed = self.request.META['REMOTE_ADDR']

        if self.participant.vars['chosen_app'] == 1:
            p.chosen_app = 1
        elif self.participant.vars['chosen_app'] == 2:
            p.chosen_app = 2
        elif self.participant.vars['chosen_app'] == 3:
            p.chosen_app = 3
        elif self.participant.vars['chosen_app'] == 4:
            p.chosen_app = 4

        if self.participant.vars['chosen_demand'] == 0:
            p.chosen_demand = 1
        elif self.participant.vars['chosen_demand'] == 1:
            p.chosen_demand = 2
        elif self.participant.vars['chosen_demand'] == 2:
            p.chosen_demand = 3




class Mobile(Page):
    def is_displayed(self):
        user_agent = self.request.META['HTTP_USER_AGENT']
        is_mobile = False
        for substring in ['Mobi', 'Android']:
            if substring in user_agent:
                self.participant.vars['mobilex'].append(2)

        if len(self.participant.vars['mobilex']) > 1:
            is_mobile = True
            return is_mobile

        return is_mobile


#class Ip(Page):
#    def is_displayed(self):
#       is_duplicate = False
#       for k in self.session.vars['ip']:
#            if self.player.ip_observed == k:
#               self.participant.vars['ip_check'].append(2)
#
#       if len(self.participant.vars['ip_check']) > 1:
#            is_duplicate = True
#            return is_duplicate
#
#       return is_duplicate

class Intro(Page):
    def vars_for_template(self):
        players = self.player.in_previous_rounds()

        chosen_app = self.participant.vars['chosen_app']
        chosen_demand = self.participant.vars['chosen_demand']
        return {
            'player_in_previous_rounds': players,
            'chosen_app': chosen_app, 'chosen_demand': chosen_demand
        }

class Intro2(Page):
    def app_after_this_page(self, upcoming_apps):
        if self.participant.vars['chosen_app'] == 1:
            return upcoming_apps[0]
        elif self.participant.vars['chosen_app'] == 2:
            return upcoming_apps[1]
        elif self.participant.vars['chosen_app'] == 3:
            return upcoming_apps[2]
        elif self.participant.vars['chosen_app'] == 4:
            return upcoming_apps[3]


    def vars_for_template(self):
        players = self.player.in_previous_rounds()



        chosen_app = self.participant.vars['chosen_app']
        chosen_demand = self.participant.vars['chosen_demand']
        return {
            'player_in_previous_rounds': players,
            'chosen_app': chosen_app, 'chosen_demand': chosen_demand
        }


page_sequence = [
    Mobile,
    First,
    Intro,
    Intro2
]
