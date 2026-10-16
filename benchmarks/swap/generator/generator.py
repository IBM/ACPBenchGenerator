#!/usr/bin/env python
import itertools
import sys
import random

def get_agents(num, random):
    names = ["Alice", "Bob", "Carol", "Dave", "Erin", "Frank", "Grace", "Heidi", "Ivan", "Judy", "Kevin", "Liam", "Michelle", "Nicole", "Olivia", "Pat", "Quentin", "Richard", "Steve", "Ted", "Una", "Vic", "Wade", "Xena", "Yana", "Zoe"]
    return random.sample(names,k=num)


def get_roles(num, random):
    d = {
        "c_suite_job" : ['CAO', 'CBO', 'CCO', 'CDO', 'CEO', 'CFO', 'CGO', 'CHRO', 'CIO', 'CKO', 'CLO', 'CMO', 'CNO', 'COO', 'CPO', 'CRO', 'CSO', 'CTO', 'CUO', 'VCO', 'WCO', 'XCO', 'YCO', 'ZCO'],
        "fruit" : ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape", "Honeydew", "Imbu", "Jackfruit", "Kiwi", "Lemon", "Melon", "Nectarine", "Orange", "Plum", "Quince", "Raspberry", "Strawberry", "Tangerine", "Umari", "Vanilla", "Watermelon", "Xigua", "Yuzu", "Zill"],
        "vegetable" :  ['Artichoke', 'Beet','Cabbage', 'Dandelion', 'Eggplant',  'Fennel', 'Garlic', 'Horseradish', 'Iceplant', 'Jicama', 'Kale', 'Leek', 'Mushroom',  'Nopales', 'Okra', 'Parsnip', 'Quince', 'Radish', 'Spinach', 'Tomato', 'Ulluco', 'Valerian', 'Watercress', 'Xigua', 'Yam', 'Zucchini'],
        "tool" : ["Axe", "Backsaw", "Cable", "Drill", "Edger", "Funnel", "Grinder", "Hammer", "Icepick", "Jigsaw", "Knead", "Level", "Mallet", "Nibbler", "Outlet", "Pliers", "Q-Saw", "Ratchet", "Sander", "Trowel", "Ubolt", "Vise", "Wrench", "XActoKnife", "Yardstick", "Zester"],
        "toy" : ["Airplane", "Ball", "Car", "Doll", "Elephant", "Frisbee", "Guitar", "HulaHoop", "IceSkates", "JigsawPuzzle", "Kaleidoscope", "Lego", "Marble", "Necklace", "Octopus", "PlayDoh", "Quadcopter", "Rocketship", "Slinky", "TeddyBear", "Unicorn", "Volleyball", "Whale", "Xylophone", "Yo-Yo", "Zebra"],
        "instrument" : ["Accordion", "Banjo", "Cello", "Drums", "Ektara", "Flute", "Glockenspiel", "Harmonica", "Ibanez", "Jazzophone", "Kazoo", "Lyre", "Mandolin", "Nai", "Oboe", "Piano", "Quena", "Recorder", "Saxophone", "Tambourine", "Ukulele", "Viola", "Washboard", "Xylophone", "Yaogu", "Zither"],
        "book" : [],
        # "role" : [],
        # "partner" : ['Alex', 'Blake', 'Cameron', 'Danielle', 'Eleanor', 'Flora', 'Gabriel', 'Harrison', 'Isabella', 'Julian', 'Katherine', 'Lucas', 'Margo', 'Natalie', 'Owen', 'Piper', 'Quincy', 'Rebecca', 'Sawyer', 'Tessa', 'Ursula', 'Vivian', 'Winston', 'Xanthe', 'Yolanda', 'Zelda']
    }
    r = random.choice(list(d.keys()))
    print(r)
    if r in ["book", "role"]:
        return [f"{r}{count+1:02}" for count in range(num)]
    return random.sample(d[r],k=num)


def get_agents_roles(num, random):
    roles = get_roles(num, random)
    # roles = ["role"+str(r + 1) for r in range(num_roles)]
    agents = get_agents(num, random)
    # agents = ["agent"+str(agent + 1) + " " for agent in range(num_agents)]
    return agents, roles


def get_objects(agents, roles):
    return " ".join(roles) + " - role\n " + " ".join(agents)+ " - agent "

def get_init(agents, roles):
    init = []
    for i, a in enumerate(agents):
        r = roles[i]
        init.append(f" (assigned {a} {r}) ")

    for a, b in itertools.combinations(agents, 2):
        init.append(f" (not-eq {a} {b}) ")
        init.append(f" (not-eq {b} {a}) ")

    for a, b in itertools.combinations(roles, 2):
        init.append(f" (not-eq {a} {b}) ")
        init.append(f" (not-eq {b} {a}) ")

    return "\n".join(init)


def get_goals(agents, roles):
    # make sure goal is not the same as init
    goal = []
    goal_assignment = roles[1:] + [roles[0]]

    for i, a in enumerate(agents):
        r = goal_assignment[i]
        goal.append(f" (assigned {a} {r}) ")
    return "(and " + "\n".join(goal) + ")"


def main(name, num_agents, seed = None):
    assert(num_agents <= 26)

    if seed:
        random.seed(seed)

    agents, roles = get_agents_roles(num_agents, random)
    print(agents, roles)

    ret = str("(define (problem " + name + ")\n") + \
    str(" (:domain swap)\n") + \
    str(" (:objects " + get_objects(agents, roles) + ")\n") + \
    str(" (:init \n" + get_init(agents, roles) + ")\n") + \
    str(" (:goal \n" + get_goals(agents, roles) + ")\n") + \
    str(")")
    return ret


if __name__ == "__main__":
    # Reading the command line arguments
    try:
        name = sys.argv[1]
        num_roles = int(sys.argv[2])
        num_agents = int(sys.argv[3])

        if len(sys.argv) == 5:
            seed = int(sys.argv[4])
        else:
            seed = None


    except BaseException:
        print(
            "Usage: "
            + sys.argv[0]
            + " <name> <num_agents> [<seed>]"
        )
        sys.exit(1)

    print(main(name, num_agents, seed))
