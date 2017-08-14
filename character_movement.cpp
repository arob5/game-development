/*
* character_movement.cpp
* Purpose: Class implementations of classes relevent to character movement
* Last Modified: 8/13/2017
* Modified By: Andrew Roberts
*/

#include "character_movement.h" 

Point::Point(float x, float y) {
	this->x = x; 
	this->y = y; 
}

void Point::set_position(float x, float y) {
	this->x = x; 
	this->y = y; 
}

float Point::get_x_pos() {
	return x; 

}

float Point::get_y_pos() {
	return y; 

}

Point Point::add_vector(Vector v) {
	float new_x = x + v.x; 
	float new_y = y + v.y; 

	return Point(new_x, new_y); 
}

