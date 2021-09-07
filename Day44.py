import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math
import tf
import time
from std_srvs.srv import Empty


def callback(odom_msg):
    print("POSITION")
    print()
    print("px=", odom_msg.pose.pose.position.x)
    print()
    print("py=", odom_msg.pose.pose.position.y)
    print()
    print("VELOCITY")
    print("vx=", odom_msg.twist.twist.linear.x)
    print()
    print("vy=", odom_msg.twist.twist.angular.y)
    print()
    print("ORIENTATION")
    print("x=", odom_msg.pose.pose.orientation.x)
    print()
    print("y=", odom_msg.pose.pose.orientation.y)
    print()
    print("z=", odom_msg.pose.pose.orientation.z)
    print()
    print("w=", odom_msg.pose.pose.orientation.w)


if __name__ == "__main__":

    try:
        rospy.init_node("position_data", anonymous=True)
        position_topic = '/odom'
        subcriber = rospy.Subscriber(position_topic, Odometry, callback)
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo()