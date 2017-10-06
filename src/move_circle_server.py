#!/usr/bin/env python

import rospy
from turtlesim_cleaner.srv import *
from geometry_msgs.msg import Twist

PI = 3.1415926535897

def handle_move_circle(req):
	pub = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size = 10)
	vel_msg = Twist()
	speed = req.s
	radius = req.r

	print "Your wish is my command"
	print "If you want to quit and watch me draw squares, Ctl-c me"


	vel_msg.linear.x = speed
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = speed/radius
	
	#Move Robot in circle
	while not rospy.is_shutdown():
		pub.publish(vel_msg)
	
	vel_msg.linear.x = 0	
	vel_msg.linear.z = 0
	pub.publish(vel_msg)	

def move_circle_server():
	rospy.init_node('move_circle_server')
	s = rospy.Service( 'move_circle', MoveCircle, handle_move_circle )
	rospy.spin()

if __name__ == "__main__":
	move_circle_server()

