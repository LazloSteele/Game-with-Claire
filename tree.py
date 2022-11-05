from plant import Plant

class Tree(Plant):
    def __init__(self):
        super().__init__()
    
        self._wood = NotImplemented
        self._bark = NotImplemented
        self._leaves = NotImplemented
        self._flowers = NotImplemented
        self._fruit = NotImplemented

        self._features = [self._bark, self._leaves, self._flowers, self._fruit]

    def render(self):
        self.features.append(f'{random.choice(self._bark)} bark')

