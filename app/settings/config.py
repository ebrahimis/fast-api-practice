from os import getenv


def get_database_url():
    """
    Generate sqlalchemy database url from env vars.
    """
    host = getenv('DB_HOSTNAME', 'fast-api-postgres')
    port = getenv('DB_PORT', '5432')
    database = getenv('DB_NAME', 'postgres')
    user = getenv('DB_USERNAME', 'postgres')
    password = getenv('DB_PASSWORD', 'password')

    return 'postgresql://{}:{}@{}:{}/{}'.format(
        user,
        password,
        host,
        port,
        database
    )


class Config:
    """
    Base config class.
    """
    APP_VERSION = getenv('APP_VERSION', '0.0.1')
    SQLALCHEMY_DATABASE_URI = get_database_url()    


class DevelopmentConfig(Config):
    APP_ENV = 'development'


class TestingConfig(Config):
    APP_ENV = 'testing'


class ProductionConfig(Config):
    APP_ENV = 'production'


config_by_env = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}


def get_environment_config() -> Config:
    return config_by_env[getenv('APP_ENV', 'development')]
