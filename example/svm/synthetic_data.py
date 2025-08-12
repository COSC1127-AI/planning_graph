# https://gist.github.com/agramfort/2071994

from scipy import stats
import numpy as np
import numpy.random as rd


def synthetic_data(k, n, c_max, m, n_maxs):
    """Create a synthetic dataset used for intuition testing and training purposes

       Parameters:
       k: int, the number of problems
       n: int, the number of action schemas 
       c_max: int, maximum cost
       m: int array, shape(k): 
       stores the number of vector data for each problem
       n_maxs: int array, shape(k,2): 
       stores [n_max, n2_max], the upper bound - k/3 for each problem 

       Returns:
       data_set: float array, shape (sum(m), n+2*n^2): 
       the synthetic dataset composed of k probelms, each problem contains m[i] feature vectors of length n+2n^2
       cost: int array, shape(sum(m), 2): 
       the cost array, cost[i,0] correspond to the cost for data_set[i], cost[i, 1] correspond to the problem label corresponding to input m
    """
    # create the data structure
    num_vec = np.sum(m)
    num_features = n + 2*n**2
    data_set = np.zeros((num_features,num_vec), dtype = np.float)
    class_label = np.zeros(num_vec, dtype = int)
    current_vec = 0
    # loop to generate synthetic dataset
    for i in range(k):
        next_vec = current_vec + m[i]
        # update data set
        n_max = n_maxs[i][0] + np.floor(k/3)
        n2_max = n_maxs[i][1] + np.floor(k/3)
        data_set[0:n, current_vec:next_vec] = rd.uniform(low = 0.0, high = n_max, size = (n, m[i]))
        data_set[n:n+2*n**2, current_vec:next_vec] = rd.uniform(low = 0.0, high = n2_max, size = (2*n**2, m[i]))
        # update class label
        class_label[current_vec:next_vec] = i
        # update vec index
        current_vec = next_vec
    cost = rd.randint(low = 1, high = c_max, size = num_vec)
    cost = np.column_stack((cost,class_label))

    return data_set.T, cost
        
def create_synthetic_data(k, n, c_max, s, m_max, n_max, n2_max):
    """Randomly generate a synthetic dataset used for intuition testing and training purposes

       Parameters:
       k: int, the number of problems
       n: int, the number of action schemas 
       c_max: int, maximum cost
       s: int, number of states, lower bound of m
       m_max: int, upper bound of m 
       n_max: int, upper bound of n data for all problem 
       n_max2: int, upper bound of 2*n^2 data for all problem

       Returns:
       problem_index: array of ending indexs for ending of each problem, each problem i begins at i and end at i+1
       data_set: float array, shape (sum(m), n+2*n^2): 
       the synthetic dataset composed of k probelms, each problem contains m[i] feature vectors of length n+2n^2
       cost: int array, shape(sum(m), 2): 
       the cost array, cost[i,0] correspond to the cost for data_set[i], cost[i, 1] correspond to the problem label corresponding to input m
    """
    m = rd.randint(low = s, high=m_max, size = k)
    n_maxs = np.zeros((k, 2), dtype = int)
    n_maxs[:,0] = n_max
    n_maxs[:,1] = n2_max
    data_set, cost = synthetic_data(k, n, c_max, m, n_maxs)
    end_index = np.cumsum(m)
    return np.insert(end_index,0,0), data_set, cost


