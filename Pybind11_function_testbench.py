"""
Project:
Pybind11 Function testbench:
    
    - Checks for: 
        - Timing of functions: time values and comparison (Python and C++)
        - Values are correct (the same)
        
    - Note, avoid excessive calls as Pybind11 has a call overhead which will skew the results. 
    - Although, the above should be considered for high call amount functions. 

Author: Nicholas Chui Wan Cheong
Date:   05/11/2019

"""

# Import Pybind11 wrapped C++ dynamic library (.pyd file)
import Cxx_PythonFunction_variants as cxx; 

# Import modules for testing functions
import random as rand;
import copy
from time import perf_counter
import psutil 


"""
Descriptive functions for verbose output and debugging 
"""
# Get the C++ function variant descriptions and equivalent python code 
def getDescriptionAndEquivalentPythonCode(function) : 
    print(function.__doc__);

def dispDynAddedVars(class_) : 
    print("Dynamically added variables in class", class_ ,class_.__dict__);
    
    
    
""" ================================================================
                            Test bench
===================================================================="""

"""
selection sort algorithm
"""
def selective_sort_py(data, NP): 
    # Start of algorithm (sort selection)
    # Advance down entire list 
    for i in range(0,NP-1) :
        
        # Set the minimum value index is the first index for each iteration 
        minval_index = i; 
        
        # Loop along data and find the smallest data value to sort to top of list (i+1 as)
        for j in range (i+1, NP) :
            
            # Condition to see if the new element is the minimum 
            if data[j] < data[minval_index] :
                # Overwrite old minimum value index
                minval_index = j; 
        
        # After establishing the minimum value index; swap the current (i) list position with established min value
        if minval_index != i :
            copy_element = data[i]; 
            data[i] = data[minval_index];
            data[minval_index] = copy_element;





""" Function to compare the output of a Python and C++ function to ensure it is the same """    
def variant_output_test(fnName, output_py, output_cxx):
     

    """ Preliminary checks """
    # Data length test
    assert len(output_py) == len(output_cxx), f"Error: data lengths of Python and Cxx dont match: Length of Python data {len(output_py)}, length of C++ data {len(output_cxx)}.";
    data_length = len(output_py);   # Since data lengths correspond...
    
    # Data type test (sys.getsizeof does not work for 3rd party types so using primitive element)
    assert type(output_py[0]) == type(output_cxx[0]), f"Error, output of Python and C++ data types do not match.";
    
    
    """ Output checks """
    sum_res = list([0]*data_length);
    for i in range(0,data_length) :
        sum_res[i] = abs(output_py[i] - output_cxx[i]); 
    
    # Note, this wont work with floats due to the round off error. |Change!|
    assert sum(sum_res) == 0 , "Error: cxx and python function output not the same.";

    # If all asserts have been satisfied... 
    print(f"C++ and Python function outputs match for: | {fnName} | ");
    
    


    
""" Function to get the statistics of a function (Execution time and average CPU usage)"""
def test(iters, fn, *functionArgs):
    
    duration  = list([0]*iters);
    
    for i in range (0,iters) :
        
        start = perf_counter();                 # Start timer
        
        """"""
        fn(*functionArgs);                      # Execute function
        #cpu_usage[i] = psutil.cpu_percent();    # Store CPU usage for stats
        """"""
       
        duration[i] = perf_counter() - start;   # Calculate timings 
        
    # Return statistics
    stats = sum(duration)/iters #, sum(cpu_usage)/iters;
    return stats;

# Test function which returns an output (i.e. not passing by referebnce)
def test_wOutput(iters, fn, *functionArgs):
    
    duration  = list([0]*iters);
    
    for i in range (0,iters) :
        
        start = perf_counter();                 # Start timer
        
        """"""
        fnOutput = fn(*functionArgs);                      # Execute function
        #cpu_usage[i] = psutil.cpu_percent();    # Store CPU usage for stats
        """"""
       
        duration[i] = perf_counter() - start;   # Calculate timings 
        
    # Return statistics
    stats = sum(duration)/iters #, sum(cpu_usage)/iters;
    return stats, fnOutput ;




""" function to generate random 1D date for testing function """
def Generate_randomPyCxxData_1D(size, dtype="Please enter a data type int or float") :
    
    # Generate data 
    if dtype == 'int' : 
        data = list([0]*size); 
        data_vect = cxx.VectorInt([0]*size);
    
        for i in range (0,size) :
            data[i] = rand.randint(0,100);
            data_vect[i] = copy.deepcopy(data[i]);
        
        return data, data_vect;
    
    elif dtype == 'float' : 
        print('Not implemented yet')
    else: 
        if dtype != 'int' and dtype != 'float' :
            raise AssertionError("Error: Please select datatype as 'int' or 'float' in function 'gen_RandomPyCxxData_1D'.")



    
if __name__ == '__main__' :

    # Test parameters
    iters = 1;          # Number of test iterations
    NP    = 10000;      # Number of data points in 1D data. 
    
    

    """ Selective sort test using C++ datatype std::vector<int> (IntVector)
    =====================================================================================================================================
    """
    print("Selective sort algorithm: test output and execution time using std::vector BY REFERENCE (requires custom dtype IntVector (std::vector<int>))")
    
    # Generate data 
    data_py, data_cxx = Generate_randomPyCxxData_1D(NP, 'int');
    
    # --------- Time C++ ---------
    duration_Cxx = test(iters, cxx.selective_sort, data_cxx, NP);
    print('\nC++ function variant took:      {:.5f} seconds'.format(duration_Cxx))
    
   
    # --------- Time Python ---------
    duration_Py = test(iters, selective_sort_py, data_py, NP);
    print('Python function variant took:   {:.5f} seconds\n'.format(duration_Py))
    
    # Statistics of timings 
    print(f"C++ took {duration_Cxx/duration_Py:.4f}% of the time of Python. ({duration_Py/duration_Cxx:.2f} times faster)")
    
    # Check output
    variant_output_test("selective_sort",data_py, data_cxx)
    """ ============================================================================================================================= """
    
    
    
    
    """ Selective sort test passing in a Python List by reference
    =====================================================================================================================================
    """ 
    print("\n\nSelective sort algorithm: test output and execution time using PY::LIST BY REFERENCE (requires Python dtype)")

    # Generate data 
    data_py, data_cxx = Generate_randomPyCxxData_1D(NP, 'int');
    data_cxx = copy.deepcopy(data_py); 
    
    # --------- Time C++ ---------
    duration_Cxx = test(iters, cxx.selective_sort_pylist, data_cxx, NP);
    print('\nC++ function variant took:      {:.5f} seconds'.format(duration_Cxx))
    
   
    # --------- Time Python ---------
    duration_Py = test(iters, selective_sort_py, data_py, NP);
    print('Python function variant took:   {:.5f} seconds\n'.format(duration_Py))

    
    # Statistics of timings 
    print(f"C++ took {duration_Cxx/duration_Py:.4f}% of the time of Python. ({duration_Py/duration_Cxx:.2f} times faster)")
    
    # Check output
    variant_output_test("selective_sort_pylist",data_py, data_cxx)
    
    
    
    
    """ Selective sort test passing in a numpy array by reference
    =====================================================================================================================================
    """ 
    print("\n\nSelective sort algorithm: test output and execution time using NP ARRAY BY REFERENCE (requires Numpy dtype)")

    # Generate data 
    data_py, data_cxx = Generate_randomPyCxxData_1D(NP, 'int');
    import numpy as np; 
    data_cxx = np.zeros(NP, dtype =int)
    for i in range(0,NP) : 
        data_cxx[i] = copy.deepcopy(data_py[i]); 
        data_py[i] = np.int32(data_py[i]);          # int for list default is "int",  int for numpy default is "int32" (since C ints are 32 bits by default). 
    
    # --------- Time C++ ---------
    duration_Cxx = test(iters, cxx.selective_sort_numpyarr, data_cxx, NP);
    print('\nC++ function variant took:      {:.5f} seconds'.format(duration_Cxx))
    
   
    # --------- Time Python ---------
    duration_Py = test(iters, selective_sort_py, data_py, NP);
    print('Python function variant took:   {:.5f} seconds\n'.format(duration_Py))

    
    # Statistics of timings 
    print(f"C++ took {duration_Cxx/duration_Py:.4f}% of the time of Python. ({duration_Py/duration_Cxx:.2f} times faster)")
    
    # Check output
    variant_output_test("selective_sort_pylist",data_py, data_cxx)
