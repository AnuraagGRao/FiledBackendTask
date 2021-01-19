 #/instance/config.py


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = 'TemporarySecretCode'


class DevelopmentConfig(Config):
    """Config for Development."""
    DEBUG = True


class TestingConfig(Config):
    """Config for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True


class StagingConfig(Config):
    """Config for Staging."""
    DEBUG = True


class ProductionConfig(Config):
    """Config for Production."""
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}