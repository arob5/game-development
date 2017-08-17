
/*
* Vector.cpp
* Purpose: Class implementation of a class defining a vector to be used for character movement
* Last Modified: 8/13/2017
* Modified By: Andrew Roberts
*/

#include "Vector.h" 
#include<cmath> 

Vector::Vector(float x, float y) {
	this->x = x; 
	this->y = y; 
}

float Vector::length() const {
	return sqrt(x*x + y*y); 
}

float Vector::length_sqr() const {
	return (x*x + y*y); 
}
		
Vector Vector::operator*(float s) const {
	return Vector(x*s, y*s); 
}

Vector Vector::operator/(float s) const {
	return Vector(x/s, y/s); 
}

Vector Vector::operator+(const Vector& v) const {

	return Vector(x + v.x, y + v.y); 

} 

Vector Vector::operator-(const Vector& v) const {

	return Vector(x - v.x, y-v.y); 

} 

Vector Vector::normalized() const{
	
	return (*this) / length(); 

}
