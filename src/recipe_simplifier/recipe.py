

class Recipe:
    """ add docstring """

    def __init__(self, title, ingredients, instructions):
        """ add docstring """
        self.title = title
        self.ingredients = ingredients 
        self.instructions = instructions
    
    def print(self):
        """ add docstring """
        print(self.title.title())
        print("\nINGREDIENTS:")
        for i in self.ingredients:
            print("-", i)
        print("\nINSTRUCTIONS:")
        if "\n" in self.instructions:
            for i, step in enumerate(self.instructions.splitlines()):
                print(f"{i+1}. {step}")
        else:
            for i, step in enumerate(self.instructions.split('. ')):
                print(f"{i+1}. {step}")
    
    def display(self):
        """ add docstring """
        # add code to open nice html in browser 