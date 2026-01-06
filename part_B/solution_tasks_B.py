from util_generate_data_B import *

from prim_alg_B import prim
from part_B.util_visualize import *

def solve_tasks():
    # Prepare data for solving the tasks
    factors = [1, 2, 4, 1] # factors of 5 -> 5 , 10, 20 , 5 years

    weights = [calculate_weights(d,t, var_cst, f) for f in factors]   # weights_5y, weights_10y, ...
    networks = [generate_network(edges, w) for w in weights]    # network_5y, network_10y, ...

    networks[-1] = remove_edge(networks[-1], 'N', 'S')

    assert len(networks) == len(weights) == len(factors), 'should be 5 networks'

    start = 'N'

    tasks = [f'{5*f} year utilization' for f in factors]
    tasks[-1] = tasks[-1] + ' (no road between Northern and Southern) '

    # Find MST for each network
    for task, network in zip(tasks, networks):
        print('\nSolving ' + task)
        print("=" * 30)

        mst = prim(network, start)
        assert len(networks[0]) == len(mst) + 1, 'MST must have n-1 edges'

        print('Minimum connected network: ' , mst)
        total_cost = sum(w for _,_, w in mst)
        print(f'Total profit: ${-total_cost:.2f} millions')

        title = f'{task} \nTotal profit/loss is ${-1 * total_cost:,.0f} millions'
        G = create_G_from_network(network=network)
        MST = create_G_from_mst(mst)

        # Visualize solution, uncomment in case of interest
        #plot_mst(G, MST, title)





if __name__ == '__main__':
    solve_tasks()

