from viewers import viewers_group
from converters import converters_group
from rich.table import Table
from rich.logging import RichHandler
from rich.console import Console
import click
from datetime import datetime
import logging
import os
import sys

# Get the absolute path of the parent directory (CLI-using-Click)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the CLI directory to the Python path
sys.path.append(os.path.join(project_root, 'CLI'))


# import converters_group

# import viewers_group

# initialize log
log = logging.getLogger(__name__)
logging.basicConfig(
    level="NOTSET",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True, tracebacks_suppress=[click])],
)
log = logging.getLogger("rich")
console = Console()


@click.command(name="logging")
def logging1():
    """this will log hello world"""
    log.info("hello, info")
    log.debug("hello, debug")
    log.warning("hello, warning")
    log.error("hello, error")
    log.critical("hello, critical")
    log.fatal("hello, fatal")
    log.exception("hello, exception")
    # log.success("hello, success")
    log.log(logging.INFO, "hello, log")


@click.command(name="table")
def richTable():
    """this will print table"""
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Date", style="dim", width=12)
    table.add_column("Title")
    table.add_column("Production Budget", justify="right")
    table.add_column("Box Office", justify="right")
    table.add_row(
        "Dec 20, 2019",
        "Star Wars: The Rise of Skywalker",
        "$275,000,000",
        "$375,126,118",
    )

    table.add_row(
        "May 25, 2018",
        "[red]Solo[/red]: A Star Wars Story",
        "$275,000,000",
        "$393,151,347",
    )
    table.add_row(
        "Dec 15, 2017",
        "Star Wars Ep. VIII: The Last Jedi",
        "$262,000,000",
        "[bold]$1,331,539[/bold]",
    )

    console.print(table)


@click.command()
def date():
    """this will print the current date"""
    click.echo(datetime.now().date().isoformat())


@click.command()
def time():
    """this will print the current time"""
    click.echo(datetime.now().time().isoformat())


@click.command(name="hello")
def printName():
    """this will print Hi"""
    console.print("Hi :hand: [bold green]there[/bold green]")


@click.group()
def main_cli():
    pass


main_cli.add_command(date)
main_cli.add_command(time)
main_cli.add_command(printName)
main_cli.add_command(logging1)
main_cli.add_command(richTable)
main_cli.add_command(converters_group)
main_cli.add_command(viewers_group)
