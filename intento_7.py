import os
import json
import requests
from tkinter import (
    Tk, Label, Entry, Button, messagebox, Text, Scrollbar, RIGHT, Y, BOTH, Toplevel
)
from PIL import Image, ImageTk
from io import BytesIO


def get_pokemon_data(pokemon_name):
    """Fetches data for a given Pokémon from the PokeAPI."""
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return {
            "name": data['name'],
            "weight": data['weight'],
            "height": data['height'],
            "moves": [move['move']['name'] for move in data['moves']],
            "abilities": [ability['ability']['name'] for ability in data['abilities']],
            "types": [poke_type['type']['name'] for poke_type in data['types']],
            "image": data['sprites']['front_default']
        }
    return None


def save_pokemon_data(pokemon_data):
    """Saves Pokémon data to a JSON file in the 'pokedex' directory."""
    if not os.path.exists('pokedex'):
        os.makedirs('pokedex')

    file_path = os.path.join('pokedex', f"{pokemon_data['name']}.json")
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(pokemon_data, file, indent=4, ensure_ascii=False)


def display_pokemon_data(pokemon_data):
    """Displays Pokémon data in a tkinter window."""
    window = Toplevel()
    window.title(f"Pokémon - {pokemon_data['name'].capitalize()}")
    window.configure(bg='black')

    # Pokémon Image
    image_url = pokemon_data['image']
    response = requests.get(image_url)
    image_data = response.content
    image = Image.open(BytesIO(image_data))
    photo = ImageTk.PhotoImage(image)
    image_label = Label(window, image=photo, bg='black')
    image_label.image = photo  # Keep a reference to avoid garbage collection
    image_label.pack()

    # Pokémon Details
    details_label = Label(
        window, text="Details:", font=("Arial", 14, "bold"),
        bg='black', fg='yellow'
    )
    details_label.pack()

    details_text = Text(
        window, wrap="word", height=6, width=50,
        font=("Arial", 12), bg='black', fg='red'
    )
    details_text.pack(padx=10, pady=5, fill=BOTH, expand=True)

    details_text.insert("1.0", f"Name: {pokemon_data['name']}\n")
    details_text.insert("2.0", f"Weight: {pokemon_data['weight']}\n")
    details_text.insert("3.0", f"Height: {pokemon_data['height']}\n")
    details_text.insert("4.0", f"Abilities: {', '.join(pokemon_data['abilities'])}\n")
    details_text.insert("5.0", f"Types: {', '.join(pokemon_data['types'])}\n")
    details_text.config(state="disabled")

    # Pokémon Moves
    moves_label = Label(
        window, text="Moves:", font=("Arial", 14, "bold"),
        bg='black', fg='yellow'
    )
    moves_label.pack()

    moves_text = Text(
        window, wrap="word", height=10, width=50,
        font=("Arial", 10), bg='black', fg='red'
    )
    moves_text.pack(padx=10, pady=5, fill=BOTH, expand=True)

    scrollbar = Scrollbar(window, command=moves_text.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    moves_text.config(yscrollcommand=scrollbar.set)
    moves_text.insert("1.0", "\n".join(pokemon_data['moves']))
    moves_text.config(state="disabled")

    window.mainloop()


def search_pokemon():
    """Fetches and displays Pokémon data based on user input."""
    pokemon_name = entry.get().strip()
    if not pokemon_name:
        messagebox.showerror("Error", "Please enter a Pokémon name.")
        return

    pokemon_data = get_pokemon_data(pokemon_name)

    if pokemon_data:
        save_pokemon_data(pokemon_data)
        display_pokemon_data(pokemon_data)
    else:
        messagebox.showerror("Error", f"The Pokémon '{pokemon_name}' does not exist.")


def main():
    """Main function to run the Pokédex application."""
    global entry

    # Tkinter setup
    root = Tk()
    root.title("Pokédex")
    root.configure(bg='black')

    # Input field
    entry_label = Label(
        root, text="Enter Pokémon name:", font=("Arial", 14),
        bg='black', fg='yellow'
    )
    entry_label.pack(padx=10, pady=5)

    entry = Entry(root, font=("Arial", 14), bg='black', fg='yellow')
    entry.pack(padx=10, pady=5)

    # Search button
    search_button = Button(
        root, text="Search", command=search_pokemon,
        font=("Arial", 14, "bold"), bg='yellow', fg='black'
    )
    search_button.pack(padx=10, pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
