import click

ALLOWED = '+-<>,.[]'


@click.command(help='Minify your Brainf files.')
@click.argument(
    'source',
    type=click.Path(exists=True,
                    file_okay=True,
                    dir_okay=False),
)
@click.argument(
    'target',
    type=click.Path(file_okay=True,
                    dir_okay=False),
)
def minify(source, target):
    with open(source) as src:
        chars = src.read()
    with open(target, 'w') as trg:
        for c in chars:
            if c in ALLOWED:
                trg.write(c)

