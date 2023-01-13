#!/usr/bin/env python3
import rospy
import getch
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


'''
initialise is the function for controlling the keyboard 
with a publisher to control the turtle using the keyboard using the arrow keys
'''


def initialise():
	rospy.init_node('turtle_teleoperation', anonymous=False) # init node here
	pub=rospy.Publisher('/rover/base_controller/cmd_vel', Twist, queue_size=10) # init publisher here
	rate=rospy.Rate(50)
	move_message = Twist()
	while not rospy.is_shutdown():
		key = ord(getch.getch())
		if key==65:
			rospy.loginfo("Up key pressed")
			move_message.linear.x = 1.0
			move_message.angular.z = 0.0
			pub.publish(move_message)
		# move turtle forward here
		elif key==66:
			rospy.loginfo("Down key pressed")
			move_message.linear.x = -1.0
			move_message.angular.z = 0.0
			pub.publish(move_message)
		# move turtle backwards here
		elif key==67:
			move_message.linear.x = 0.0
			move_message.angular.z = -1.0
			pub.publish(move_message)
			rospy.loginfo("left key pressed")
		#move turtle left here

		elif key==68:
			rospy.loginfo("right key pressed")
			move_message.linear.x = 0.0
			move_message.angular.z = 1.0
			pub.publish(move_message)
		#move turtle right here

		rate.sleep()

if __name__ == '__main__':
	initialise()
