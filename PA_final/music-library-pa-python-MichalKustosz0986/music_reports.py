artistPosition = 0
albumNamePosition = 1
genrePosition = 3
timePosition = 4
RealesedYearPosition = 2


def get_albums_by_multiply_genre(albums, list_of_user_genres):
    
    resultList = []

    for elem in albums:
        for genre in list_of_user_genres:

            if elem[genrePosition] == genre:
                resultList.append(elem)

    return resultList

#=====================================================================================================================
def get_albums_by_genre_between_two_given_years(albums, genre, year_first, year_second):
    
    resultList = []

    for elem in albums:
        if elem[genrePosition] == genre:
            if int(elem[RealesedYearPosition]) <= year_second and int(elem[RealesedYearPosition]) >= year_first: 
                resultList.append(elem)

    if len(resultList) == 0:
        raise ValueError('no such genre between those years')
    return resultList
    
#=====================================================================================================================
def get_albums_by_genre(albums, genre):
    """
    Get albums by genre
    :param list albums: albums' data
    :param str genre: genre to filter by

    :returns: all albums of given genre
    :rtype: list
    """
    resultList = []
    for elem in albums:
        if elem[genrePosition] == genre:
            resultList.append(elem)
    if len(resultList) == 0:
        raise ValueError('Wrong genre')
    return resultList
    
#======================================================================================

def get_genre_stats(albums):
    """
    Get albums' statistics showing how many albums are in each genre
    Example: { 'pop': 2, 'hard rock': 3, 'folk': 20, 'rock': 42 }

    :param list albums: albums' data
    :returns: genre stats
    :rtype: dict
    """
    albumsDictionaryStat = {}
    listOfGenres = []

    for element in albums:
        listOfGenres.append(element[genrePosition])
    
    #now try do convert list to dictionary
    for element in listOfGenres:
        if element in albumsDictionaryStat.keys():
            albumsDictionaryStat[element] +=  1
        else:
            albumsDictionaryStat[element] = 1
    return albumsDictionaryStat

#======================================================================================
def get_longest_album(albums):
    """
    Get album with biggest value in length field.
    If there are more than one such album return the first (by original lists' order)

    :param list albums: albums' data
    :returns: longest album
    :rtype: list
    """
    #creating of list of times ( strings mm:ss )
    listOfLengthTimeSeconds = []

    for element in albums:
        listOfLengthTimeSeconds.append(to_time(element[timePosition]))
        

    maxValue = 0

    for i in range( len(listOfLengthTimeSeconds) ):
        if listOfLengthTimeSeconds[i] > maxValue:
            maxValue = listOfLengthTimeSeconds[i]
            maxValueIndex = i

    return albums[maxValueIndex]
    
#=================================================================================================

def get_last_oldest(albums):
    """
    Get last album with earliest release year.
    If there is more than one album with earliest release year return the last
    one of them (by original list's order)

    :param list albums: albums' data
    :returns: last oldest album
    :rtype: list
    """
    listOfReleasedYears = []
    for element in albums:
        listOfReleasedYears.append( int(element[RealesedYearPosition]) )

    minValue = listOfReleasedYears[0]

    for i in range( len(listOfReleasedYears) ):
        if listOfReleasedYears[i] <= minValue:
            minValue = listOfReleasedYears[i]
            minValueIndex = i

    return albums[minValueIndex]

#=================================================================================================

def get_last_oldest_of_genre(albums, genre):
    """
    Get last album with earliest release year in given genre

    :param list albums: albums' data
    :param str genre: genre to filter albums by
    :returns: last oldest import_data(filename='albums_data.txt'):album in genre
    :rtype: list
    """
    listOfTuplesYearGenreIndex = []
    index = 0
    newListOfGivenGenre = []

    for element in albums:
        if element[genrePosition] == genre:
            newListOfGivenGenre.append(element)

    newListOfGivenGenreSorted = sorted( newListOfGivenGenre, key=lambda t: t[RealesedYearPosition])

    return newListOfGivenGenreSorted[0]
    
#=================================================================================================
def to_time(str):
    """
    converts time in format "minutes:seconds" (string) to seconds (int)
    """
    SEC_IN_MIN = 60
    min_sec = str.split(':')
    return int( min_sec[0] )*SEC_IN_MIN + int(min_sec[1] )

#=================================================================================================
def get_total_albums_length(albums):
    """
    Get sum of lengths of all albums in minutes, rounded to 2 decimal places
    Example: 3:51 + 5:20 = 9.18             
             231 + 320 seconds = 551 seconds

    Get last album with earliest release year in given genre

    :param list albums: albums' data
    :param str genre: genre to filter albums by
    :returns: last oldest import_data(filename='albums_data.txt'):album in genre
    :rtype: list
    :param list albums: albums' data
    :returns: total albums' length in minutes
    :rtype: float
    """
    DURATION = 4
    durations = map( lambda album: to_time(album[DURATION]) , albums)
    total = sum(durations)
    return int(total / 60) + ((total % 60)/ 60)


albumTemp = [
            ["Pink Floyd", "The Dark Side Of The Moon", "1973", "progressive rock", "43:00"],
            ["Britney Spears", "Baby One More Time", "1999", "pop", "42:20"],
            ["The Beatles", "Revolver", "1966", "rock", "34:43"],
            ["Deep Purple", "Machine Head", "1972", "hard rock", "37:25"],
            ["Old Timers", "Old Time", "966", "ancient", "123:45"],
            ["Pink Floyd", "Wish You Were Here", "1975", "progressive rock", "44:28"],
            ["Boston", "Boston", "1976", "hard rock", "37:41"],
            ["Monika Brodka", "Granada", "2010", "pop", "37:42"],
            ["David Bowie", "Low", "1977", "rock", "38:26"],
            ["rock", "rock", "966", "pop", "13:37"],
            ["Massive Attack", "Blue Lines", "1991", "hip hop", "45:02"]
        ]

# result_list_of_multiply_genres = get_albums_by_multiply_genre(albumTemp, ["rock", "pop"])
# print(result_list_of_multiply_genres)

# resultList_between_years = get_albums_by_genre_between_two_given_years(albumTemp, "rock", 1967, 1977)
# print(resultList_between_years)

#get_longest_album(albumTemp)
#get_last_oldest_of_genre(albumTemp, "rock")


get_longest_album(albumTemp)