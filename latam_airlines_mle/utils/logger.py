def get_logging_config(transaction_id=None):
    """create the log

    Args:
        transaction_id (_type_): _description_

    Returns:
        _type_: _description_
    """
    if transaction_id is None:
        transaction_id='000001'
    logging_config = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'standard': {
                "datefmt": '%Y-%m-%d %H:%M:%S %p',
                'format': f'%(asctime)s | %(levelname)s | LATAM AIRLINES MLE | %(module)s >> {transaction_id} | %(message)s'
            },
        },
        'handlers': {
            'default': {
                'formatter': 'standard',
                'class': 'logging.StreamHandler',
            },
        },
        'loggers': {
            '': {
                'handlers': ['default'],
                'level': 'INFO',
                'propagate': False
            }
        }
    }
    return logging_config