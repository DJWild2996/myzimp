from abstract_commands import AbstractCommands
import random
import pandas as pd
from dev_card import DevCard


# Product C
class LoadCards(AbstractCommands):
    def command(self):
        try:
            card_data = pd.read_excel('DevCards.xlsx')
            for card in card_data.iterrows():
                item = card[1][0]
                event_one = (card[1][1], card[1][2])
                event_two = (card[1][3], card[1][4])
                event_three = (card[1][5], card[1][6])
                charges = card[1][7]
                dev_card = DevCard(item, charges, event_one, event_two, event_three)
                self.dev_cards.append(dev_card)
            random.shuffle(self.dev_cards)
            self.dev_cards.pop(0)
            self.dev_cards.pop(0)

        except FileNotFoundError as e:
            print("ERROR: File not found please check Excel file name", e)
        except OSError as e:
            print("ERROR: Unable to access file please check file location", e)
