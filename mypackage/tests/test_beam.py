# test_beam.py
import pytest
import numpy as np
import mypackage as mypkg


def test_euler_bernoulli_beam():
    # Define test parameters
    length = 1.0  # Example length
    num_elements = 10  # Example number of elements
    force = 1.0  # Example force in kN
    expected_displacements = np.array([-0.01811594, -0.36231884, -0.07246377, -0.72463768,
                                   -0.16304348, -1.08695652, -0.28985507, -1.44927536,
                                   -0.45289855, -1.8115942, -0.65217391, -2.17391304,
                                   -0.88768116, -2.53623188, -1.15942029, -2.89855072,
                                   -1.4673913, -3.26086957, -1.8115942, -3.62318841])
 
    # Call the function
    displacement = mypkg.euler_bernoulli_beam(length, num_elements, force)
    
    # Define assertions
    # Add your assertions based on the expected behavior of the function
    assert isinstance(displacement, np.ndarray)
    assert len(displacement) == 2*num_elements
    np.testing.assert_allclose(displacement, expected_displacements, atol=1e-8),f" We have successfully verified the displacement"
    # Add more assertions as needed
