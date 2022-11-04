from tree import Tree

class Elm(Tree):
    def __init__(self):
        super().__init__()

        self._name = 'Elm Tree'
        
        self._growth_habit = super().erect()
        self._water_requirement = 'LOW'
        self._cold_hardiness = [4, 9]
        self._seasons = {'WINTER': {'FOLIAGE': False, 'FLOWER': False, 'FRUIT': False}, 'SPRING': {'FOLIAGE': True, 'FLOWER': True, 'FRUIT': False}, 'SUMMER': {'FOLIAGE': True, 'FLOWER': False, 'FRUIT': True}, 'AUTUMN': {'FOLIAGE': True, 'FLOWER': False, 'FRUIT': False}}

        self._wood = 'HARDWOOD'
        self._bark = ['rough', 'jagged', 'cracking', 'intricate', 'ancient', 'layered', 'crumbling', 'grey', 'tawny', 'ashy', 'burnt']
        self._leaves = ['serrated', 'emerald', '']
        self._flowers = ['pink clusters that burst forth all through the branches']
        self._fruit = ['hairy seedpod with little appeal']

        
        self._descriptors = {'sturdy', 'thick', 'majestic', 'tall', 'stunted', 'wicked', 'plain', 'lonely'}
