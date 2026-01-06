import pyomo.environ as pyo

# Common part of the models
def StationLocationCommon(fixed_costs, distance_matrix, unit_var_cst):
    # Create model
    model = pyo.ConcreteModel('Station Location')
    # Define sets
    model.neighborhoods = pyo.Set(initialize=range(len(distance_matrix)))   # set of neighborhoods
    model.stations = pyo.Set(initialize=range(len(fixed_costs)))       # set of stations

    # Decision variables
    model.x = pyo.Var(model.stations, domain=pyo.Binary)
    model.y = pyo.Var(model.neighborhoods, model.stations, domain=pyo.Binary)

    # Expressions for fixed and variable cost
    @model.Expression()
    def fixed_cost(m):
        return sum(fixed_costs[j] * m.x[j] for j in m.stations)


    @model.Expression()
    def variable_cost(m):
        total_dist =  sum(
            distance_matrix[i][j] * m.y[i,j]
            for i in m.neighborhoods
            for j in m.stations
        )
        total_var_cost = unit_var_cst * total_dist
        return total_var_cost
    
    @model.Objective(sense=pyo.minimize)
    def total_cost(m):
        return m.fixed_cost + m.variable_cost
    
    @model.Constraint(model.neighborhoods, model.stations)
    def serve_if_open(m, i, j):
        return m.y[i,j] <= m.x[j]
            

    return model

# Model for task 2 - Connecting all the neighbourhoods, unlimited stations
def StationModelToServeAll(fixed_costs, distance_matrix, unit_var_cst):
    model = StationLocationCommon(fixed_costs, distance_matrix, unit_var_cst)

    @model.Constraint(model.neighborhoods)
    def one_station_per_neigh(m, i):
        return sum(m.y[i,j] for j in m.stations) == 1

    return model

# Model for task 3 - connect all, exactly 1 station
def StationModelOnlyOneStation(fixed_costs, distance_matrix, unit_var_cst):
    model = StationModelToServeAll(fixed_costs, distance_matrix, unit_var_cst)

    @model.Constraint()
    def only_one_station(m):
        return sum(m.x[j] for j in model.stations) == 1
    
    return model

# Model for task 4
def StationModelFractionServed(fixed_costs, distance_matrix, unit_var_cst, b):
    model = StationLocationCommon(fixed_costs, distance_matrix, unit_var_cst)

    @model.Constraint(model.neighborhoods)
    def at_most_one_station_per_neigh(m, i):
        return sum(m.y[i,j] for j in m.stations) <= 1


    @model.Constraint()
    def fraction_served(m):
        return sum(m.y[i,j] for i in m.neighborhoods for j in m.stations) >= b
    
    return model


def GetSolutionFiltered(model):
    '''
    Filters out 0 values from decision variables and returns
    indexes of 1 values and objective value

    '''
    X = [pyo.value(model.x[j]) for j in model.stations]
    Y = [[pyo.value(model.y[i, j])  for j in model.stations] for i in model.neighborhoods]

    built_stations = [j for j, val in enumerate(X) if val == 1.0]   # indexes of built stations
    neigh_stat = [(i,j) for i in model.neighborhoods for j in model.stations if Y[i][j] == 1.0] # index pairs i, j - neigh i connected to station j
    obj_val = pyo.value(model.total_cost)   # total cost

    return built_stations, neigh_stat, obj_val


