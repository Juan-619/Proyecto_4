This python script creates a simple pokédex application using the 'tkinter'library
for the graphical user interface (GUI). The application fetches data from the pokeAPI,
displays the details of a specified Pokémon, and saves this information to a JSON file.

1- Importing libraries:
° 'os':For handling file and directory operations.
° 'json':For saving and loading JSON files.
° 'requests':For making HTTP requests to fetch data from PokeAPI.
° 'tkinter':For creating the GUI components.
° 'pil'(Pillow):For handling image operations.
° 'io.BytesIO':For handlin image data in memory.

2- Fetching Pokémon data:
This funcion makes a request to the PokeAPI to fetch data for a given pokémon.
If the request is succesful (status code 200), it extracts relevant details (name,weight,
height,moves,abilities,types, and image URL) and returns them in a dictionary.
If the Pokémon is not fond, it returns 'None'.

3- Saving Pokémon data:
This fucion saves the fetched pokémon data to a JSON file inside a directory named 'pokédex'.
If the 'pokédex' directory doesn't exist, it creates it.
The data is saved in a JSON file named after the Pokémon.

4- Displaying Pokémon data:
This funcion creates a new 'tkinter' window (Toplevel) to display the Pokémon data.
The window background is set to black.
The Pokémon's image is fetched and displayed.
The details (name,weight,height,abilities,types) are displayed in a 'Text' widget
with a black background and red text.
The moves are displayed in another 'Text' widget with a scrollbar, also styled
with a black background and red text.

5- Searching for a Pokémon:
This funcion is triggered when the user clicks the search button.
It retrieves the pokémon name from the input field fetches the data, saves it, and displays it.
If the pokémon doesnt' exist, it shows an error message.

6- Main Function:
The 'main' function sets up the main 'tkinter' window.
It creates an imput field for the pokémon name and a search button.
The window is styled with a black background and yellow text.

7- Entry Point:
This check if the script is being run directly (not imported) and calls the 'main' function to start the application.

Summary:
The script fetches and displays Pokémon data using a graphical interface.
It uses the PokeAPI to get data and the 'tkinter' library fot the GUI.
The data is displayed in a styled window, and the information is saved to a JSON file.
The main function sets up the interface and starts the application.
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
we have lerned how to create a Pokédex application using Python, the PokeAPI,
and the tkinter library for the graphical user interfce (GUI). Specifically, we have
lerned to. 

Make HTTP request: We used the 'requests' library to make GET requests to the PokéAPI
and fetch Pokémon data.

Process JSON data: We prased the JSON response to extract relevant information such as the
Pokémon's name,weight,heght,moves,abilities, and types.

Save data to a file: We saved the Pokémon information in JSON files within a directory named
'pokedex'.

Create a graphical user interface (GUI): We used the tinker library to create a window that prompts the user 
for a Pokémon's name and then displays the fetched data.
We customized the apperance of the window with specific colors and fonts.

Display images in the GUI: We downloaded and displayed the Pokémon's image in the GUI window
using 'PIL'(Python imaging library) and 'ImageTK'.

Orgnize code according to PEP-8: We structured and formatted the code to comply with Python's
PEP-8 style guide, improvin readadbility and maitainbility.

Thtse skills combine the use of libraries for making web requests, handling JSON
data, creting grphicl user interfaces, and following good coding practices in Python.
