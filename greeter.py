#Dushyant Tara(20-06-2020):This program helps you understand functions along with while loops
"""#name = input("Please enter your name: ")
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name?"
name = input(prompt)
print("Hello, " + name.title() + "!")

#Using int() to accept numerical input
age = input("How old are you?")

age= int(age)

print(age >= 18)

"""

def greet_user():
    """Display a simple meeting"""
    print("Hello!")

greet_user()

#passing information to a function
def greet_user(username):
    """Display a simple greeting"""
    print("Hello, " + username.title() + "!")

greet_user('jesse')

#Arguments and parameters
#Exercise
def display_message():
    """Tells everyone what we learnt in this chapter"""
    print("We learnt about functions")

display_message()

def favorite_book(title):
    """Display's the book withthe title"""
    print("My favorite book is " + title)

favorite_book('Alice in Wonderland')


def get_formatted_name(first_name,last_name):
    """Return a full name, neatly formatted.

    Args:
        first_name (str): first name of the person
        last_name (str): second name of the person
    """    
    full_name = first_name + ' ' + last_name
    return full_name.title()

active = False#change this to True to run the line below
while active:
    print("\nPlease tell me your name:")
    print("(Enter 'q' at any time to quit)")
    f_name = input("First Name: ")
    if f_name == 'q':
        break

    l_name = input("Last Name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

#Exercises
#city names
def city_country(city,country):
    """Returns a city_country formatted string.

    Args:
        city (str): city name
        country (str): country name

    Returns:
        str: city_country in a formatted string(city,country)
    """    
    message = city + "," + country
    return message.title()

message1 = city_country('Bangalore','India')
message2 = city_country('New York','United States')
print(message1)
print(message2)

#Album
def make_album(album,artist):
    """Returns album info in a dictionary structure

    Args:
        album (str): album name
        artist (str): artist name

    Returns:
        Dict: Dictionary containing album information
    """    
    album_info = {}
    album_info['album'] = album.title()
    album_info['artist'] = artist.title()
    return album_info

abbey_road = make_album('abbey road','the beatles')
print(abbey_road)

wall_pf = make_album('the wall','pink floyd')
print(wall_pf)
    

def make_album(album,artist,tracks = ''):
    """Returns album info in a dictionary

    Args:
        album (str): Album name
        artist (str): Artist name
        tracks (int, optional): No. of songs in the album. Defaults to ''.

    Returns:
        Dict: Dictionary containing album information
    """    
    album_info = {}
    album_info['album'] = album.title()
    album_info['artist'] = artist.title()
    if tracks:
        album_info['tracks'] = tracks
    return album_info

wall_pf = make_album(album = 'the wall',artist = 'pink floyd')
print(wall_pf)

while True:
    print("\nPlease input your favorite album, artist and tracks in that album")
    print("\n Enter 'q' anytime to quit")
    album = input("Album name: ")
    if album == 'q':
        break
    artist = input("Artist: ")
    if artist == 'q':
        break
    tracks = input("tracks: ")
    if tracks == 'q':
        break
    album_info = make_album(album = album,artist = artist,tracks = tracks)

    print(album_info)