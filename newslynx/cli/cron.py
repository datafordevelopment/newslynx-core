import sys
import os
from inspect import isgenerator

import click
from colorama import Fore
import argparse

def setup(parser):
    """
    Install this parser. Basic for now.
    """
    from newslynx import settings

    cron_parser = parser.add_parser("cron", help="Spawns the dynamic scheduling daemon.")
    cron_parser.add_argument('-r', '--refersh-interval', dest='interval',
        type=int, default=settings.SCHEDULER_REFRESH_INTERVAL)
    return 'cron', run

def run(opts, log, **kwargs):
    from newslynx.scheduler import RecipeScheduler
    scheduler = RecipeScheduler(log=log, **kwargs)
    scheduler.run(**kwargs)