# Exercise 1
def save_scores(names, scores, filename):
    file = open(filename, "w")
    for i in range(len(names)):
        file.write(names[i] + "," + str(scores[i]) + "\n")
    file.close()

# Exercise 2
def average_score(filename):
    average = 0
    file = open(filename, "r")
    lines = file.readlines()
    for line in lines:
        spl = line.split(",")
        average = average + int(spl[1])
    file.close()
    average = round(average / len(lines), 1)

# Exercise 3
def filter_passed(source, destination, pass_mark):
    count = 0
    file = open(source, "r")
    lines = file.readlines()
    file.close()
    file_1 = open(destination, "w")
    for line in lines:
        spl = line.strip().split(",")
        if int(spl[1]) >= pass_mark:
            file_1.write(spl[0] + "," + spl[1] + "\n")
            count += 1
    file_1.close()

# Exercise 4
def replace_word(filename, old_word, new_word):
    file = open(filename, "r")
    text = file.read()
    file.close()
    text = text.replace(old_word, new_word)
    file = open(filename, "w")
    file.write(text)
    file.close()

# Exercise 5
def remove_line(filename, line_number):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    file = open(filename, "w")
    for i in range(len(lines)):
        if i != line_number - 1:
            file.write(lines[i])
    file.close()
