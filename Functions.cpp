/* ==========================================================================
				Project: C++ function variants of Python
========================================================================== */

// Include Pybind11 for C++ -> Python interface
#include "pybind11/pybind11.h"
#include "pybind11/numpy.h"

// Include any external modules 
#include <iostream>

// Selective sort algorithm which uses C++ datatype std::vector.
void selective_sort(std::vector<int>& data, int NP) {

	int minval_index;
	int copy_element;

	// Advance down entire list 
	for (int i = 0; i < NP - 1; i++) {

		// Set the minimum value index is the first index for each iteration 
		minval_index = i;
		
		// Loop along data and find the smallest data value to sort to top of list (i+1 as)
		for (int j = i+1; j < NP; j++) {

			// Condition to see if the new element is the minimum 
			if (data[j] < data[minval_index]) {
				minval_index = j;
			}
		}

		// After establishing the minimum value index; swap the current (i) list position with established min value
		if (minval_index != i) {

			copy_element = data[i];
			data[i] = data[minval_index];
			data[minval_index] = copy_element;
		}
	}

}

// Selective sort algorithm which takes a Python list by reference.
void selective_sort_pylist(pybind11::list& data, int NP) {

	int minval_index;
	pybind11::handle copy_element;

	// Index recorder
	int i = 0;

	// Advance down entire list 
	for (auto data_item: data) {

		// Set the minimum value index is the first index for each iteration 
		minval_index = i;

		// Loop along data and find the smallest data value to sort to top of list (i+1 as)
		for (int j = i + 1; j < NP; j++) {

			// Condition to see if the new element is the minimum 
			if (data[j] < data[minval_index]) {
				minval_index = j;
			}
		}

		// After establishing the minimum value index; swap the current (i) list position with established min value
		if (minval_index != i) {

			copy_element = data_item;
			data[i] = data[minval_index];
			data[minval_index] = copy_element;
		}

		// Increment index
		i++;
	}
}

// Selective sort algorithm which uses Numpy arrays
void selective_sort_numpyarr(pybind11::array_t<int>& data, int NP) {

	int minval_index;
	int copy_element;

	// Advance down entire list 
	for (int i = 0; i < NP - 1; i++) {

		// Set the minimum value index is the first index for each iteration 
		minval_index = i;

		// Loop along data and find the smallest data value to sort to top of list (i+1 as)
		for (int j = i + 1; j < NP; j++) {

			// Condition to see if the new element is the minimum 
			if (data.at(j) < data.at(minval_index)) {
				minval_index = j;
			}
		}

		// After establishing the minimum value index; swap the current (i) list position with established min value
		if (minval_index != i) {

			copy_element = data.at(i);
			data.mutable_at(i) = data.at(minval_index);
			data.mutable_at(minval_index) = copy_element;
		}
	}

}


/* Pybind code must be declared after functions (position dependent)*/
#include "Pybind_interface.h"