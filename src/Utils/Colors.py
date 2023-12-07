class Colors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'

    @staticmethod
    def color_text(text, color):
        return f'{color}{text}{Colors.RESET}'

    @staticmethod
    def red(text):
        return Colors.color_text(text, Colors.RED)

    @staticmethod
    def green(text):
        return Colors.color_text(text, Colors.GREEN)

    @staticmethod
    def yellow(text):
        return Colors.color_text(text, Colors.YELLOW)

    @staticmethod
    def blue(text):
        return Colors.color_text(text, Colors.BLUE)

    @staticmethod
    def magenta(text):
        return Colors.color_text(text, Colors.MAGENTA)

    @staticmethod
    def cyan(text):
        return Colors.color_text(text, Colors.CYAN)

    @staticmethod
    def white(text):
        return Colors.color_text(text, Colors.WHITE)