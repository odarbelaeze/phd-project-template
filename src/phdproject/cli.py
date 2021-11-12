import click


@click.group()
def main():
    """
    My phd project in cli
    """


@main.group()
def first_data():
    """
    Manage first data.
    """


@first_data.command()
def decompress():
    """
    De compress the data using such and such algorithm.
    """
    click.secho("Done decompressing!", fg="green")


@main.command()
def algo():
    """
    Do some special processing.
    """
    click.secho("Done!", fg="green")


if __name__ == "__main__":
    main()
