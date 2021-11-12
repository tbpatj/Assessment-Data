#open the file "um-server-01.txt" and assign the result to a variable named log_file
log_file = open("um-server-01.txt")

#create a function with one parameter called log_file
def sales_reports(log_file):
    #iterate through each line of the .txt file supplied through the params, assign each line to a variable named line
    for line in log_file:
        #removes all the whitespaces and other garbage at the end of the string (line)
        line = line.rstrip()
        #get back the first 3 indecies of the string line assign it to the variable named day
        day = line[0:3]
        #check if the day is Tuesday, or Monday, by checking it with its shortened self, which is how the file is formated
        if day == "Mon":
            #log out the line if the day is tuesday
            print(line)

def top_sellers(log_file):
    for line in log_file:
        line = line.rstrip()
        #get the 3rd item which is the amount of melons delivered
        amount = int(line.split(" ")[2])
        #check if they delivered more than 10 melons if so print the line
        if(amount > 10):
            print(line)
print("\n---------------BIG SELLERS---------------\n")
top_sellers(log_file)
#call the function sales_reports with the file that we opened at the begining of the file
log_file.close()
log_file = open("um-server-01.txt")
print('\n---------------MELON MONDAY---------------\n')
sales_reports(log_file)
log_file.close()

