builtin_print = print  # 备份默认print函数
builtin_input = input  # 备份默认input函数
try:
    import colorama

    changeRule: list[tuple] = [
        ("[red]", colorama.Fore.RED),
        ("[green]", colorama.Fore.GREEN),
        ("[yellow]", colorama.Fore.YELLOW),
        ("[blue]", colorama.Fore.BLUE),
        ("[magenta]", colorama.Fore.MAGENTA),
        ("[cyan]", colorama.Fore.CYAN),
        ("[white]", colorama.Fore.WHITE),
        ("[/]", colorama.Fore.RESET),
    ]

except ImportError:
    print(
        "colorama没有安装，无法使用彩色输出。建议使用pip install colorama安装colorama。"
    )
    changeRule: list[tuple] = [
        ("[red]", ""),
        ("[green]", ""),
        ("[yellow]", ""),
        ("[blue]", ""),
        ("[magenta]", ""),
        ("[cyan]", ""),
        ("[white]", ""),
        ("[/]", ""),
    ]


def print(*args, **kwargs):
    data = "".join(args)
    for rule in changeRule:
        data = data.replace(rule[0], rule[1])
    if not data.endswith(colorama.Fore.RESET):
        data += colorama.Fore.RESET
    builtin_print(data, **kwargs)


def input(*args, **kwargs):
    data = "".join(args)
    for rule in changeRule:
        data = data.replace(rule[0], rule[1])
    return builtin_input(data, **kwargs)


if __name__ == "__main__":
    print("[red]红色[/]")
