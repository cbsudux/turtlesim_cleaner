#!/usr/bin/env python

import rospy
from turtlesim_cleaner.srv import *

def move_square_client():
	rospy.wait_for_service('move_square')
	try:
		side_length = input("Enter Side length (0-5) : ")
		rotations = input("Enter number of rotations : ")
		move_square = rospy.ServiceProxy('move_square', MoveSquare)
		move_square(side_length,rotations)

	except rospy.ServiceException, e:
		print "Service call failed: %s"%e

if __name__ == "__main__":
	move_square_client()