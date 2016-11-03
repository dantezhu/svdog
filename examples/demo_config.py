# -*- coding: utf-8 -*-


LOG_FORMAT = '\n'.join((
    '/' + '-' * 80,
    '[%(levelname)s][%(asctime)s][%(process)d:%(thread)d][%(filename)s:%(lineno)d %(funcName)s]:',
    '%(message)s',
    '-' * 80 + '/',
))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,

    'formatters': {
        'standard': {
            'format': LOG_FORMAT,
        },
    },

    'handlers': {
        'flylog': {
            'level': 'ERROR',
            'class': 'flylog.LogHandler',
            'formatter': 'standard',
            'source': 'svdog',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
    },

    'loggers': {
        'svdog': {
            'handlers': ['console', 'flylog'],
            'level': 'ERROR',
            'propagate': False
        },
    }
}

