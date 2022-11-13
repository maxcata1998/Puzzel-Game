import turtle
import time
import math
import random
import copy
##def starter(): 
##    turtle.register_shape("Resources/splash_screen.gif")
##    turtle.shape("Resources/splash_screen.gif")
##    time.sleep(3)
##    turtle.hideturtle()
##    player = turtle.textinput("CS5001 Puzzle Slide", "Your Name:")
##    move = turtle.numinput("5001 Puzzle Slide - Moves", \
##                           "Enter the number of moves(chances) you want (5-200)", \
##                            None, 5, 200)
turtle.speed(10)
class get_file:
    def __init__(self, name):
        self.name = name
        try:
        #get everything that within the file
            with open(self.name, mode="r") as file:
                self.images = []
                self.thumbnail = {}
                line = file.readlines()
                self.number = int(line[1].split(":")[1])
                self.size = int(line[2].split(":")[1])
                #set the first image's position
                k, v = line[3].split(":")
                self.thumbnail[k] = v
                #get the image of thumbnail
                for i in range(4, len(line)):
                    image = {}
                    key, v = line[i].split(":")
                    value = v.split()
                    image[int(key)] = value[0]
                    #get image's path
                    self.images.append(image)
        except IOError:
            turtle.register_shape("Resources/file_error.gif")
            turtle.shape("Resources/file_error.gif")
            time.sleep(2)
            turtle.hideturtle()  
            
    def get_number(self):
        return self.number

    def get_size(self):
        return self.size

    def get_image(self):
        return self.images
            
class show_puzzle:
    def __init__(self, name):
        self.name = name
        try:
        #get everything that within the file
            with open(self.name, mode="r") as file:
                self.images = []
                self.thumbnail = {}
                line = file.readlines()
                self.number = int(line[1].split(":")[1])
                self.size = int(line[2].split(":")[1])
                #set the first image's position
                k, v = line[3].split(":")
                value = v.split()
                self.thumbnail[k] = value[0]
                #get the image of thumbnail
                for i in range(4, len(line)):
                    image = {}
                    key, v = line[i].split(":")
                    value = v.split()
                    image[int(key)] = value[0]
                    #get image's path
                    self.images.append(image)
        except IOError:
            turtle.register_shape("Resources/file_error.gif")
            turtle.shape("Resources/file_error.gif")
            time.sleep(2)
            turtle.hideturtle()
                
    def draw_frame(self):
        #draw the border of the picture
        turtle.pu()
        turtle.setheading(0)
        turtle.pen(pensize = 3, pencolor = "gray")
        turtle.forward(self.size/2)
        turtle.rt(90)
        turtle.pd()
        turtle.forward(self.size/2)
        turtle.rt(90)
        turtle.forward(self.size)
        turtle.rt(90)
        turtle.forward(self.size)
        turtle.rt(90)
        turtle.forward(self.size)
        turtle.rt(90)
        turtle.forward(self.size/2)
        
    def set_position(self):
        #set specific coordinates for each image
        n = int(math.sqrt(self.number))
        ori_x = -340 + self.size/2
        ori_y = 250 - self.size/2
        position = []      
        for i in range(n):
            for j in range(n):
                new_x = ori_x
                new_x += self.size * j
                position.append((new_x, ori_y))
            ori_y -= self.size
        return position
            
    def original_images(self):
        p = self.set_position()
        #get the position for images
        ori_coordinates = {}
        #get the image's position
        blank_coordinates = []
        #get the blank image's position
        for i in range(len(p)):
            turtle.goto(p[i])
            self.draw_frame()
            turtle.stamp()
            turtle.pu()
            turtle.goto(p[i])
            turtle.register_shape(self.images[i][i + 1])
            #from the image list select the exact image and set it as shape to turtle
            turtle.shape(self.images[i][i + 1])
            #show the image
            turtle.stamp()
            turtle.shape("blank")
            ori_coordinates[p[i]] = self.images[i][i + 1]
            #get the key and value for dictionary,key represents the image's coordinates,
            #value represents the image's path
            if i == self.number - 1:
##                blank_coordinates[self.number] = p[i]
                blank_coordinates.append(p[i])
                #get the key and value for blank image's dictionary, key represents
                #the number of the blank image, value represents it's coordinate
        turtle.pu()
        turtle.goto((320, 250))
        turtle.register_shape(self.thumbnail["thumbnail"])
        turtle.shape(self.thumbnail["thumbnail"])
        turtle.stamp()
        turtle.shape("blank")
        return ori_coordinates, blank_coordinates
            
    def mix_images(self):
        number = []
        for i in range(self.number):
            number.append(i)  
        #set the list number to select the image
        mix_coordinates = {}
        #get the image's position
        blank_coordinates = []
        #get the blank image's position
        p = self.set_position()
        for i in range(len(p)):
            turtle.goto(p[i])
            self.draw_frame()
            turtle.stamp()
            turtle.pu()
            turtle.goto(p[i])
            n = random.choice(number)
            #randomly select images to display
            turtle.register_shape(self.images[n][n + 1])
            turtle.shape(self.images[n][n + 1])
            number.remove(n)
            #remove the image number that has been displayed
            turtle.stamp()
            turtle.shape("blank")
            mix_coordinates[p[i]] = self.images[n][n + 1]
            mix_coordinates.append(dic_image)
            if n == self.number - 1:
                blank_coordinates.append(p[i])
##                blank_coordinates[self.number] = p[i]
                #get the key and value for blank image's dictionary, key represents
                #the number of the blank image, value represents it's coordinate
        turtle.pu()
        turtle.goto((320, 250))
        turtle.register_shape(self.thumbnail["thumbnail"])
        turtle.shape(self.thumbnail["thumbnail"])
        turtle.stamp()
        turtle.shape("blank")
        return mix_coordinates, blank_coordinates
        
    def get_coordinates(self):
        p = self.set_position()
        #get the position of the images
        x = []
        y = []
        for i in range(len(p)):
            x1 = p[i][0] - self.size/2
            x2 = p[i][0] + self.size/2
            x.append((x1, x2))
            y1 = p[i][1] - self.size/2
            y2 = p[i][1] + self.size/2
            y.append((y1, y2))
        return x, y

class click:
    def __init__(self, image, blank, size, blank_path, x_list, y_list):
        self.image = image
        self.blank = blank
        #get the blank image's coordinate
        self.size = size
        self.blank_path = blank_path
        self.x_list = x_list
        self.y_list = y_list
        self.copy_blank = copy.deepcopy(self.blank)
        #get the copy of the blank's coordinate
        self.copy_image = copy.deepcopy(self.image)
        #get the copy of the image's coordinate
        
    def get_mouse_click(self, x, y):
##        copy_image = copy.deepcopy(self.image)
##        
##        copy_blank = copy.deepcopy(self.blank)
        print(self.copy_blank)
        blank_x = self.copy_blank[0][0]
        #get the blank image's x coordinate
        blank_y = self.copy_blank[0][1]
        #get the blank image's y coordinate
        coordinate = []
        co_x = self.x_list
        co_y = self.y_list
        for i in range(len(co_x)):
        #x and y represents onscreen clicked's coordinates
            if co_x[i][0] < x and co_x[i][1] > x:
                coo_x = (co_x[i][0] + co_x[i][1])/2
                #get the x coordinate of the clicked image
                coordinate.append(coo_x)
                break
        for j in range(len(co_y)):
            if co_y[j][0] < y and co_y[j][1] > y:
                coo_y = (co_y[j][0] + co_y[j][1])/2
                #get the y coordinate of the clicked image
                coordinate.append(coo_y)
                break
        while len(coordinate) > 1:
            image_path = self.copy_image[tuple(coordinate)]
            d = [(blank_x, blank_y + self.size), (blank_x , blank_y - self.size),
                 (blank_x + self.size, blank_y), (blank_x - self.size, blank_y)]
            #get the coordinates of the neighbor of the blank image
            if tuple(coordinate) in d:
                list_blank = []
                turtle.pu()
                turtle.goto(self.copy_blank[0])
                print(self.copy_blank[0])
                turtle.register_shape(image_path)
                turtle.shape(image_path)
                turtle.stamp()
                turtle.pu()
                turtle.goto(tuple(coordinate))
                turtle.register_shape(self.blank_path)
                turtle.shape(self.blank_path)
                turtle.stamp()
                image_path = self.copy_image[tuple(coordinate)]
                self.copy_image[self.copy_blank[0]] = image_path
                self.copy_image[tuple(coordinate)] = self.blank_path
                list_blank.append(tuple(coordinate))
                self.copy_blank = list_blank
                print(self.copy_blank)
            break
               #when the coordinate clicked image is the blank image's neighbor
               #swap the image with the blank image              
              

              
def main():
    s = show_puzzle("mario.puz")
    ori_image, ori_blank = s.original_images()
    x, y = s.get_coordinates()
    onclick = click(ori_image, ori_blank, 98, "Images/mario/blank.gif", x, y)
    while turtle.onscreenclick(onclick.get_mouse_click):
        onclick.get_mouse_click(x, y)
####    
                

main()
