/*
* test_file.cpp
* Purpose: Testing game development code
* Last Modified: 8/13/2017
* Modified By: Andrew Roberts
*/

#include "Point.h"

Vector operator-(Point a, Point b); 
float dot_product(const Vector& a, const Vector& b); 

int main() {
	
	Point p1(5, 5); 
	Vector v; 
	v.x = 10; 
	v.y = -2; 

	/*
	cout << "Initial position: (" << p1.get_x_pos() << ", " << p1.get_y_pos() << ")" << endl; 
	cout << "Vector change: (" << v.x << ", " << v.y << ")" << endl; 
	cout << "Vector length: " << v.length() << endl; 

	Point p2 = p1.add_vector(v);
	cout << "New position: (" << p2.get_x_pos() << ", " << p2.get_y_pos() << ")" << endl; 
 	
	Vector v2 = p1 - p2;   
	cout << "Vector from b to a: (" << v2.x << ", " << v2.y << ")" << endl; 
	
	Vector v3 = v2*2; 
	cout << "Scaled vector by 2: (" << v3.x << ", " << v3.y << ")" << endl;  
	
	Vector v4 = v2/2; 
	cout << "Scaled vector by .5: (" << v4.x << ", " << v4.y << ")" << endl;  
	
	Vector v5 = v2.normalized(); 
	cout << "Normalized vector: (" << v5.x << ", " << v5.y << ")" << endl;  
	cout << "Length of normalized vector: " << v5.length() << endl; 
	*/

	Vector v1 = Vector(1, 1); 
	Vector v2 = Vector(4, 4);  
	Vector v3 = v1 + v2; 
	cout << v3.x << ", " << v3.y << endl;  
	cout << "Dot Product: " << dot_product(v1.normalized(), v2.normalized()) << endl; 
	
	return 0; 
}

/*
* Returns vector to get from b to a
*
*
*/
Vector operator-(Point a, Point b) {

	Vector v; 
	v.x = a.get_x_pos() - b.get_x_pos(); 
	v.y = a.get_y_pos() - b.get_y_pos(); 

	return v; 
}

float dot_product(const Vector& a, const Vector& b) {

	return (a.x * b.x) + (a.y * b.y); 

}
