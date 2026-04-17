import tempfile
import webbrowser
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
        
        # separate out instructions 
        if "\n" in self.instructions:
            instructions = self.instructions.splitlines()
        else:
            instructions = self.instructions.split('. ')

        html = f"""<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{self.title}</title>
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Lora:wght@400;600&family=Inter:wght@400;500&display=swap');

                *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

                body {{
                    font-family: 'Inter', sans-serif;
                    background: #e6e8ff;
                    color: #2c2c2a;
                    min-height: 100vh;
                    padding: 32px clamp(24px, 5vw, 64px) 40px;
                }}

                .card {{
                    background: #fff;
                    width: min(95vw, 1100px);
                    margin: 0 auto;
                    border-radius: 16px;
                    overflow: hidden;
                    box-shadow: 0 2px 24px rgba(98,102,210,0.10);
                }}

                .header {{
                    background: #e11444;
                    padding: 40px clamp(24px, 5vw, 64px) 32px;
                    text-align: center;
                }}

                .header h1 {{
                    font-family: 'Lora', Georgia, serif;
                    font-size: 2rem;
                    font-weight: 600;
                    color: #ffffff;
                    letter-spacing: 0.01em;
                    line-height: 1.3;
                }}

                .body {{
                    padding: 40px 48px 48px;
                }}

                .section {{
                    margin-bottom: 36px;
                }}

                .section:last-child {{
                    margin-bottom: 0;
                }}

                h2 {{
                    font-family: 'Lora', Georgia, serif;
                    font-size: 1.1rem;
                    font-weight: 600;
                    color: #e11444;
                    text-transform: uppercase;
                    letter-spacing: 0.08em;
                    margin-bottom: 16px;
                    padding-bottom: 10px;
                    border-bottom: 1.5px solid #c7caee;
                }}

                ul {{
                    list-style: none;
                    display: grid;
                    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
                    gap: 8px;
                }}

                ul li {{
                    background: #f0f1ff;
                    border: 1px solid #c7caee;
                    border-radius: 8px;
                    padding: 10px 14px;
                    font-size: 0.9rem;
                    color: #2c2c3e;
                    line-height: 1.4;
                }}

                ol {{
                    list-style: none;
                    counter-reset: steps;
                    display: flex;
                    flex-direction: column;
                    gap: 12px;
                }}

                ol li {{
                    counter-increment: steps;
                    display: flex;
                    gap: 16px;
                    align-items: flex-start;
                    font-size: 0.95rem;
                    line-height: 1.65;
                    color: #2c2c3e;
                }}

                ol li::before {{
                    content: counter(steps);
                    min-width: 28px;
                    height: 28px;
                    background: #e11444;
                    color: #ffffff;
                    border-radius: 50%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 0.78rem;
                    font-weight: 500;
                    flex-shrink: 0;
                    margin-top: 1px;
                }}
            </style>
        </head>
        <body>
            <div class="card">
                <div class="header">
                    <h1>{self.title}</h1>
                </div>
                <div class="body">
                    <div class="section">
                        <h2>Ingredients</h2>
                        <ul>
                            {''.join(f'<li>{i}</li>' for i in self.ingredients)}
                        </ul>
                    </div>
                    <div class="section">
                        <h2>Instructions</h2>
                        <ol>
                            {''.join(f'<li>{step}</li>' for step in instructions)}
                        </ol>
                    </div>
                </div>
            </div>
        </body>
        </html>"""

        with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as f:
            Path(f.name).write_text(html, encoding="utf-8")
            temp_path = Path(f.name)
    
        full_path = f"file://{temp_path}"
        webbrowser.open(full_path)
        print(f"Opening at {full_path}.\n")
    
        try:
            input("Press Enter to exit...")
        finally:
            temp_path.unlink(missing_ok=True)