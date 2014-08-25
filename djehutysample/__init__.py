from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.scan('djehutysample.services')
    return config.make_wsgi_app()
