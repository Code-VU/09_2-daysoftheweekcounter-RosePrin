def countDayOfTheWeek():
    # This first line is provided for you
    file_name = input("Enter a file name: ")
    try: 
        file = open(file_name)
    except:
        print('invalid file name')
        exit()

    dayoftheweek_count = {}

    for line in file:
        if line.startswith('From '):
            line_words = line.split()
            week_day = line_words[2]
            
            if week_day not in dayoftheweek_count:
                dayoftheweek_count[week_day] = 1
            else:
                dayoftheweek_count[week_day] += 1

    print(dayoftheweek_count)


## if you want to test locally run > python payCalculator.py
if __name__ == "__main__":
    countDayOfTheWeek()
