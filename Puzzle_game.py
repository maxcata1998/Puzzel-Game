'''
    CS 5001
    Fall 2021
    Final project
    Xiao Ma
    Design a puzzle game and realize the funcitons according to users' operations.

'''
import turtle
import time
import math
import random
turtle.title("CS5001 Sliding Puzzle Game")
screen = turtle.Screen()

def rectangle(turtle,length,width,color):
    '''
    draw a rectangle according to the given conditions
    '''
    turtle.pendown()
    turtle.color(color)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)

def start():
    '''
    Show the splash screen and get the information
    '''
    turtle.register_shape("Resources/splash_screen.gif")
    turtle.shape("Resources/splash_screen.gif")
    time.sleep(1)
    turtle.hideturtle()
    player = turtle.textinput("CS5001 Puzzle Slide", "Your Name:")
    step = turtle.numinput("5001 Puzzle Slide - Moves", \
                           "Enter the number of moves(chances) you want (5-200)", \
                            None, 5, 200)
    turtle.shape('blank')
    return player, step

def frame():
    '''
    draw the UI interface
    '''
    t1 = turtle.Turtle()
    t1.speed(10)
    t1.width(7)
    t1.penup()
    t1.goto(-300,300)
    rectangle(t1,480,470,'black')
    t1.penup()
    t1.goto(200,300)
    rectangle(t1,140,470,'blue')
    t1.penup()
    t1.goto(-300,-210)
    rectangle(t1,640,100,'black')
    turtle.penup()
    turtle.goto(100,-260)
    turtle.register_shape("Resources/resetbutton.gif")
    turtle.shape("Resources/resetbutton.gif")
    turtle.stamp()
    turtle.penup()
    turtle.goto(190,-260)
    turtle.register_shape("Resources/loadbutton.gif")
    turtle.shape("Resources/loadbutton.gif")
    turtle.stamp()
    turtle.penup()
    turtle.goto(280,-260)
    turtle.register_shape("Resources/quitbutton.gif")
    turtle.shape("Resources/quitbutton.gif")
    turtle.stamp()
    turtle.shape("blank")

class puzzle:
    number =0 
    def __init__(self, name):
        self.name = name
        try:
            with open(self.name, mode="r") as file:
                lines = file.readlines()
                self.number = int(lines[1].split(":")[1])
                self.size = int(lines[2].split(":")[1])
                self.thumbnail = lines[3].split(":")[1].strip()
                images = {}
                for i in range(4, len(lines)):
                    key, value = lines[i].split(":")
                    images[int(key)] = value.strip()
                self.images = images# get the index and address of puzzle pictures
        except IOError:
            turtle.register_shape("Resources/file_error.gif")
            turtle.shape("Resources/file_error.gif")
            time.sleep(2)
            turtle.hideturtle()
            
    def get_positions(self):
        '''
        get pairs of position.
        '''
        mode = int(math.sqrt(self.number))
        x = -250 + self.size/2
        y = 250 - self.size/2# set(-250,250)as the upper-left corner
        positions = []
        for i in range(mode):
            positions.append([x,y]) 
            for j in range(mode-1):
                x += self.size
                positions.append([x,y])# get the same amount coordinates as the numbers of puzzle 
            x = -250 + self.size/2
            y -=  self.size
        return positions

    def wrong_puzzles(self):
        '''
        get a list containing the groups of coordinates and index of picture
        '''
        all_positions = self.get_positions()
        random_list = random.sample(range(1,self.number+1),self.number)# Generate a random list to paste puzzle pictures
        positions_wrong=[]
        for i in range(len(all_positions)):
            key_i =random_list[i]
            turtle.penup()
            turtle.goto(all_positions[i][0],all_positions[i][1])
            turtle.register_shape(self.images[key_i])
            turtle.shape(self.images[key_i])
            turtle.stamp()
            positions_wrong.append([all_positions[i][0],all_positions[i][1],key_i])#get the list of position and index
        turtle.penup()
        turtle.goto(300,270)
        turtle.register_shape(self.thumbnail)
        turtle.shape(self.thumbnail)
        turtle.stamp()
        turtle.shape("blank")
        for i in range(len(positions_wrong)):
            if positions_wrong[i][2]== self.number:
                blank_position = [positions_wrong[i][0],positions_wrong[i][1]]# get the position of blank puzzle
        return positions_wrong, blank_position 
    

class click:
    def __init__(self,size,number,wrong_positions,blank_position,images,count):
        self.number = number
        self.size = size
        self.wrong_positions = wrong_positions
        self.blank_position = blank_position
        self.images = images
        self.count = count

    def operation(self,x,y):
        '''
        Determine operation according the position of mouse click
        '''
        click_position =[]
        for i in range(self.number):
            if (x > self.wrong_positions[i][0]-self.size/2) and (x < self.wrong_positions[i][0]+self.size/2) \
               and (y < self.wrong_positions[i][1]+self.size/2) and (y > self.wrong_positions[i][1]-self.size/2):
                click_position = [self.wrong_positions[i][0], self.wrong_positions[i][1]]
                #get the corresponding center coordinate of clicked position
                click_puzzle = self.wrong_positions[i][2]
                index_1 = i# get the index of the clicked picture
            if self.wrong_positions[i][2] == self.number:
                index_b = i# get the index of the blank picture           
        around_blank = [] # get the nearby coordinates of blank picture
        around_blank.append([self.blank_position[0]+self.size,self.blank_position[1]])
        around_blank.append([self.blank_position[0]-self.size,self.blank_position[1]])
        around_blank.append([self.blank_position[0],self.blank_position[1]+self.size])
        around_blank.append([self.blank_position[0],self.blank_position[1]-self.size])                        
        if click_position in around_blank:
            turtle.pendown
            turtle.goto(click_position[0],click_position[1])
            turtle.register_shape(self.images[self.number])
            turtle.shape(self.images[self.number])
            turtle.stamp()
            turtle.penup()
            turtle.goto(self.blank_position[0],self.blank_position[1])
            turtle.register_shape(self.images[click_puzzle])
            turtle.shape(self.images[click_puzzle])
            turtle.stamp()# swap the picture
            self.wrong_positions[index_1][2]=self.number
            self.wrong_positions[index_b][2] = click_puzzle
            self.blank_position = self.wrong_positions[index_1]# modify the list of position and index
            self.count +=1# moving steps add one
            t = turtle.Turtle()
            t.shape('blank')
            t.penup()
            t.goto(-260,-260)
            t.write("Player Moves:",font=("Verdana", 30, "normal"))
            t.penup()
            t.goto(-40,-260)
            t.write(self.count,font=("Verdana", 30, "normal"))
            t.goto(100,-260)
            t.clear()
                        
        if math.sqrt((x-100)**2+(y+260)**2)<50:#trigger the reset function
            for i in range(self.number):
                turtle.goto(self.wrong_positions[i][0],self.wrong_positions[i][1])
                turtle.register_shape(self.images[i+1])
                turtle.shape(self.images[i+1])
                turtle.stamp()
                
        if (x > 230) and (x < 330) and (y < -240) and (y > -280):#trigger the quit function
            turtle.reset()
        
        if (x > 140) and (x < 240) and (y < -210) and (y > -310):#trigger the load function
            new_picture = turtle.textinput("Load Puzzle",\
                                           "Enter the name of the puzzle you wish to load. Choices are:\n \
luigi.puz \n smiley.puz \n family.puz \n fifteen.puz \n yoshi.puz \n mario.puz")
            return new_picture
                                  

def main():
    start()
    frame()
    game = puzzle("luigi.puz") 
    puzzle.get_positions(game)
    wrong_positions, blank_position = puzzle.wrong_puzzles(game)
    number = game.number
    size = game.size
    images = game.images    
    one_click = click(size,number, wrong_positions,blank_position,images,0)
    turtle.onscreenclick(one_click.operation)
    
if __name__=="__main__":
    main()
    
