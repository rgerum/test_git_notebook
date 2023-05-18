from helpers import calculate_average
import numpy as np

def test_average():
    values = np.random.rand(5)
    assert calculate_average(values) == np.mean(values)
    np.testing.assert_almost_equal(calculate_average(values), np.mean(values))
    
    
def test_average_shift():
    values = np.random.rand(5)
    
    mean = calculate_average(values)
    assert calculate_average(values+5) == (mean + 5)