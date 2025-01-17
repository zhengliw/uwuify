import click

from uwuify import SMILEY, YU, uwu, STUTTER


def allow_pipe(ctx, param, value):
    if not value and not click.get_text_stream("stdin").isatty():
        pipped = click.get_text_stream("stdin").read().strip()
        return pipped.split(" ")  # Compatibility with -1 garbage
    else:
        return value


@click.command(help="Command line uwuification.")
@click.option("--smiley", is_flag=True, help="Add smileys on puntuation.")
@click.option("--yu", is_flag=True, help="Replace u with yu")
@click.option(
    "--stutter",
    help="Add stutter for every 4-th word.",
    is_flag=True,
    type=int
)
@click.argument("text", nargs=-1, callback=allow_pipe)
def main(smiley, yu, text, stutter):
    text = " ".join(text)
    flags = 0

    if smiley:
        flags |= SMILEY

    if yu:
        flags |= YU

    if stutter:
        flags |= STUTTER

    uwuified = uwu(text, flags=flags)
    click.echo(uwuified)
