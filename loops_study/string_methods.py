SHOWS = [
    " Avatar: The last airbender",
    "Ben 10",
    "Arthur",
    " Spongebob Squarepants",
    "phineas and ferb",
    "Kim possible",
    "jimmy Neutron",
    "the Proud family "
]


def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append((show.title().strip()))

    print(', '.join(cleaned_shows))


main()