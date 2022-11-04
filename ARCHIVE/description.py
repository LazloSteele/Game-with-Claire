import tracery as t
from tracery.modifiers import base_english
import json
import os

class description:
    def __init__(self, rules_file: json):
        self._rules = None

        self.import_grammar(rules_file)

    @property
    def rules(self):
        return self._rules

    def import_grammar(self, rules_file):
        with open(rules_file) as f:
            self._rules = json.load(f)
        self._grammar = t.Grammar(self.rules)
        self._grammar.add_modifiers(base_english)

    def set_scene(self):
        print(self._grammar.flatten("#on_enter#"))

if __name__ == '__main__':
    d = description('rules.json')
    d.set_scene()
