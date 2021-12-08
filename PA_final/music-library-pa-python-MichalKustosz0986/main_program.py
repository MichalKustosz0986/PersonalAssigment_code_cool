# from display import print_program_menu, print_albums_list, print_command_result, print_album_info
# from music_reports import get_albums_by_genre,get_genre_stats, get_last_oldest,\
# get_last_oldest_of_genre, get_longest_album, get_total_albums_length, to_time

import display
import music_reports
import file_handling


"""
The main program should use functions from music_reports and display modules
"""
def delete_album_by_artist_and_album_name_v2(albums, artist, album_name):

    isElementRemoved = False
    for i in range(len(albums)):
        if albums[i][music_reports.artistPosition] == artist and albums[i][music_reports.albumNamePosition] == album_name:
            del albums[i]
            isElementRemoved = True
            break

    if isElementRemoved == False:
        raise IOError('Wrong artist and/or album name')
    file_handling.export_data(albums)

#===============================================================================================================
def delete_album_by_artist_and_album_name(albums, artist, album_name):
    """
    Deletes album of given name by given artist from list and updates data file

    :param list albums: currently existing albums
    :param str artist: artist who recorded the album
    :param str album_name: name of album to be deleted

    :returns: updated albums' list
    :rtype: list
    """

    for element in albums:
        if element[music_reports.artistPosition] == artist and element[music_reports.albumNamePosition] == album_name:

            albums.remove(element)
            # indexOfElement = albums.index(element)
            # del albums[indexOfElement]
    file_handling.export_data(albums)
#=========================================================================================================================

def create_album(albums, artist, albumName, realiseYear, genre, timeLength):
    info = ""
    info += artist+", "+albumName +", "+ realiseYear+", "+ genre+ ", "+ timeLength
    print("\n\t",info)

#=========================================================================================================================
def make_user_choice(userOption):
    
    albums = file_handling.import_data('albums_data.txt')

    if userOption == 0:
        print("\n\tyour choose is: Deleting Album ")
        artist = input("\n\tEnter artist name: ")
        albumName = input("\n\tEnter album name:")

        try:
            delete_album_by_artist_and_album_name_v2(albums, artist, albumName)
        except IOError:
            print("wrong artist name or/and album name")
    
    elif userOption == 1:
        print("\n\tyour choose is: Get albums by genre ")
        genre = input("\n\tenter Genre: ")

        try:
            listOfSpecificGenres = music_reports.get_albums_by_genre(albums, genre)
            display.print_albums_list(listOfSpecificGenres)

        except Exception:
            print("\n\tno such genre ",genre)
        
    elif userOption == 2:
        print("\n\tyour choose is: Display oldest album")
        lastOldestAlbum = music_reports.get_last_oldest(albums)
        display.print_album_info(lastOldestAlbum)
    
    elif userOption == 3:
        print("\n\tyour choose is: Show genre stat ")
        dictStatReport = music_reports.get_genre_stats(albums)
        print(dictStatReport)

    elif userOption == 4:
        print("\n\tyour choose is: Show albums: ")
        display.print_albums_list(albums)

    elif userOption == 5:
        print("\n\tyour choose is: add album ")
        artist = input("\ntenter artist: ")
        albumName = input("\n\tenter Album Name: ")
        realiseYear = input("\n\tenter Realise Year: ")
        genre = input("\n\tenter Genre: ")
        timeLength = input("\n\tenter time Length in format(mm:ss): ")
        create_album(albums, artist, albumName, realiseYear, genre, timeLength)

    elif userOption == 6:

        display.print_command_result("your choose is: List Albums of specific genre between two giwen years ")
        genre = input("\n\tenter Genre: ")
        first_year = int( input("\ntenter first year: ") )
        second_year = int( input("\n\tenter second year: "))
        
        try:
            result_between_years = music_reports.get_albums_by_genre_between_two_given_years(albums, genre, first_year, second_year )
            display.print_albums_list(result_between_years)
            
        except Exception:
            print("\n\tno such genre ",genre, "between ", first_year, " and ", second_year)
            
        
    elif userOption == 7:

        display.print_command_result("your choose is: list albums by specifying multiple specific genres (not just a single one)")

        #pobierz od usera liste
        #list_of_user_genres =  ["rock", "pop", ]

        #list_of_user_genres = []

        #how_many_genres_user_want = int( input("enter number of genres\n") )
        # i = 1
        # while i <= how_many_genres_user_want:
        #     list_of_user_genres.append( input(" enter your genre\n") )
        #     i+=1

        
        user_genres = input("enter genres separating by commas, ")
        list_of_user_genres = user_genres.split(",")
        print(list_of_user_genres)


        

        result_multiple_genres = music_reports.get_albums_by_multiply_genre(albums, list_of_user_genres)
        display.print_albums_list(result_multiple_genres)



#=========================================================================================================================
def main():
    """
    Calls all interaction between user and program, handles program menu
    and user inputs. It should repeat displaying menu and asking for
    input until that moment.

    You should create new functions and call them from main whenever it can
    make the code cleaner
    """

    menu_comand = [ "Delete album", "Get albums by genre",  "Display oldest album",
                    "Show genre stats", "Show albums", "Create ALbum", 
                    "List Albums of specific genre between two giwen years" , 
                    "list albums by specifying multiple specific genres (not just a single one)" ]

    UserAnswer = "yes"
    while UserAnswer == "yes":

# result_list_of_multiply_genres = get_albums_by_multiply_genre(albumTemp, ["rock", "pop"])
# print(result_list_of_multiply_genres)
        display.print_program_menu(menu_comand)

        try:
            userOption = int(input("\n input your choise: "))
            if (userOption == 0 or userOption == 1 or userOption == 2 or userOption == 3 or userOption == 4 or userOption == 5 or userOption == 6 or userOption == 7):
                make_user_choice(userOption)
            else:
                print(userOption," No such Option try again")  
        
        except ValueError:
            print("enter valid number choice")
       
        UserAnswer = input("\tDo You want to continue yes/no \n")
    

    
if __name__ == '__main__':
    main()
