from elm import Elm

class TreeFactory():
    @staticmethod
    def generate_tree(tree):
        try:
            if plan == 'ELM':
                return Elm()
            raise AssertionError("Tree is not valid")
        except AssertionError as e:
            print(e)
        
