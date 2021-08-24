#subscriber
#! /usr/bin/python

import rospy
from std_msgs.msg import Int64

def call(msg):
	print(msg.data)

def subscriber():
	rospy.init_node("subscriber")
	rospy.Subscriber("hello", Int64,call)
	rospy.spin()

if __name__=="__main__":

  subscriber()