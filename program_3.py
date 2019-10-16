import csv
def amt_per_console(file_name): #function to count amount of games per genre
    file = open(file_name,'r') #opens .csv file
    file.readline()
    set_console = {} #sets open dict for console
    for line in file:
        line = line.split(',') #splits each line based on commas
        console = line[-24]
        if console not in set_console:
            set_console[console] = 1
        elif console in set_console:
            set_console[console] += 1
    file.close()
    print("|+--------------------------------------------------------------------+|")
    print('Console Name | Amount of Games       ')
    for key in set_console.keys():
        print('-'+key+": "+str(set_console[key]))
    print("|+--------------------------------------------------------------------+|")
def amt_genre(file_name):
    myDictionary = {}
    file = open(file_name, "r")
    file.readline() # skips first line
    blacklist = "EA THQ 1 2 3 4 5 6 7 8 9 Nintendo Ubisoft Sony Activision Namco Konami Sega Capcom Rockstart IHQ Microsoft 2K Atari SquareEnix Midway Eidos Disney True"
    totalGames = 0
    for line in file:
        line = line.replace('"','')
        line = line.split(",") # format so we can work with it
        totalGames += 1
        for i in range(6):
            if line[-i-28] not in myDictionary and line[-i-28] not in blacklist:
                myDictionary[line[-i-28]] = 1
            elif line[-i-28] not in blacklist:
                myDictionary[line[-i-28]] += 1
    file.close() # close the file
    print("|+--------------------------------------------------------------------+|")
    print("| Total games released between 2004 and 2008: "+str(totalGames)+"                     |")
    print("| Amount of times a genre is listed:                                   |")
    for key in myDictionary.keys():
        print(" -"+key+": "+str(myDictionary[key]))
    print("|+--------------------------------------------------------------------+|")

def average_len_story(file_name):
    file = open(file_name, "r")
    file.readline()
    average = 0.0
    leisure = 0.0
    median = 0.0
    rushed = 0.0
    polled = 0.0
    counter = 0
    for line in file:
        line = line.split(",")
        rushed += float(line[-1][1:-2])
        polled += float(line[-2][1:-1])
        median += float(line[-3][1:-1])
        leisure += float(line[-4][1:-1])
        average += float(line[-5][1:-1])
        counter += 1
    file.close()
    myList = [rushed/counter, polled/counter, median/counter, leisure/counter, average/counter]
    print('+---------------------------------------------+')
    print(myList)

def main():
    amt_per_console('video_games.csv')
    amt_genre('video_games.csv')
    average_len_story('video_games.csv')
main()
