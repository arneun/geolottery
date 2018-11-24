

from distutils.core import setup

setup(
        name='Geolottery',
        modules = ['bets', 'map', 'prices', 'random', 'user'],
        install_requires=['flask', 'flask-login']
        )


