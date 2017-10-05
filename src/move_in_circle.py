#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

PI = 3.1415926535897

def move_circle():
	pub = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size = 10)
	rospy.init_node('Robot_cleaner',anonymous = True)
	vel_msg = Twist()

	print "Move the robot! :"
	radius = input("Enter Radius:")
	speed = input("Enter Speed :")
	print radius

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


# def set_desired_position(speed,radius):	
# 	# Move Robot to starting position	

# 	vel_msg.linear.x = speed
# 	vel_msg.linear.y = 0
# 	vel_msg.linear.z = 0
# 	vel_msg.angular.x = 0
# 	vel_msg.angular.y = 0
# 	vel_msg.angular.z = 0

# 	t0 = rospy.Time.now().to_sec()
# 	distance_travelled = 0

# 	while distance_travelled < radius:
# 		pub.publish(vel_msg)
# 		t1 = rospy.Time.now().to_sec()
# 		distance_travelled = speed*(t1-t0)

# 	vel_msg.linear.x = 0
# 	pub.publish(vel_msg)

# def set_desired_orientation(speed):
# 	angular_speed = speed/radius*PI/180
# 	vel_msg.linear.x = 0
# 	vel_msg.angular.z = angular_speed
#   	t0 = rospy.Time.now().to_sec()
# 	angle_travelled = 0

# 	while ( angle_travelled < PI/2.0 ):
# 		pub.publish(vel_msg)
# 		t1 = rospy.Time.now().to_sec()
# 		angle_travelled = angular_speed*(t1-t0)

# 	vel_msg.linear.z = 0
# 	pub.publish(vel_msg)	

if __name__ == '__main__':
	try:
		move_circle()
	except rospy.ROSInterruptException:
		pass
