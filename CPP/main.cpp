/*
* main.cpp
* Purpose: Main game loop
* Last Modified: 8/14/2017
* Modified By: Andrew Roberts
*/

#include "Point.h"

int main() {

	p1_pos = Point(0, 0);
	p1_vel = Vector(2, 2);
	p1_grav = Vector(0, -2); 
  
	float prev_time = 0; 
	float curr_time = get_current_time(); 

	while(true) {
		prev_time = curr_time; 
		curr_time = get_curr_time();

		float dt = curr_time - prev_time; 
		
		if(dt > .15f)
			dt = .15f

		update(dt); 
		draw(); 
	}
}
