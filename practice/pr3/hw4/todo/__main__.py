# Main file. Contains program execution logic.

from custom_exceptions import UserExitException
from runtime import parse_user_input, perform_command


def main():
    """
    Main method.

    Works infinitely until user runs `exit` command.
    Or hits `Ctrl+C` in the console.
    """
    while True:
        try:
            perform_command(parse_user_input())
        except UserExitException:
            break
        except Exception as ex:
            print(  # noqa: WPS421
                'You have done something wrong!',
                ex,
                type(ex),
            )


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Shutting down, bye!')  # noqa: WPS421
