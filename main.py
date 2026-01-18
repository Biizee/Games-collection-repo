import django_setup

from collection.models import Genre, Game

#!--Creating some genres of games
#first_genre = Genre.objects.create(
#    name = "JRPG"
#)
#
#second_genre = Genre.objects.create(
#    name = "Roguelike"
#)
#
#third_genre = Genre.objects.create(
#    name = "Shooter"
#)

#!--Getting genres by their id
first_genre = Genre.objects.get(id = 1)
second_genre = Genre.objects.get(id = 2)
third_genre = Genre.objects.get(id = 3)

#!--Creating some games
#first_game = Game.objects.create(
#    name = "Heaven for Death",
#    release_date = "2023-01-27",
#    rating = 9
#)
#
#second_game = Game.objects.create(
#    name = "Omori",
#    release_date = "2020-12-25",
#    rating = 10
#)
#
#third_game = Game.objects.create(
#    name = "Risk of Rain 2",
#    release_date = "2020-03-28",
#    rating = 8
#)
#
#fourth_game = Game.objects.create(
#    name = "Ultrakill",
#    release_date = "2020-09-03",
#    rating = 9
#)

#!--Getting games by their id
first_game = Game.objects.get(id = 1)
second_game = Game.objects.get(id = 2)
third_game = Game.objects.get(id = 3)
fourth_game = Game.objects.get(id = 4)

#!--Relating genres and games
#first_game.genre.add(first_genre)
#second_game.genre.add(first_genre)
#third_game.genre.add(second_genre)
#fourth_game.genre.add(third_genre)

#!--Printing info about games and their genres
games = Game.objects.all()
for g in games:
    print(g.name + " гра у жанрі " + str(g.genre.all()))
