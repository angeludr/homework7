import numpy as np
import matplotlib.pyplot as plt
import time

def func(x, c):
    return 1 - np.exp(-1 * c * x)
    
def relaxation(startGuess = 1, functionToRelax = None, funcArgs = None, tolerance = 1e-6, maxiter = 20):
    """Function that computes te root via the fixed point (relaxation) method.
    Inputs are a starting guess, a function to use, any function arguments, and a tolerance to exit the function when successive approximations are less than this value"""
    
    guess = startGuess
    
    for i in range(maxiter):
        guess = func(guess, c)
    return guess
    
    
if __name__ == "__main__":
    
    c = 2
    
    print("""a. Write a program to solve this equation for x using the relaxation method for the case c = 2. Calculate your solution to an accuracy of six decimal places.  (3 pts)""")
    print("The solution for part a is:")
    print(relaxation(functionToRelax = func, funcArgs = {'c' :2}))
    
    print('\n')
    
    print("""b) Modify your program to calculate the solution for values of R0 from 0 to 5 in steps of 0.01 and make a plot of P as a function of R0. Save this plot as a png file as an output to your program, with properly labeled axes and titles and such. You should see a clear transition from a regime in which P = 0 to a regime of nonzero P. This is another example of a phase transition. In physics this transition is known as the percolation transition; in epidemiology it is the epidemic threshold.  (7 pts)""")

    # Loop over r0 values from 0 to 5
    r0_values = np.arange(0, 5.0, 0.01)
    c = r0_values
        
    solutions = []
    for r0 in r0_values:
        answer = relaxation(functionToRelax = func,
                            funcArgs = {'c':r0})
        solutions.append(answer)
    
    # Save the output data
    output_textfile = 'epidemic.txt'
    np.savetxt(output_textfile,
               np.array(np.vstack((r0_values, solutions))).T,
               delimiter = ', ', header='R_0, Probability of epidemic')
    
    # Loading txt file to plot graph
    data = np.loadtxt('epidemic.txt', delimiter = ',', skiprows = 1)
    
    # Slicing data to get values
    r0values = data[:,0]
    epidemicProb = data[:,1]
    
    
    # Plot of solutions
    plt.plot(epidemicProb, r0values)
    plt.ylabel('R0 values')
    plt.xlabel('Epidemic Probability')
    
    plt.title('Probability of epidemic')
    
    # Saving plot to directory
    plt.savefig('epidemicPlot.png')
    
    plt.show()

    print('\n')
    print('***Plot saved as epidemicPlot.png***')
    print('\n')
