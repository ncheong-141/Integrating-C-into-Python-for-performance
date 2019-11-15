#pragma once


/* Pybind11 interface file for Pybind11 code to interface between C++ and Python */
#include "pybind11/pybind11.h"

//  Additional pybind headers for STL conversion 
#include "pybind11/stl.h"	
#include "pybind11/stl_bind.h"

// Include any additional internal modules 
#include "SL_Runtime_Interface.h"

#include <iostream>
#include <vector>




namespace py = pybind11;

// Allow pass-by-reference on stl containers:
PYBIND11_MAKE_OPAQUE(std::vector<int>)


PYBIND11_MODULE(Cxx_PythonFunction_variants, m) {

	/* - The Pybind11_Module is a macro which creates a function that will be called when an "import" statement is issied from Python. 
	   - The argument is the file name, what you which to define the library name in Python. 
	   - m is a variable of type py::module which is the main interface for creating bindings. 
	*/


	// Information about dynamic library as a whole (called with print(Cxx_PythonFunctions_variants.__doc__))
	m.doc() = "C++ Function variants of Python";

	// Construct psuodo stl classes to interface stl containers between python and C++ by reference. 
	py::bind_vector<std::vector<int>>(m, "VectorInt");

	/* ---------------------------------- Define functions to interface ------------------------------ */
	/* Note: 
	-  To define a function to Python: 
		-  m.def("FnNameForPython", &FnNameInC++, R*pbdoc()) where &FnNameinC++ is the memory address of the function.
		-  R"pbdoc() sets the Cxx_PythonFunction_variants.FnName.__doc__ information. Using this to set the function description
		   AND equivalent python code it is tested against.
	*/


	// Selective sort function python interface
	// Using std::vector by reference (no return value policy specification needed as by refernece)
	m.def("selective_sort", &selective_sort, R"pbdoc(
	
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
	)pbdoc");


	// Using pybind11::list, i.e., python lists by reference.  
	m.def("selective_sort_pylist", &selective_sort_pylist, R"pbdoc(
	
	---- Selective sort algorithm for ordering data minimum to maximum using a Python List by reference ----

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
	)pbdoc");


	// Using pybind11::array_t, i.e., numpy array by reference
	m.def("selective_sort_numpyarr", &selective_sort_numpyarr, R"pbdoc(
	
	---- Selective sort algorithm for ordering data minimum to maximum using a Numpy array by reference ----

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
	)pbdoc");

#ifdef VERSION_INFO
	m.attr("__version__") = VERSION_INFO;
#else
	m.attr("__version__") = "dev";
#endif
}

