import sys
import csv
import random
import os
import time


def new_album():
    os.system('clear')
    add_artist = input('Enter an artist: ')
    add_album = input('Enter an album: ')
    add_year = input('Enter a year of release: ')
    add_genre = input('Enter a genre of music: ')
    add_length = input('Enter length of album: ')
    new_registry = ' | '.join([add_artist, add_album, add_year, add_genre, add_length])
    new_reg = open("music.csv", 'a')
    new_reg.write(new_registry)
    new_reg.write("\n")
    new_reg.close

    menu_return()


def albums_by_artist():
    os.system('clear')
    sel_artist = input('Enter selected artist: ')

    with open('music.csv', 'r') as csvfile:
        readCSV = csv.reader(csvfile, delimiter='|')
        for row in readCSV:
            artist = row[0]
            album = row[1]
            if sel_artist in artist:
                artists = []
                albums = []
                artists.append(artist)
                albums.append(album)
                print(albums)

    menu_return()


def albums_by_year():

    os.system('clear')
    sel_year = input('Enter a year of release: ')
    with open('music.csv', 'r') as csvfile:
        readCSV = csv.reader(csvfile, delimiter='|')
        for row in readCSV:
            album = row[1]
            year = row[2]
            if sel_year in year:
                albums = []
                years = []
                albums.append(album)
                years.append(year)
                print(albums)

    menu_return()


def musician_by_album():

    os.system('clear')
    sel_album = input('Enter a name of an album: ')
    with open('music.csv', 'r') as csvfile:
        readCSV = csv.reader(csvfile, delimiter='|')
        for row in readCSV:
            artist = row[0]
            album = row[1]
            if sel_album in album:
                artists = []
                albums = []
                artists.append(artist)
                albums.append(album)
                print(artists)

    menu_return()


def albums_by_letters():

    os.system('clear')
    sel_letter = input('Enter a letter (or a letters): ')
    with open('music.csv', 'r') as csvfile:
        readCSV = csv.reader(csvfile, delimiter='|')
        for row in readCSV:
            album = row[1]
            albums = []
            albums.append(album)
            for item in albums:
                if sel_letter in album:
                    print(albums)

    menu_return()


def albums_by_genre():

    os.system('clear')
    sel_genre = input('Enter a genre: ')
    with open('music.csv', 'r') as csvfile:
        readCSV = csv.reader(csvfile, delimiter='|')
        for row in readCSV:
            album = row[1]
            genre = row[3]
            if sel_genre in genre:
                albums = []
                genres = []
                genres.append(genre)
                albums.append(album)
                print(albums)

    menu_return()


def calculate_age():

    os.system('clear')
    with open('music.csv', 'r') as csvfile:
        readCSV = csv.reader(csvfile, delimiter='|')
        years = []
        sum_years = 0
        for row in readCSV:
            years.append(row[2])
        for each_year in years:
                sum_years = sum_years + int(each_year)
                age_of_all_albums = 2017*len(years) - sum_years
        print('The age of all albums is', age_of_all_albums, 'years.')

    menu_return()


def choose_random_album():

    os.system('clear')
    sel_genre = input('Enter a genre: ')
    with open('music.csv', 'r') as csvfile:
        readCSV = csv.reader(csvfile, delimiter='|')
        for row in readCSV:
            try:
                album = row[1]
                genre = row[3]
                albums = []
                genres = []
                if sel_genre in genre:
                    genres.append(genre)
                    albums.append(album)
                    random_index = random.randint(0, len(albums))
                    print(albums[random_index])
            except IndexError:
                pass
            continue

    menu_return()


def menu_return():

    decision = input("Press 'q' to quit program or to come back to the main menu - press any other key:  ").lower()
    if decision == "q":
        print('See You later!')
        sys.exit()
    else:
        main()


def main():

    with open('music.csv', 'r') as csvfile:
        readCSV = csv.reader(csvfile, delimiter='|')

    os.system('clear')

    print('Welcome in the CoolMusic catalog system! Please choose what you want to do:')
    print('1 - Add new album')
    print('2 - Find albums by artist')
    print('3 - Find albums by year')
    print('4 - Find musician by album')
    print('5 - Find albums by letter(s)')
    print('6 - Find albums by genre')
    print('7 - Calculate the age of all albums')
    print('8 - Choose a random album by genre')
    print('0 - Exit')

    chosen_number = input("Enter selected number from the list above: ")

    if chosen_number == '1':
        new_album()
    elif chosen_number == '2':
        albums_by_artist()
    elif chosen_number == '3':
        albums_by_year()
    elif chosen_number == '4':
        musician_by_album()
    elif chosen_number == '5':
        albums_by_letters()
    elif chosen_number == '6':
        albums_by_genre()
    elif chosen_number == '7':
        calculate_age()
    elif chosen_number == '8':
        choose_random_album()
    elif chosen_number == '0':
        print('See you next time!')
        sys.exit()
    else:
        print('Incorrect number!')
        main()
        answer = input('Select a number of choosen action: ')

main()
