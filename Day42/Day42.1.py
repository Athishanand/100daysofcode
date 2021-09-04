#! /usr/bin/python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist


def shapes():
    rospy.init_node('shapes', anonymous=True)
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)
    m = Twist()
    rate.sleep()

    for i in range(3):
        # front
        m.linear.x = 2.4
        m.angular.z = 1.4
        rospy.loginfo(m)
        pub.publish(m)
        rate.sleep()


if __name__ == '__main__':
    shapes()