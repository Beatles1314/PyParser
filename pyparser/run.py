#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# run.py
# @Author : PengYingzhi
# @Date   : 10/17/2018, 10:39:05 AM


import click


@click.group()
def main():
    pass


@main.command()
def redis_monitors():
    """
        Run redis monitors.
    """
    from pyparser.cores.redis_monitor import ItemRedisMonitorManager

    manager = ItemRedisMonitorManager()
    manager.run()


@main.command()
def script_manager():
    """
        Run script manager.
    """
    from pyparser.parse_scripts import ScriptManager

    script_manager = ScriptManager()
    script_manager.run()


if __name__ == '__main__':
    main()
