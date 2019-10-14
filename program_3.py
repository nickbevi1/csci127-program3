
def amt_per_console(file_name):
    file = open(file_name, "r")

    file.close()

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
    return myList

print(average_len_story("video_games.csv"))

