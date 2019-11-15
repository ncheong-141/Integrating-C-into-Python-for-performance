# Integrating-C-into-Python-for-performance

The objective of this project was to integrate C++ functions into Python for performance and test different data type inputs 
(C++ std::vector, Python List and NumPy array)

The steps performed: 
1. Set up MSVS (C++ IDE for windows) for creating a .pyd file (the Python DLL). 
2. Create functions and Python interface using Pybind11. 
3. Import functions into Python and test functions. 
  - Testing functions entailed:
    - Checking outputs were the same. 
    - Timing exectution.
    - Comparing C++ and Python function variant times. 
    
    
In order to run the Python script, the "Cxx_PythonFunction_variant.pyd" file must be in your Python "DLLs" folder. However, the results are
below: 




    Selective sort algorithm: test output and execution time using std::vector BY REFERENCE (requires custom dtype IntVector)

    C++ function variant took:      0.03873 seconds
    Python function variant took:   4.30719 seconds

    C++ took 0.0090% of the time of Python. (111.21 times faster)
    C++ and Python function outputs match for: | selective_sort | 



    Selective sort algorithm: test output and execution time using PY::LIST BY REFERENCE (requires Python dtype)

    C++ function variant took:      1.38211 seconds
    Python function variant took:   4.81058 seconds

    C++ took 0.2873% of the time of Python. (3.48 times faster)
    C++ and Python function outputs match for: | selective_sort_pylist | 



    Selective sort algorithm: test output and execution time using NP ARRAY BY REFERENCE (requires Numpy dtype)

    C++ function variant took:      0.34305 seconds
    Python function variant took:   4.71227 seconds

    C++ took 0.0728% of the time of Python. (13.73 times faster)
    C++ and Python function outputs match for: | selective_sort_numparr | 



There is clear performance advantages integrating C++ functions into Python, particularly by integrating C++ types (the std::vector<int>)) into Python and passing by reference. This is likely due to moreorless using "pure" c++, whereas with the Python List and NumPy array types there is an additional "middle man" in order to use Python types within C++.

However, the cost of the huge performance gain by using C++ datatypes in Python is having to use C++ datatypes within Python, where, for example, you can lose functionality of NumPy by not using NumPy arrays (unless you copy data between C++ arrays and NumPy arrays, which is the default type conversion mechanic that PyBind11 does by default if you dont pass by reference). 

Furthermore, since you are unable to see the implementation of the C++ functions/if you dont code on C++, Pybind11 offers an option
to display documentation of a C++ function in Python. Here, I have inputed the equivalent Python code as well as a function description. 
For example, 


>> getDescriptionAndEquivalentPythonCode(cxx.selective_sort)

Output:

        ---- Selective sort algorithm for ordering data minimum to maximum using C++ std::vector<int> datatype ----

        Equivalent Python code: 

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
