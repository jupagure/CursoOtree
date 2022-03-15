from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

mturk_hit_settings = {
    'keywords': ['reward','bonus', 'study'],
    'title': 'Decision Making / $0.5 reward + bonus (average on $0.5) / Not for portable devices',
    'description': 'We are conducting research on decision making. During the experiment, your task is to make forecasting decisions and answer a questionnaire. No prior knowledge in forecasting is required. Participation will take approximately 15 minutes and you will be paid a participation fee of 0.5 USD. Please note that we do not allow connection from a portable device, e.g., cell phone, tablet. You will not be able to access our experiment if you are connecting from a portable device.',
    'frame_height': 800,
    'template': 'global/mturk_template.html',
    'minutes_allotted_per_assignment': 30,
    'expiration_hours': 96, # 7 days
    'grant_qualification_id': '39XUM4N2MLV6R1N4UEVL3XYZFJGKH9',
       'qualification_requirements': [
        {
            'QualificationTypeId': "00000000000000000071",
            'Comparator': "EqualTo",
            'LocaleValues': [{'Country': "US"}]
        },
        {
            'QualificationTypeId': "00000000000000000040",
            'Comparator': "GreaterThanOrEqualTo",
            'IntegerValues': [100]
        },
        {
            'QualificationTypeId': "000000000000000000L0",
            'Comparator': "GreaterThanOrEqualTo",
            'IntegerValues': [99],
        },
        {
            'QualificationTypeId': "39XUM4N2MLV6R1N4UEVL3XYZFJGKH9",
            'Comparator': "DoesNotExist",
        },
    ]
}

SESSION_CONFIG_DEFAULTS = {
    'mturk_hit_settings': mturk_hit_settings,
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.50,
    'doc': "",
}


SESSION_CONFIGS = [
    {
        'name': 'judgmental',
        'display_name': "judgmental",
        'num_demo_participants': 50,
        'app_sequence': ['intro', 'increasing_t1', 'increasing_t2', 'decreasing_t1', 'decreasing_t2','survey'],
    }
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True
POINTS_DECIMAL_PLACES = 2
POINTS_CUSTOM_NAME = 'dollars'
ROOMS = []



AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')

ADMIN_USERNAME = 'MSK'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = environ.get('OTREE_SECRET_KEY')
#SECRET_KEY = '@ri=%t0qex-=f$)7v_v$thogqko^ulz*p^m(0y5$k13!9qc6j+'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
