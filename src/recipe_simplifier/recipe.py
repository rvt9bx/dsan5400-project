import tempfile
import webbrowser
import os
from pathlib import Path

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

        html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>{self.title}</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: 40px auto;
                    line-height: 1.6;
                    background: #fafafa;
                    color: #333;
                }}
                h1 {{
                    text-align: center;
                }}
                h2 {{
                    margin-top: 30px;
                    border-bottom: 2px solid #eee;
                    padding-bottom: 5px;
                }}
                ul, ol {{
                    padding-left: 20px;
                }}
                li {{
                    margin-bottom: 8px;
                }}
                .card {{
                    background: white;
                    padding: 30px;
                    border-radius: 10px;
                    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
                }}
            </style>
        </head>
        <body>
            <div class="card">
                <h1>{self.title}</h1>

                <h2>Ingredients</h2>
                <ul>
                    {''.join(f"<li>{i}</li>" for i in ingredients)}
                </ul>

                <h2>Instructions</h2>
                <ol>
                    {''.join(f"<li>{step}</li>" for step in instructions)}
                </ol>
            </div>
        </body>
        </html>
        """

        with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as f:
            f.write(html.encode("utf-8"))
            temp_path = Path(f.name)

        webbrowser.open(f"file://{temp_path}")


# Example usage
title = "Tortilla Breakfast Bake"
ingredients = [
    "6 eggs",
    "1 cup milk",
    "2 tortillas",
    "1 cup cheese"
]
instructions = [
    "Preheat oven to 375°F",
    "Mix eggs and milk",
    "Layer tortillas and cheese",
    "Bake for 25 minutes"
]

open_recipe_in_browser(title, ingredients, instructions)

        
        # get absolute path to file
        filename = 'result.html'
        file_path = os.path.abspath(filename)

        # open in the default browser
        webbrowser.open(f'file://{file_path}')