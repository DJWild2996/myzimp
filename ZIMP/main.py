import sys
from commands import Commands

if __name__ == "__main__":
    print("Number of command-line arguments: ", len(sys.argv))
    print(sys.argv[0])
    print("Welcome to Zombie in My Pocket type start to start playing the game, if you need help at any time type "
          "help Good Luck")
    commands = Commands()
    commands.cmdloop()

