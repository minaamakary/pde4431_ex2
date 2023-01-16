#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import turtlesim.srv

'''
Line 11 - 25 (Spawning 4 turtles for cleaning the world)
'''
rospy.wait_for_service('spawn')
spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
spawner(1,1,0,"turtle2")

rospy.wait_for_service('spawn')
spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
spawner(1,8,0,"turtle3")

rospy.wait_for_service('spawn')
spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
spawner(7,2,0,"turtle4")

rospy.wait_for_service('spawn')
spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
spawner(1,3,0,"turtle5")

def callback5(data): #for 5th turtle
	#TURTLE 5
	pub=rospy.Publisher('/turtle5/cmd_vel', Twist, queue_size=10) # init publisher here
	rate=rospy.Rate(80)
	move_message = Twist()
	rospy.loginfo("x = %f" % data.x)
	rospy.loginfo("y =  %f" % data.y )
	move_message.linear.x = 0.4

	if data.x < 1 or data.x > 10.0:
		rospy.loginfo("hittng the wall")
		move_message.linear.x = 0.4
		move_message.angular.z = 0.8
		pub.publish(move_message)
		#turtle.kill()

	if data.y < 1 or data.y > 10.0:
		rospy.loginfo("hittng the wall")
		move_message.linear.x = 0.4
		move_message.angular.z = 0.8
		pub.publish(move_message)
	
	pub.publish(move_message)




def callback(data):
	pub=rospy.Publisher('/rover/base_controller/cmd_vel', Twist, queue_size=10) # init publisher here
	rate=rospy.Rate(50)
	move_message = Twist()
	rospy.loginfo("x = %f" % data.x)
	rospy.loginfo("y =  %f" % data.y )
	move_message.linear.x = 0.4

	if data.x < 1 or data.x > 10.0:
		rospy.loginfo("hittng the wall")
		move_message.linear.x = 0.4
		move_message.angular.z = 0.8
		pub.publish(move_message)
		#turtle.kill()

	if data.y < 1 or data.y > 10.0:
		rospy.loginfo("hittng the wall")
		move_message.linear.x = 0.4
		move_message.angular.z = 0.8
		pub.publish(move_message)
	
	pub.publish(move_message)

'''
readTurtlemovement is the function that initialises the node automove - with all the turtles
subscribing to pose to get location !!!
'''

def readTurtlemovement():
	
	rospy.init_node('turtle_automove', anonymous=True)
	rospy.Subscriber("/turtle1/pose", Pose, callback)	
		
if __name__ == '__main__':
	readTurtlemovement()
	
