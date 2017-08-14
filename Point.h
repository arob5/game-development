/*
* Point.h
* Purpose: Class definitions allowing game characters to move
* Last Modified: 8/14/2017
* Modified By: Andrew Roberts
*/

#include<iostream>
#include "Vector.h"
using namespace std; 


class Point {
	public:
		Point(float x, float y); 
		void set_position(float x, float y); 
		float get_x_pos(); 
		float get_y_pos(); 
		Point add_vector(Vector v); 

	private: 
		float x, y; 
};


