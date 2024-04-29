import numpy as np


def euler_bernoulli_beam(length, num_elements, force):
    """
    Calculate the displacement of an Euler-Bernoulli beam.

    :param length: The length of the rod (in meters).
    :type length: float
    :param num_elements: The number of elements in the beam.
    :type num_elements: int
    :param force: The applied force at the right tip (in kN).
    :type force: float

    :return: The displacement of the beam.
    :rtype: numpy.ndarray

    This function calculates the displacement of an Euler-Bernoulli beam given its length, the number of elements in the beam, and the applied force at the right tip. The beam is modeled as a series of massless, elastic rods connected by massless, rigid joints. The displacement is calculated using the Euler-Bernoulli beam equation, which takes into account the mass, stiffness, and boundary conditions of the beam.

    The function first computes the density, Young's modulus, width, and thickness of the beam, as well as its moment of inertia and cross-sectional area. It then constructs the mass and stiffness matrices for the beam, taking into account the element length and the boundary conditions (fixing the left tip). Finally, the function solves for the displacement of the beam using the stiffness matrix and the applied force.

    The function uses the NumPy library for numerical computations.
    """
    rho = 2700  # Density
    E = 69e9    # Young Modulus
    h = 0.02    # Width of the beam in meters
    b = 0.006   # Thickness of the beam in meters
    I = (b * h**3) / 12
    A = b * h   # Cross section area
    Le = length / num_elements  # Element length
    
    # Mass matrix
    M = np.zeros((2*num_elements+2, 2*num_elements+2))
    for i in range(num_elements):
        M[2*i:2*i+4, 2*i:2*i+4] += rho*A*Le/420*np.array([[156, 22*Le, 54, -13*Le], 
                                                            [22*Le, 4*Le**2, 13*Le, -3*Le**2], 
                                                            [54, 13*Le, 156, -22*Le], 
                                                            [-13*Le, -3*Le**2, -22*Le, 4*Le**2]])
    
    # Stiffness matrix
    K = np.zeros((2*num_elements+2, 2*num_elements+2))
    for i in range(num_elements):
        K[2*i:2*i+4, 2*i:2*i+4] += E*I/Le**3*np.array([[12, 6*Le, -12, 6*Le], 
                                                        [6*Le, 4*Le**2, -6*Le, 2*Le**2], 
                                                        [-12, -6*Le, 12, -6*Le], 
                                                        [6*Le, 2*Le**2, -6*Le, 4*Le**2]])
    
    # Applying boundary conditions (fixing left tip)
    K_bc = K[2:, 2:]
    F_bc = np.zeros(2*num_elements)
    F_bc[-1] = -force * 1000  # Converting kN to N
    
    # Solving for displacement
    displacement = np.linalg.solve(K_bc, F_bc)
    
    return displacement


# # Example usage
# length = 1
# num_elements = 10
# force = 1

# disp = euler_bernoulli_beam(length, num_elements, force)
# print(f"the displacement is: {disp}")