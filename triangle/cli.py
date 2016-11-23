import click


@click.group(context_settings=dict(help_option_names=['-h', '--help']))
def cli():
    pass


@cli.command()
@click.argument('first_length', type=float)
@click.argument('second_length', type=float)
@click.argument('third_length', type=float)
def check(first_length, second_length, third_length):
    """check type of triangle."""
    output = analyse(first_length, second_length, third_length)
    click.echo('OUTPUT: {output}'.format(output=output))


def analyse(a: float, b: float, c: float) -> str:
    """
    Check type of triangle.

    :param a: first length
    :param b: second length
    :param c: third length
    :return: Type of triangle
    """
    a_quadrat = a * a
    b_quadrat = b * b
    c_quadrat = c * c

    # Example: 3, 4, 7
    if (a >= b + c) or (b >= a + c) or (c >= a + b):
        output = 'Not a triangle!'
    # Example: 3, 3, 3
    elif a == b and b == c:
        output = 'Equilateral'
    # Example: 3, 3, 1
    elif a == b or b == c or a == c:
        output = 'Isosceles'
    # Example: 3, 4, 5
    elif (a_quadrat + b_quadrat == c_quadrat) or (a_quadrat + c_quadrat == b_quadrat) or (
            b_quadrat + c_quadrat == a_quadrat):
        output = 'Scalene'
    # Example: 3, 5, 7
    else:
        output = 'TODO <other type of triangle>'

    return output

if __name__ == '__main__':
    cli()
