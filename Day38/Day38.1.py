#! /usr/bin/python

import rospy
from std_msgs.msg import String
from insta.msg import learnros


def talker():
    pub = rospy.Publisher('custom_chatter', learnros, queue_size=10)
    rospy.init_node('custom_talker', anonymous=True)
    r = rospy.Rate(1)
    rospy.loginfo("Publisher node started, now publishing message")

    while not rospy.is_shutdown():
        msg = learnros()
        msg.message = "done with day one"
        msg.name = "ROS User"
        pub.publish(msg)
        r.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass