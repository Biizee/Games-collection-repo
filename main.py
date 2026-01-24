import django_setup

from collection.models import Genre, Game
from django.core.exceptions import ObjectDoesNotExist

def list_all_games():
    games = Game.objects.all()
    if games:
        for game in games:
            print(f"\nGame id - {game.id}. \nGame name - {game.name}. \nGame release date - {game.release_date}. \nGame rating - {game.rating}. \nGame genre - {game.genre.all()}")

def list_all_genres():
    genres = Genre.objects.all()
    if genres:
        for genre in genres:
            print(f"\nGenre id - {genre.id}. \nGenre name - {genre.name}.")

def add_genre():
    name = input("Enter genre name: ")
    genre = Genre.objects.create(name = name)
    print(f"Added {genre.name} genre!")

def add_game():
    name = input("Enter game name: ")
    try:
        release_date = input("Enter realese date of game (example: 2020-01-30): ")
        rating = int(input("Enter game rating (min 1, max 10): "))
        genre = int(input("Enter genre id: "))
        game = Game.objects.create(
            name = name,
            release_date = release_date,
            rating = rating
        )
        game.genre.add(genre)
        print(f"\nGame was succesfully added!")
    except ObjectDoesNotExist:
        print(f"\nGenre doesn't exitsts or u made mistake. Try again!")
    except Exception as e:
        print(f"\nError: {e}")

def edit_game():
    try:
        game_id = int(input("Enter game id: "))
        game_id = Game.objects.get(id = game_id)
        new_name = input("Enter new name for game (leave blank to keep current): ")
        if new_name:
            game_id.name = new_name
        new_rating = input("Enter new rating for game (leave blank to keep current): ")
        if new_rating:
            game_id.rating = new_rating
        new_date = input("Enter new release date for game (leave blank to keep current): ")
        if new_date:
            game_id.release_date = new_date
        game_id.save()
        print(f"\nGame was succesfully edited!")
    except ObjectDoesNotExist:
        print(f"\nGame doesn't exitsts. Try again!")
    except Exception as e:
        print(f"\nError: {e}")

def edit_genre():
    try:
        genre_id = int(input("Enter genre id: "))
        genre_id = Genre.objects.get(id = genre_id)
        new_name = input("Enter new name for genre (leave blank to keep current): ")
        if new_name:
            genre_id.name = new_name
        genre_id.save()
        print(f"\nGenre was succesfully edited!")
    except ObjectDoesNotExist:
        print(f"\nGenre doesn't exitsts. Try again!")
    except Exception as e:
        print(f"\nError: {e}")

def delete_game():
    try:
        game = int(input("Enter game id: "))
        game = Game.objects.get(id = game)
        game.delete()
        print("\nGame deleted succesfully!")
    except ObjectDoesNotExist:
        print(f"\nGame doesn't exists. Try again!")
    except Exception as e:
        print(f"\nError: {e}")

def delete_genre():
    try:
        genre = int(input("Enter genre id: "))
        genre = Genre.objects.get(id = genre)
        genre.delete()
        print("\nGenre deleted succesfully!")
    except ObjectDoesNotExist:
        print(f"\nGenre doesn't exists. Try again!")
    except Exception as e:
        print(f"\nError: {e}")

while True:
    print("""
Options:
1. List all games
2. List all genres
3. Add genre
4. Add game
5. Edit game
6. Edit genre
7. Delete game
8. Delete genre
9. Exit""")
    
    try:
        choice = int(input("\nEnter your choice: "))
    except Exception as e:
        print(f"Error: {e}")
    
    if choice == 9:
        break

    elif choice == 1:
        list_all_games()
    
    elif choice == 2:
        list_all_genres()

    elif choice == 3:
        add_genre()
    
    elif choice == 4:
        add_game()
    
    elif choice == 5:
        edit_game()
    
    elif choice == 6:
        edit_genre()
    
    elif choice == 7:
        delete_game()
    
    elif choice == 8:
        delete_genre()

    else:
        print("Invalid choice, try again!")
