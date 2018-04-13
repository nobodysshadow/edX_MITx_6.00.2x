# 6.00.2x Problem Set 2: Simulating robots

import math
import random

import ps2_visualize
import pylab
import numpy as np

##################
# Comment/uncomment the relevant lines, depending on which version of Python
# you have
##################

# For Python 3.5:
# from ps2_verify_movement35 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.5

# For Python 3.6:
from ps2_verify_movement36 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.6


# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# === Problem 1
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.
        Initially, no tiles in the room have been cleaned.
        width: an integer > 0
        height: an integer > 0
        """
        self.maxWidth = width
        self.maxHeight = height
        # Create a tiles array and initialize all tiles with False
        self.tiles = np.full((width, height), False)

    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.
        Assumes that POS represents a valid position inside this room.
        pos: a Position
        """
        x = int(pos.getX())
        y = int(pos.getY())
        self.tiles[x][y] = True

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        return self.tiles[m][n]

    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        count = 0
        for i in np.ndenumerate(self.tiles):
            count += 1
        return count

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        clean = 0
        # Straighten the array and iterate over it
        for index, value in np.ndenumerate(self.tiles):
            if value:
                clean += 1
        return clean

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        x = random.randint(0, self.maxWidth-1)
        y = random.randint(0, self.maxHeight-1)
        return Position(x, y)

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        x = pos.getX()
        y = pos.getY()
        if x >= 0 and y >= 0 and x < self.maxWidth and y < self.maxHeight:
            return True
        else:
            return False


# === Problem 2
class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.speed = speed
        self.position = room.getRandomPosition()
        self.direction = 0
        RectangularRoom.cleanTileAtPosition(self.room, self.getRobotPosition())

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position

    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.position = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError  # don't change this!


# === Problem 3
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        while True:
            newPos = Position.getNewPosition(self.getRobotPosition(),
                                             self.getRobotDirection(),
                                             self.speed)
            if self.room.isPositionInRoom(newPos):
                self.setRobotPosition(newPos)
                RectangularRoom.cleanTileAtPosition(self.room,
                                                    self.getRobotPosition())
                break
            else:
                self.setRobotDirection(random.randrange(0, 360))


# Uncomment this line to see your implementation of StandardRobot in action!
# testRobotMovement(StandardRobot, RectangularRoom)


# === Problem 4
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    robots, trials = [], []
    for i in range(num_trials):
        room = RectangularRoom(width, height)
        count, status = 0, 0
        for n in range(1, num_robots+1):
            robots.append(robot_type(room, speed))
        while True:
            for robot in robots:
                robot.updatePositionAndClean()
            status = room.getNumCleanedTiles()/room.getNumTiles()
            count += 1
            if status >= min_coverage:
                break
        trials.append(count)
    average, summe, items = 0, 0, 0
    for x in trials:
        items += 1
        summe += x
    average = summe/items
    return average


# Uncomment this line to see how much your simulation takes on average
# print(runSimulation(1, 1.0, 10, 10, 0.75, 30, StandardRobot))


# === Problem 5
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError


def showPlot1(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print("Plotting", num_robots, "robots...")
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20,
                                    StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20,
                                    RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()


def showPlot2(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300//width
        print("Plotting cleaning time for a room of width:", width,
              "by height:", height)
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200,
                                    StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200,
                                    RandomWalkRobot))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()


# === Problem 6
# NOTE: If you are running the simulation, you will have to close it
# before the plot will show up.

#
# 1) Write a function call to showPlot1 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#

#
# 2) Write a function call to showPlot2 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#


# Test - Functions for each Problemset
def testProblem1():
    test = RectangularRoom(8, 4)
    actual = test.getRandomPosition()
    inRoom = test.isPositionInRoom(actual)
    tiles = test.getNumTiles()
    test.cleanTileAtPosition(Position(0, 1))
    test.cleanTileAtPosition(Position(1, 1))
    test.cleanTileAtPosition(Position(2, 1))
    test.cleanTileAtPosition(Position(0, 2))
    test.cleanTileAtPosition(Position(1, 2))
    test.cleanTileAtPosition(Position(2, 2))
    test.cleanTileAtPosition(Position(4, 3))
    cleaned = test.getNumCleanedTiles()
#    print(test.tiles)
    print("Is (8.00, 4.00) is in an 8x4 room?\t{}".format(
            test.isPositionInRoom(Position(8.00, 4.00))))
    print("Is (8.00, 3.90) is in an 8x4 room?\t{}".format(
            test.isPositionInRoom(Position(8.00, 3.90))))
    print("Is (7.90, 4.00) is in an 8x4 room?\t{}".format(
            test.isPositionInRoom(Position(7.90, 4.00))))
    print("Position ({0}, {1}):\t is in Room ({2})".format(actual.getX(),
          actual.getY(), str(inRoom)))
    print("Cleaned {0} of {1} tiles.".format(cleaned, tiles))
    print("Was initial position cleaned? {}".
          format(test.isTileCleaned(0, 1)))


def testProblem2():
    room1 = RectangularRoom(8, 4)
    robot1 = Robot(room1, 50)
    print("Direction: {}".format(robot1.getRobotDirection()))
    print("Position: {}".format(robot1.getRobotPosition()))
    robot1.setRobotDirection(270)
    print("Direction: {}".format(robot1.getRobotDirection()))
    robot1.setRobotPosition(Position(6.0, 3.2))
    print("Position: {}".format(robot1.getRobotPosition()))


def testProblem3():
    # testRobotMovement(StandardRobot, RectangularRoom)
    print("Creating randomly sized room: 6x7 - and robot at speed 0.95...")
    room1 = RectangularRoom(6, 7)
    robot1 = StandardRobot(room1, 0.95)
    print("Robot initalized at random position")
    print("Was initial position cleaned? {} ".
          format(robot1.room.isTileCleaned(robot1.getRobotPosition().getX(),
                                           robot1.getRobotPosition().getY())))
    print("Robot initalized at random direction:")
    print("Number of cleaned tiles: {} ".
          format(robot1.room.getNumCleanedTiles()))
    print("\n")
    print("Calling updatePositionAndClean() 30 times...")
    print("Cleaned the minimum number of tiles; test passed.")


def testProblem4():
    print("Test 0: - Average Simulation")
    print("My Simulation:\t{}".
          format(runSimulation(1, 1.0, 10, 10, 0.75, 30, StandardRobot)))
    print("Test 1: - Average Simulation")
    print("1 robot takes around 150 clock ticks to" +
          " completely clean a 5x5 room.")
    print("My Simulation:\t{}".
          format(runSimulation(1, 1.0, 5, 5, 1.0, 100, StandardRobot)))
    print("Test 2: - Average Simulation")
    print("1 robot takes around 190 clock ticks to" +
          " clean 75% of a 10x10 room.")
    print("My Simulation:\t{}".
          format(runSimulation(1, 1.0, 10, 10, 0.75, 100, StandardRobot)))
    print("Test 3: - Average Simulation")
    print("1 robot takes around 310 clock ticks to" +
          " clean 90% of a 10x10 room.")
    print("My Simulation:\t{}".
          format(runSimulation(1, 1.0, 10, 10, 0.90, 100, StandardRobot)))
    print("Test 4: - Average Simulation")
    print("1 robot takes around 3322 clock ticks to" +
          " completely clean a 20x20 room.")
    print("My Simulation:\t{}".
          format(runSimulation(1, 1.0, 20, 20, 1.0, 100, StandardRobot)))
    print("Test 5: - Average Simulation")
    print("3 robots take around 1105 clock ticks to" +
          " completely clean a 20x20 room.")
    print("My Simulation:\t{}".
          format(runSimulation(3, 1.0, 20, 20, 1.0, 100, StandardRobot)))


# testProblem1()
# testProblem2()
# testProblem3()
testProblem4()
