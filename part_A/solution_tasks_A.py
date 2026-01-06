from setuptools.command.rotate import rotate

from part_A import models_A
from util_generate_data_A import *
from models_A import *
from util_visualize_A import *



solver = 'appsi_highs'
SOLVER = pyo.SolverFactory(solver)

def solve_tasks_A():
    
    # Prepare data
    xN, yN = split_alphanum_to_coord(neighbourhoods_alphanumerical_loc) # x and y coordingates of neighbourhod locations
    xS, yS = generate_all_possible_stations_location()  # possible station locations
    dist_matrix = generate_dist_matrix(xN, yN, xS, yS)
    VAR_CST = 100
    
    # Generate fixed costs matrix
    central_loc = ['E5', 'E6', 'F5', 'F6']
    x_central, y_central = split_alphanum_to_coord(central_loc)
    fixed_costs = generate_fixed_costs_matrix(x_central, y_central, xS, yS)

    # E5 = 54
    assert [fixed_costs[i] == 2500 for i in [54, 55, 64, 65]], 'central regions cost must be 2500'
    assert [fixed_costs[i] == 2000 for i in range(0, 100) if i not in [54, 55, 64, 65]], 'cost must be 2000'


    # Lower bound for number of neighbourhoods to serve
    b_fractions = [14, 16, 18, 20]

    tasks = ['Station location to serve all neighbourhoods', 'Exactly one station to built']

    serve_all = StationModelToServeAll(fixed_costs, dist_matrix, VAR_CST)
    one_station = StationModelOnlyOneStation(fixed_costs, dist_matrix, VAR_CST)

    models = [serve_all, one_station]

    for b in b_fractions:
        tasks.append(f'Connecting at least {b} neighbourhoods')
        models.append(StationModelFractionServed(fixed_costs, dist_matrix, VAR_CST, b))

    assert len(tasks) == len(models),  'number of tasks not equal to number of models'


    for task, m in zip(tasks, models):
        print('\nSolving ' + task)
        print("=" * 30)

        SOLVER.solve(m)


        # Translate stations built x_j and neighbourhood i served at station j y_i_j to alphanumerical names
        x_var, y_var, val = GetSolutionFiltered(m)
        stations_built = [stations_possible_alphanum_loc[station] for station in x_var]
        neigh_served = [
            (neighbourhoods_alphanumerical_loc[n],
             stations_possible_alphanum_loc[s])
            for n, s in y_var
        ]

        print(f'Stations built : {stations_built}')
        print(f'Neighbourhoods served at stations : {neigh_served}')

        title = f'{task}, total cost is ${val:,.2f}'

        # Visualize solution, uncomment if plots are of interest
        #ShowStationLocation(xN, yN, xS, yS, X, Y, v, title)






if __name__ == '__main__':
    solve_tasks_A()