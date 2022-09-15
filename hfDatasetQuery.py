#!/usr/bin/env python
from hlib.loader import search, inspect_data
import click
from random import choice

COLORS = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]

# build function that yields a random color not used sequentially
def random_non_sequential_color():
    last_color = None
    color = None
    while True:
        if color == last_color:
            color = choice(COLORS)
        last_color = color
        yield color


# build click group
@click.group()
def cli():
    """Hugging Face Dataset Query Tool"""


# build click command
@cli.command("query")
@click.argument("pattern")
@click.option("--limit", default=10, help="Limit the number of results")
@click.option("--sort", default=True, help="Sort the results")
def query(pattern, limit, sort):
    """Search for a Hugging Face dataset by name or description.

    Example: ./hf-dataset-query.py query 'squad' --limit 5 --sort True
    """

    datasets = search(pattern, limit, sort)
    color = random_non_sequential_color()
    for dataset in datasets:
        # print colored dataset name
        print(click.style(dataset, fg=next(color)))


# build click command
@cli.command("inspect")
@click.argument("dataset")
@click.option("--column", default="train", help="Column to inspect")
@click.option("--rows", default=5, help="Number of rows to inspect")
def inspect(dataset, column, rows):
    """Inspect a Hugging Face dataset.

    Example: ./hf-dataset-query.py inspect squad --column train --rows 5
    """

    data = inspect_data(dataset, column, rows)
    print(data)


if __name__ == "__main__":
    cli()
