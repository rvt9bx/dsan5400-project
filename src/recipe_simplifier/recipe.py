

class Recipe:
    """ add docstring """

    def __init__(self, title, ingredients, instructions):
        """ add docstring """
        self.title = title
        self.ingredients = ingredients 
        self.instructions = instructions.splitlines()
    
    def print(self):
        """ add docstring """
        print(self.title.title())
        print("\nINGREDIENTS:")
        for i in self.ingredients:
            print("-", i)
        print("\nINSTRUCTIONS:")
        for i, step in enumerate(self.instructions):
            print(f"{i+1}. {step}")
    
    def display(self):
        """ add docstring """
        # add code to open nice html in browser 