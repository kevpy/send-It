# import os


# class TestEnvConfigs(object):
#     @staticmethod
#     def test_development_config(client):
#         client.config.from_object('instance.config.DevelopmentConfig')
#         assert client.config['DEBUG']
#         assert not client.config['TESTING']
#         assert client.config['DATABASE_URL'] == os.environ.get('APP_DB_URI')

#     @staticmethod
#     def test_testing_config(client):
#         client.config.from_object('instance.config.TestingConfig')
#         assert client.config['DEBUG']
#         assert client.config['TESTING']
#         assert not client.config['PRESERVE_CONTEXT_ON_EXCEPTION']
#         assert client.config['DATABASE_URL'] == os.environ.get('TEST_DB_URI')

#     @staticmethod
#     def test_production_config(client):
#         client.config.from_object('instance.config.ProductionConfig')
#         assert not client.config['DEBUG']
#         assert not client.config['TESTING']
