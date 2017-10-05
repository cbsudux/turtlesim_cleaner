#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

PI = 3.1415926535897

def move():
	pub = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size = 10)
	rospy.init_node('Robot_cleaner',anonymous = True)
	vel_msg = Twist()

	print "Move the robot! :"
	speed = input("Enter angular velocity :")
	angle_deg = input("Enter angle :")
	direction = input("Clockwise? :")


	angle_rad = angle_deg*2*PI/360
	angular_speed = speed*2*PI/360

	if(direction):
		vel_msg.angular.z = -abs(angular_speed)

	else:
		vel_msg.linear.z = abs(angular_speed)

	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	
  	t0 = rospy.Time.now().to_sec()

	angle_travelled = 0

	while ( angle_travelled < angle_rad ):
		pub.publish(vel_msg)
		t1 = rospy.Time.now().to_sec()
		angle_travelled = angular_speed*(t1-t0)

	vel_msg.linear.z = 0
	pub.publish(vel_msg)	

if __name__ == '__main__':
	try:
		move()
	except rospy.ROSInterruptException:
		pass
