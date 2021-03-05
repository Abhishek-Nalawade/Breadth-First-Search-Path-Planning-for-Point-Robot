
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


def obstacles(st, go):
    if st[0] > 90 and st[0] < 110 and st[1] > 40 and st[1] < 60:
        st = []
        go = []
        print(start coordinate is in obstacle space)
        return st ,go
    elif go[0] > 90 and go[0] < 110 and go[1] > 40 and go[1] < 60:
        st = []
        go = []
        print(goal coordinate is in obstacle space)
        return st ,go
    elif ((st[0] - 160)**2 + (st[1] - 50)**2) < 225:
        st = []
        go = []
        print(start coordinate is in obstacle space)
        return st ,go
    elif ((go[0] - 160)**2 + (go[1] - 50)**2) < 225:
        st = []
        go = []
        print(goal coordinate is in obstacle space)
        return st ,go
    else :
        return st ,go

#removes from the queue
def removing_from_queue():
    check = queue1.remove()
    return check







#this function performs actions and gets children and calls the locate_0 function as well
def super_move_function(currentnode):

    def moveleft(node1):
        child = node1.copy()
        child =

        #print(currentnode)
        return child

    def moveright(node1):
        child = node1.copy()

        return child

    def moveup(node1):
        child = node1.copy()

        return child

    def movedown(node1):
        child = node1.copy()

        return child

    def up_left(node1):
        child = node1.copy()

        return child

    def down_left(node1):
        child = node1.copy()

        return child


    def up_right(node1):
        child = node1.copy()

        return child

    def down_right(node1):
        child = node1.copy()

        return child



    #node =
    new_child = list()
    
    new_child.append(moveleft(currentnode))
    new_child.append(moveright(currentnode))
    new_child.append(moveup(currentnode))
    new_child.append(movedown(currentnode))
    new_child.append(up_left(currentnode))
    new_child.append(down_left(currentnode))
    new_child.append(up_right(currentnode))
    new_child.append(down_right(currentnode))

    return new_child, node


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






canvas = np.ones((100,200))
start = list()
goal = list()
n = 1
while n > 0:           #if the coordinate is in obstacle space display a message and ask again for coordinates
    x1 = input("Enter the x co-ordinate of the start point: ")
    y1 = input("Enter the y co-ordinate of the start point: ")
    x2 = input("Enter the x co-ordinate of the goal point: ")
    y2 = input("Enter the y co-ordinate of the goal point: ")
    start.append(int(x1))
    start.append(int(y1))
    goal.append(int(x2))
    goal.append(int(y2))
    start, goal = obstacles(start, goal)
    if start != []:
        n = 0

first_node = node(start, None)

print(start)
cv2.imshow("canvas",canvas)    #dimensions of the canvas
cv2.waitKey(0)
