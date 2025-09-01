import random, threading, playsound


SOUNDS = {
    "🟥": "sfx/live.wav",
    "🟦": "sfx/blank.wav"
}
PRESETS_MANY = [
# 1L1B (2), 1L2B (3), 2L2B (4), 2L3B (5) , 3L3B (6), 3L4B (7), and 4L4B (8)   [reddit]
# (4, 4), (4, 3), (3, 1), (1, 1), (2, 3), (3, 3), (3, 2)   [markiplier]
#    L  B
    (3, 3),
    (3, 4),
    (4, 3),
    (4, 4),
    (5, 4),
    (5, 5),
    (5, 6),
]
PRESETS_FEW = [
    (1, 1),
    (1, 2),
    (2, 1),
    (2, 2),
    (2, 3),
    (3, 1),
    (3, 2),
]
INVERT = {"🟥": "🟦", "🟦": "🟥"}
wrap = lambda s: f"[ {s} ]"
header = lambda s: f"==== {s} ====\n"
clear = lambda: print("\n"*100)


def play(sound):
    thread = threading.Thread(target=playsound.playsound, args=(SOUNDS[sound],), daemon=True)
    thread.start()


def phone(chamber):
    n = len(chamber)
    if n >= 3:
        pos = random.randint(3, n)
        return f"POS {pos}: {chamber[::-1][pos-1]}"
    else:
        return "HOW UNFORTUNATE..."


def load():
    lives, blanks = random.choice(PRESETS_MANY)

    show = f"{lives} LIVE // {blanks} BLANK"
    chamber = ["🟥"] * lives + ["🟦"] * blanks
    random.shuffle(chamber)
    return chamber, show


def get_rows(options, n):
    rows = [[] for i in range(n)]
    for i, option in enumerate(options):
        rows[i % n].append(f"{f"[{i}] {option}":<15}")
    return rows


def output_options(options):
    rows = get_rows(options, 4)
    for row in rows:
        print(*row)


def select(*options):
    valid = False
    choice = 0
    while not valid:
        output_options(options)

        choice = input()
        if choice == "":
            choice = 0
        try:
            choice = int(choice)
            valid = 0 <= choice < len(options)
        except ValueError:
            pass

        print()

    return options[choice]


def init_round(new_game):
    if new_game:
        charges = random.randint(3, 5)
        print(charges, "CHARGES")

        # if random.randint(1, 5) <= 2 < len(players):
        #     team = random.sample(players, 2)
        #     print(f"\nTEAM-UP: {team[0]} AND {team[1]}")

        print()

    print(f"DRAW {random.randint(2, 4)} ITEMS")
    input()


def new_round(new_game=False):
    print(header("ROUND START"))

    init_round(new_game)

    chamber, show = load()
    previous = chamber[:]
    print(show)
    input()
    clear()

    while chamber:
        choice = select(
            "FIRE",
            "EJECT",
            "INVERTER",
            "GLASS",
            "PHONE",
            "MEDICINE",
            "UNDO",
            "END",
            "! SHELL COUNT",
            "! SHOW",
            "! FULL VIEW"
        )


        if choice in ["FIRE", "EJECT"]:
            previous = chamber[:]
            shot = chamber.pop()
            print(shot)
            if choice == "FIRE":
                play(shot)

        elif choice == "INVERTER":
            previous = chamber[:]
            chamber[-1] = INVERT[chamber[-1]]
            print("POLARITY SWAPPED")

        elif choice in ["GLASS", "PHONE"]:
            if choice == "GLASS":
                print(wrap(chamber[-1]))
            else:
                print(wrap(phone(chamber)))

            input()
            clear()

        elif choice == "MEDICINE":
            print(random.choice(["+2 HEALTH", "-1 HEALTH"]))

        elif choice == "UNDO":
            if chamber == previous:
                chamber = previous
                print("RESTORED LAST SHELL")
            else:
                print("UNABLE TO RESTORE")

        elif choice == "END":
            chamber = []
            print("ENDING ROUND")

        elif choice == "! SHELL COUNT":
            print(wrap(len(chamber)))
            input()
            clear()

        elif choice == "! SHOW":
            print(f"{chamber.count("🟥")} LIVE // {chamber.count("🟦")} BLANK")
            input()
            clear()

        elif choice == "! FULL VIEW":
            print(wrap(chamber))
            input()
            clear()

        print()


    print(header("ROUND END"))


def main():
    print(header("CHAMBERED STEEL"))

    new_round(new_game=True)
    while True:
        choice = select(
            "NEXT ROUND",
            "NEW GAME",
            "EXIT"
        )

        if choice == "NEXT ROUND":
            new_round()
        elif choice == "NEW GAME":
            new_round(new_game=True)
        elif choice == "EXIT":
            break


if __name__ == "__main__":
    main()
