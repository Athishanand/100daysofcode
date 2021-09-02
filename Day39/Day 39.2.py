#! /usr/bin/python

import rospy
from std_msgs.msg import String
from rmp08.msg import dennis

def callback(data):
    rospy.loginfo("%s X: %f Y: %f",data.message,data.x,data.y)


def listen():
    rospy.init_node("subscriber",anonymous=True)
    rospy.Subscriber("talking",dennis,callback)
    rospy.spin()

if __name__ == "__main__":
    try:
        listen()
    except rospy.ROSInterruptException:
        pass