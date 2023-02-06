#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan 
from geometry_msgs.msg import Twist
def callback(msg):


	print (msg.ranges [360])
	#move.linear.x = 0.1


	if msg.ranges [360] < 1:
		move.linear.x = 0
		pub.publish(move) 
	
	if msg.ranges [360] > 1:
		move.linear.x = 0.1
		pub.publish(move) 
			
	
rospy. init_node('check_obstacle')

sub = rospy.Subscriber('/scan', LaserScan, callback)
pub = rospy.Publisher('/rover/base_controller/cmd_vel', Twist, queue_size=10)

move = Twist()

rospy.spin()

