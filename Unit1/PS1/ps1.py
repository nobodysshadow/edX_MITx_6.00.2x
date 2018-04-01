###################################
# 6.00.2x Problem Set 1: Space Cows

from ps1_partition import get_partitions
import time

# ===============================
# Part A: Transporting Space Cows
# ===============================


def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as
    values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')

    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows.
    The returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow
       that will fit to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    '''
    # --- Version 1 ---
    cowsList = sorted(iter([(v, k) for (k, v) in cows.items()]), reverse=True)
    trips, ships = [], []
    totalTrips, totalWeight = 0, 0
    for i in range(len(cowsList)+1):
        for j in range(len(cowsList)+1):
            if len(cowsList) >= 1:
                try:
                    if (totalWeight+cowsList[j][0]) <= limit:
                        ships.append(cowsList[j][1])
                        totalWeight += cowsList[j][0]
                        cowsList.remove(cowsList[j])
                    else:
                        trips.append(ships[:])
                        totalTrips += 1
                        ships.clear()
                        totalWeight = 0
                        break
                except IndexError:
                    if len(cowsList) >= 1:
                        if (totalWeight+cowsList[0][0]) <= limit:
                            ships.append(cowsList[0][1])
                            cowsList.remove(cowsList[0])
                    trips.append(ships[:])
                    totalTrips += 1
                    ships.clear()
                    totalWeight = 0
                    break
    return trips

    # --- Version 2 ---
    maxTrips = len(cows)
    cowsList = sorted(iter([(v, k) for (k, v) in cows.items()]), reverse=True)
    trips, ships = [], []
    totalTrips, totalWeight = 0, 0
    for i in range(maxTrips):
        if cowsList != []:
            ships.append(cowsList[0][1])
            totalWeight += cowsList[0][0]
            cowsList.remove(cowsList[0])
        for j in cowsList:
            if (totalWeight+j[0]) <= limit:
                ships.append(j[1])
                totalWeight += j[0]
                cowsList.remove(j)
            else:
                next
        if ships != []:
            trips.append(ships[:])
            totalTrips += 1
            ships.clear()
            totalWeight = 0
    return trips
    '''
    # --- Version 3 ---
    cowsList = sorted(iter([(v, k) for (k, v) in cows.items()]), reverse=True)
    cowWeights = sorted(cows.values(), reverse=True)
    maxTrips = len(cowWeights)+1
    trips, ships = [], []
    totalTrips, totalWeight = 0, 0
    for i in range(maxTrips):
        if cowsList != []:
            ships.append(cowsList[0][1])
            totalWeight += cowsList[0][0]
            cowsList.remove(cowsList[0])
        for j in cowWeights:
            if (totalWeight+j) <= limit:
                for x in cowsList:
                    if x[0] == j:
                        ships.append(x[1])
                        totalWeight += x[0]
                        cowsList.remove(x)
            else:
                next
        if ships != []:
            trips.append(ships[:])
            totalTrips += 1
            ships.clear()
            totalWeight = 0
    return trips


# Problem 2
def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following
    method:

    1. Enumerate all possible ways that the cows can be divided into separate
       trips
    2. Select the allocation that minimizes the number of trips without making
       any trip that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # --- Version 1 ---
    trips = []
    for trip in get_partitions(cows.keys()):
        for ship in trip:
            totalWeight = 0
            for cow in ship:
                totalWeight += cows.get(cow)
            if totalWeight <= limit:
                trips.append(ship)
        # print('Test: {0}, \nvers: {1}\nLimit = {2} | Tripweight = {3}'.format(trips, trip, limit, totalWeight))
        if trip == trips:
            return trips
        else:
            trips.clear()


# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run
    your greedy_cow_transport and brute_force_cow_transport functions here.
    Use the default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.

    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows("ps1_cow_data.txt")
    start = time.time()
    print(greedy_cow_transport(cows))
    end = time.time()
    print("Speed - Greedy: {0:.7f}\n\n".format(end-start))
    start = time.time()
    print(brute_force_cow_transport(cows))
    end = time.time()
    print("Speed - Brutef: {0:.7f}\n\n".format(end-start))


"""
Here is some test data for you to see the results of your algorithms with.
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

# cows = load_cows("ps1_cow_data.txt")
# limit = 10
# print(cows)

# print(greedy_cow_transport(cows, limit))
# print(brute_force_cow_transport(cows, limit))

'''
print("Problem 1 | Test 1:")
start = time.time()
cows = load_cows("ps1_cow_dataE1.txt")
limit = 100
print(greedy_cow_transport(cows, limit))
end = time.time()
print("Speed: {0}\n\n".format(end-start))
print("Problem 1 | Test 2:")
start = time.time()
cows = load_cows("ps1_cow_dataE2.txt")
limit = 100
print(greedy_cow_transport(cows, limit))
end = time.time()
print("Speed: {0}\n\n".format(end-start))
print("Problem 1 | Test 3:")
start = time.time()
cows = load_cows("ps1_cow_dataE3.txt")
limit = 120
print(greedy_cow_transport(cows, limit))
end = time.time()
print("Speed: {0}\n\n".format(end-start))
print("Problem 2 | Test 1:")
start = time.time()
# print("Correct: [['MooMoo', 'Horns', 'Miss Bella'], ['Milkshake', 'Lotus', 'Boo']]")
cows = load_cows("ps1_cow_dataE4.txt")
limit = 100
print(brute_force_cow_transport(cows, limit))
end = time.time()
print("Speed: {0}\n\n".format(end-start))
print("Problem 2 | Test 2:")
start = time.time()
# print("Correct: [['Buttercup'], ['Daisy'], ['Betsy']]")
cows = load_cows("ps1_cow_dataE5.txt")
limit = 75
print(brute_force_cow_transport(cows, limit))
end = time.time()
print("Speed: {0}\n\n".format(end-start))
print("Problem 2 | Test 3:")
start = time.time()
# print("Correct: [['Starlight', 'Betsy', 'Luna', 'Buttercup']]")
cows = load_cows("ps1_cow_dataE6.txt")
limit = 145
print(brute_force_cow_transport(cows, limit))
end = time.time()
print("Speed: {0}\n\n".format(end-start))
'''
compare_cow_transport_algorithms()
