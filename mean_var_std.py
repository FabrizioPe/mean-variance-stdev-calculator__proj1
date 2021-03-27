import numpy as np


def calculate(list_matrix: list) -> dict:
    """
    Calculate the most common statistical quantities for a 3x3 matrix,
    for each axis and for the flattened matrix
    :param list_matrix: a 3x3 matrix as a flat list (ex: [1,2,,4,5,6,7,8,9])
    :return: a dictionary with mean, stdev etc as keys, and list as values
            (ex: mean: [[mean along axis 0], [mean along axis 1], mean of the flatt. matrix])
    """

    if len(list_matrix) != 9:
        raise ValueError('List must contain nine numbers.')

    # converting the list into a 3x3 numpy array
    m = np.array(list_matrix).reshape((3, 3))

    calculations = dict()
    calculations['mean'] = [m.mean(axis=0).tolist(), m.mean(axis=1).tolist(), m.mean()]
    calculations['variance'] = [m.var(axis=0).tolist(), m.var(axis=1).tolist(), m.var()]
    calculations['standard deviation'] = [m.std(axis=0).tolist(), m.std(axis=1).tolist(), m.std()]
    calculations['max'] = [m.max(axis=0).tolist(), m.max(axis=1).tolist(), m.max()]
    calculations['min'] = [m.min(axis=0).tolist(), m.min(axis=1).tolist(), m.min()]
    calculations['sum'] = [m.sum(axis=0).tolist(), m.sum(axis=1).tolist(), m.sum()]

    return calculations
