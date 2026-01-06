from string import ascii_uppercase
from math import sqrt
from itertools import product



'''
This is a util file that helps to prepare data for the model.

Neighbourhood location coordinates in 2 lists xN and yN 

Generates fixed costs matrix

Generates distance matrix from each neighborhood location to each possible station location

Generate Cartesian product on a grid - for all possible locations for stations.


'''

neighbourhoods_alphanumerical_loc = [
    'F1',
    'B2', 'D2', 'E2', 'G2',
    'E3', 'J3',
    'I4',
    'B5', 'F5', 'H5', 
    'C6', 'E6', 
    'H7', 'I7',
    'C8', 'E8', 'G8', 'H8',
    'D10'

]


# Create a list of letters A to J and list of numbers 1 to 10
letters = list(ascii_uppercase[:10])
numbers = list(range(1,11))

stations_possible_alphanum_loc = [l + str(num) for l in letters for num in numbers]


def split_alphanum_to_coord(alphanum_locs):
    '''
    Function translates alphanumerical locations such as A5 to x y coordinates, such as (1, 5) and splits to separate lists
    Input list of alphanumerical locations
    Output:
        xPart: list of x coordinates,
        yPart: list of y coordinates

    '''
    xPart = []
    yPart = []
    for loc in alphanum_locs:
        alpha = loc[0]
        xcoord = letters.index(alpha) + 1
        ycoord = loc[1:]
        xPart.append(int(xcoord))
        yPart.append(int(ycoord))

    return xPart, yPart

# Neighbourhoods' location coordinates, hard coded
# Example first location is F1 = (6,1) -> x coordinate first element in xN and y coordinate first element in yN
x_n = [6, 2, 4, 5, 7, 5, 10, 9, 2, 6, 8, 3, 5, 8, 9, 3, 5, 7, 8, 4]
y_n = [1, 2, 2, 2, 2, 3, 3, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 8, 8, 10]

assert len(x_n) == len(y_n), 'must be same number of x and y coordinates'
# Test function
assert x_n == split_alphanum_to_coord(neighbourhoods_alphanumerical_loc)[0]
assert y_n == split_alphanum_to_coord(neighbourhoods_alphanumerical_loc)[1]

# Generate distance matrix

def generate_dist_matrix(xN, yN, xS, yS):
    '''
    Generates distance matrix, distance from each neighborhood to every possible station based on x y coordinates
    Resulting matrix has size len(xN) x len(xS)
    Params:
        xN: list of x coordinates of all neighborhoods
        yN: list of y coordinates of all neighborhoods
        xS: list of x coordinates of all stations
        yS: list of y coordinates of all stations

    '''
    dist = lambda i, j: sqrt(((xN[i] - xS[j]) ** 2 + (yN[i] - yS[j]) ** 2)) # function to calculate distance
    dist_matrix = [[dist(i, j) for j in range(len(xS))] for i in range(len(xN))]    # going over each station for each customer
    return dist_matrix


def generate_all_possible_stations_location(x_grid_size = 10, y_grid_size = 10):
    '''
    Generates all possible combinations of x and y coordinates on grid size x_grid_size and y_grid_size
    Default size is 10
    Output: xS, yS
    '''
    coordinates = list(product(range(1, x_grid_size + 1), range(1, y_grid_size + 1)))
    xS, yS = zip(*coordinates)
    xS = list(xS)
    yS = list(yS)

    return xS, yS

# Create fixed cost matrix with standard and non-standard cost based on location
def generate_fixed_costs_matrix(non_standard_xS, non_standard_yS,
                                xS, yS,
                                non_standard_fee = 2500, standard_fee = 2000):

    non_standard_locations = set(zip(non_standard_xS, non_standard_yS))
    fixed_costs = [non_standard_fee if (x,y ) in non_standard_locations else standard_fee for x, y in zip(xS, yS)]
   
    return fixed_costs








