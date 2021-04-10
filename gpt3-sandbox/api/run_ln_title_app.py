"""Idea taken from https://www.notion.so/Analogies-Generator-9b046963f52f446b9bef84aa4e416a4c"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app


# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=100)

gpt.add_example(Example('My little sister',
                        "My little sister can't be this cute"))
gpt.add_example(Example('My romantic comedy',
                        'My romantic comedy is wrong, as expected'))
gpt.add_example(Example('Gods blessing', 'Gods blessing on this wonderful world!'))
gpt.add_example(Example('What do you do',
                        'What do you do at the end of the world? Are you busy? Will you save us?'))
gpt.add_example(Example('Reborn as',
                        'Reborn as a vending machine, now I wander the dungeon'))
gpt.add_example(Example('Is it wrong',
                        'Is it wrong to try to pick up girls in a dungeon?'))

# Define UI configuration
config = UIConfig(description="LN Title Generator",
                  button_text="Generate",
                  placeholder="Reborn as")

demo_web_app(gpt, config)