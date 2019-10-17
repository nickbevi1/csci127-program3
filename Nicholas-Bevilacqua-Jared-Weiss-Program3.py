#####################################
# Nicholas Bevilacqua & Jared Weiss #
# October 16, 2019                  #
# Program 3                         #
#####################################
def amt_per_console(file_name): #function to count amount of games per genre
    file = open(file_name,'r') #opens .csv file
    file.readline() #reads first line in .csv file
    set_console = {} #sets open dict for console
    for line in file:
        line = line.split(',') #splits each line based on commas
        console = line[-24]
        if console not in set_console: #checks to see if the console name is not already in the dict 
            set_console[console] = 1    #if not then adds it to the dict with a value of 1
        elif console in set_console: 
            set_console[console] += 1   # if already in dict add 1 to the value for the specifc key 
    file.close()
    print("|+--------------------------------------------------------------------+|")
    print('Console Name | Amount of Games       ')
    for key in set_console.keys():
        print(key+": "+str(set_console[key]))
    print("|+--------------------------------------------------------------------+|")
def amt_genre(file_name): #function to count the amount of games in each genre 
    myDictionary = {}
    file = open(file_name, "r")
    file.readline() # skips first line
    blacklist = "EA THQ 1 2 3 4 5 6 7 8 9 Nintendo Ubisoft Sony Activision Namco Konami Sega Capcom Rockstart IHQ Microsoft 2K Atari SquareEnix Midway Eidos Disney True TRUE"
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
    print("| Total games released between 2004 and 2008: "+str(totalGames)+"                     | ")
    print("| Amount of times a genre is listed:                                   |")
    for key in myDictionary.keys():
        print(key+": "+str(myDictionary[key]))
    print("|+--------------------------------------------------------------------+|")

def average_len_story(file_name): #function to find the average length of each play through type 
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
        rushed += float(line[-1])   
        polled += float(line[-2])
        median += float(line[-3])
        leisure += float(line[-4])
        average += float(line[-5])
        counter += 1
    myList = [rushed/counter, polled/counter, median/counter, leisure/counter, average/counter]
    print("|+--------------------------------------------------------------------+|")
    print('Average times based on style of playthrough of main story')
    print('Rushed: ' + str(round(myList[0], 2)))
    print('Polled: '+ str(round(myList[1], 2)))
    print('Median: ' + str(round(myList[2], 2)))
    print('Leisure: ' + str(round(myList[3], 2)))
    print('Average: '+ str(round(myList[4], 2)))
    print("|+--------------------------------------------------------------------+|")
    file.close()


def main(): #main function just to run programs, was not intended to be apart of the 3 requirment 
    amt_per_console('video_games.csv')
    amt_genre('video_games.csv')
    average_len_story('video_games.csv')
main()
