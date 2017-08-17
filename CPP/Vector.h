/*
* Vector.h
* Purpose: Class definition of a class defining a vector to be used for character movement
* Last Modified: 8/13/2017
* Modified By: Andrew Roberts
*/

class Vector {
	public: 
		Vector() {} 
		Vector(float x, float y); 
		float length() const; 
		float length_sqr() const; 
		Vector operator*(float scale_factor) const;
		Vector operator/(float scale_factor) const;
		Vector operator+(const Vector& to_add) const;  
		Vector operator-(const Vector& to_subtract) const;  
		Vector normalized() const; 

		float x, y; 
};
