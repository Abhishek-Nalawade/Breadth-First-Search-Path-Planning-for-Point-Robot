
import numpy as np
import cv2

#defining the queue class to use as a data structure
class queue():
    def __init__(self):
        self.pending = list()

    def add(self, child):
        self.pending.insert(0, child)

    def remove(self):
        if self.pending:
            return self.pending.pop()
        return None

    def peek(self):
        if self.pending:
            return self.pending[-1]

    def size(self):
        return len(self.pending)

    def isempty(self):
        if self.pending == []:
            return True
        return False


#created node class in order to save current node and it's parent
class node():
    def __init__(self, current, parent):
        self.current = current
        self.parent = parent

#defining obstacles as well as the boundaries of the map
def obstacles(st):
    if st[1] > (90) and st[1] < 110 and st[0] > (40) and st[0] < (60):

        print("coordinate is in obstacle space")
        return None
    elif ((st[1] - (160))**2 + (st[0] - (50))**2) < 225:

        print("coordinate is in obstacle space")
        return None
    elif st[1] < 0 or st[1] > canvas_size[1]:

        print("coordinate is out of the map boundary")
        return None
    elif st[0] < 0 or st[0] > canvas_size[0]:

        print("coordinate is out of the map boundary")
        return None
    else :
        return st

#removes from the queue
def removing_from_queue():
    check = queue1.remove()
    return check



#this function performs actions and gets children
def super_move_function(currentnode):

    def moveleft(node1):
        child = node1.copy()
        child[1] = child[1] - 1

        #print(currentnode)
        return child

    def moveright(node1):
        child = node1.copy()
        child[1] = child[1] + 1
        return child

    def moveup(node1):
        child = node1.copy()
        child[0] = child[0] + 1
        return child

    def movedown(node1):
        child = node1.copy()
        child[0] = child[0] - 1
        return child

    def up_left(node1):
        child = node1.copy()
        child[0] = child[0] + 1
        child[1] = child[1] - 1
        return child

    def down_left(node1):
        child = node1.copy()
        child[0] = child[0] - 1
        child[1] = child[1] - 1
        return child


    def up_right(node1):
        child = node1.copy()
        child[0] = child[0] + 1
        child[1] = child[1] + 1
        return child

    def down_right(node1):
        child = node1.copy()
        child[0] = child[0] - 1
        child[1] = child[1] + 1
        return child



    new_child = list()
    node = currentnode.current
    new_child.append(moveleft(node))
    new_child.append(moveright(node))
    new_child.append(moveup(node))
    new_child.append(movedown(node))
    new_child.append(up_left(node))
    new_child.append(down_left(node))
    new_child.append(up_right(node))
    new_child.append(down_right(node))

    return new_child, node

#checking if the node is in obstacle space
def check_if_in_obstacle_space(children, parent):
    valid_children = list()
    for i in children:
        poss = obstacles(i)
        if poss != None:
            valid_children.append(i)

    return valid_children, parent


###############################
#####check if the new node is there in the queue
#checking if the node has been visited previously and then appending to the visited_list
def check_if_visited(check):
    for i in range(len(visited_list)):
        if check.current == visited_list[i].current:
            #print("visited")
            return None
    visited_list.append(check)
    #print("not visited")
    return check


#compares new children with goal state and adds them to the queue
#def compare_with_goal(children, parent):





canvas_size = [100,200]
canvas = np.ones((canvas_size[0],canvas_size[1]))
visited_list = []
n = 1
while n > 0:           #if the coordinate is in obstacle space display a message and ask again for coordinates
    start = list()
    goal = list()
    x1 = input("Enter the x co-ordinate of the start point: ")
    y1 = input("Enter the y co-ordinate of the start point: ")
    x2 = input("Enter the x co-ordinate of the goal point: ")
    y2 = input("Enter the y co-ordinate of the goal point: ")
    start.append(int(y1))
    start.append(int(x1))
    goal.append(int(y2))
    goal.append(int(x2))
    lis = [start, goal]
    strt = list()
    count = 0
    for i in lis:
        strt.append(obstacles(i))
    print(strt)
    if strt[0] == None or strt[1] == None:
        continue
    else:
        n = 0

first_node = node(start, None)

print(start,goal)
cv2.imshow("canvas",canvas)    #dimensions of the canvas
cv2.waitKey(0)
