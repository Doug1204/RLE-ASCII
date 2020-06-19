class Art:
    def __init__(self):
        self.RLE = None    

    def inputRLE(self): # allows user to input a certain number of lines of RLE 

        lines = getNum(min=2, question='How many lines of RLE would you like to enter (3+)?\n') # gets number of lines to input
        RLE = []

        for line in range(lines):

            badInput = True
            while badInput:

                RLE_line = input('Line: ') # input

                digits = ''.join([char for index, char in enumerate(RLE_line, start=1) if index % 3 != 0]) # checks if it is a valid RLE line
                if digits.isdigit():
                    RLE.append(RLE_line)
                    badInput = False

                else:
                    print('****Invalid Line****')

        self.RLE = RLE
    
    @staticmethod
    def getFileContent(): # gets the content of a file

        badInput = True
        while badInput:

            RLE_file = input('Enter the name of the file: ') # gets file name

            try:
                with open(RLE_file, 'r') as f: # opens file
                    return f.read() # returns content

            except FileNotFoundError: # if there is no file of that name
                print('That is not a valid file name')

    def fromFile(self): # converts file content to list of RLE
        self.RLE = self.getFileContent().split('\n')
    
    def printAsciiFile(self): # prints file content
        content = self.getFileContent()
        print(content)
    
    def convertAscii(self): # converts normal ascii to RLE
        content = self.getFileContent()
        converted = []

        for line in content.split('\n'): # runs through each line

            RLE = '' # base variables
            count = 1 # counts number of occurances
            char = line[0] # first character

            for index, new in enumerate(line[1:-1], start=1): # runs through each character checking if the character has changed

                if new != line[index + 1]: # if different character
                    RLE += str(count).zfill(2) + char # 
                    count = 1 # resets base variables
                    char = line[index + 1]

                else:
                    count += 1 # adds another occurance

            RLE += str(count).zfill(2) + char # adds final RLE as no character has changed
            converted.append(RLE) # adds to main store
        
        with open('convertedASCII.txt', 'w') as f: # saves converted to new file
            converted = '\n'.join(converted)
            f.write(converted)
        
        print(f'The file is {len(content) - len(converted)} characters smaller!') # tells user how many characters have been saved


    def displayExpanded(self): # displays the stored RLE as original

        for line in self.RLE: # for line in RLE

            for section in range(0, len(line), 3): # every section of 3 in line
                section = line[section:section+3] # every section eg 12j 08?
                print(int(section[:2]) * section[-1], end='') # print number * ASCII and end='' so it doesn't go onto a new line

            print() # new line

def getNum(min=0, max=float('inf'), question='Please enter a number'): # retrieves a valid number from user

    badInput = True
    while badInput:

        userInput = input(question)

        if userInput.isdigit(): # checks if number
            userInput = int(userInput)

            if min < userInput <= max: # if number in range
                return userInput

            else: # error messages
                print(f'Please enter a number between {min} and {max}')
        else:
            print('That is not a number')



def menu():

    options = ['Enter RLE', 'Display ASCII art', 'Convert To ASCII ART', 'Convert to RLE', 'QUIT'] # options

    print('****WELCOME****')

    lineFormat = lambda num, x: f' {num}. {option}' # option format

    for number, option in enumerate(options, start=1): # displays option with number next to them
        print(lineFormat(number, option))
    
    return getNum(max=5, question='Please enter an option: ') # returns a valid number

def execute(art, option): # converts option to process

    if option == 1: # input RLE by user
        art.inputRLE()
        art.displayExpanded()

    elif option == 2: # displays an ascii file in terminal
        art.printAsciiFile()

    elif option == 3: # expands an RLE txt file into ascii and displays on terminal
        art.fromFile()
        art.displayExpanded()

    elif option == 4: # converts an ASCII file to RLE and saves it as a new file
        art.convertAscii()

    else:
        print('****GOODBYE****')
        quit()


def main():
    while True:
        art = Art()
        option = menu()
        execute(art, option)
        
if __name__ == '__main__':
    main()
