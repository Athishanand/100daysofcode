#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

x = 0
y = 0
yaw = 0


def callback(msg):
    global x
    global y, yaw
    x = msg.x
    y = msg.y
    yaw = msg.theta


def rotating():
    velocity_msgs = Twist()
    rospy.init_node('turtlesim_node', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    print("GIVE YOUR INPUT")
    angular_speed_degree = float(10.0)
    relative_degree = float(1.1)
    clockwise = (True)

    angular_speed = math.radians(abs(angular_speed_degree))

    if (clockwise):
        velocity_msgs.angular.z = -abs(angular_speed)
    else:
        velocity_msgs.angular.z = abs(angular_speed)
    loop_rate = rospy.Rate(1)
    t0 = rospy.Time.now().to_sec()
    while True:
        rospy.loginfo("TURTLE IS ROTATING")
        velocity_publisher.publish(velocity_msgs)
        t1 = rospy.Time.now().to_sec()
        current_degree = angular_speed * (t1 - t0)
        loop_rate.sleep()

        print(current_degree)
        if current_degree > relative_degree:
            rospy.loginfo("REACHED")
            break
    velocity_msgs.angular.z = 0
    velocity_publisher.publish(velocity_msgs)


def moving_straight():
    rospy.init_node('turtlesim_node', anonymous=True)
    vel_msg = Twist()
    vel_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    a = x
    b = y
    speed = float(1)
    distance = float(4)
    forward = (True)

    if forward:
        vel_msg.linear.x = abs(speed)
    else:
        vel_msg.linear.x = -abs(speed)

    distance_moved = 0.0
    rate = rospy.Rate(1)
    while True:
        rospy.loginfo("TURTLE MOVING")
        vel_publisher.publish(vel_msg)
        distance_moved = abs(math.sqrt((x - a) ** 2) + ((y - b) ** 2))
        print(distance_moved)
        print(x, y)
        if distance_moved > distance:
            rospy.loginfo("REACHED")
            break
    vel_msg.linear.x = 0
    vel_publisher.publish(vel_msg)


def rotating1():
    velocity_msgs = Twist()
    rospy.init_node('turtlesim_node', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    print("GIVE YOUR INPUT")
    angular_speed_degree = float(10.0)
    relative_degree = float(1.8)
    clockwise = (True)

    angular_speed = math.radians(abs(angular_speed_degree))

    if (clockwise):
        velocity_msgs.angular.z = -abs(angular_speed)
    else:
        velocity_msgs.angular.z = abs(angular_speed)
    loop_rate = rospy.Rate(1)
    t0 = rospy.Time.now().to_sec()
    while True:
        rospy.loginfo("TURTLE IS ROTATING")
        velocity_publisher.publish(velocity_msgs)
        t1 = rospy.Time.now().to_sec()
        current_degree = angular_speed * (t1 - t0)
        loop_rate.sleep()

        print(current_degree)
        if current_degree > relative_degree:
            rospy.loginfo("REACHED")
            break
    velocity_msgs.angular.z = 0
    velocity_publisher.publish(velocity_msgs)


def moving_straight1():
    rospy.init_node('turtlesim_node', anonymous=True)
    vel_msg = Twist()
    vel_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    a = x
    b = y
    speed = float(1)
    distance = float(1.5)
    forward = (True)

    if forward:
        vel_msg.linear.x = abs(speed)
    else:
        vel_msg.linear.x = -abs(speed)

    distance_moved = 0.0
    rate = rospy.Rate(1)
    while True:
        rospy.loginfo("TURTLE MOVING")
        vel_publisher.publish(vel_msg)
        distance_moved = abs(math.sqrt((x - a) ** 2) + ((y - b) ** 2))
        print(distance_moved)
        print(x, y)
        if distance_moved > distance:
            rospy.loginfo("REACHED")
            break
    vel_msg.linear.x = 0
    vel_publisher.publish(vel_msg)


def rotating2():
    velocity_msgs = Twist()
    rospy.init_node('turtlesim_node', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    print("GIVE YOUR INPUT")
    angular_speed_degree = float(10.0)
    relative_degree = float(1.6)
    clockwise = (True)

    angular_speed = math.radians(abs(angular_speed_degree))

    if (clockwise):
        velocity_msgs.angular.z = -abs(angular_speed)
    else:
        velocity_msgs.angular.z = abs(angular_speed)
    loop_rate = rospy.Rate(1)
    t0 = rospy.Time.now().to_sec()
    while True:
        rospy.loginfo("TURTLE IS ROTATING")
        velocity_publisher.publish(velocity_msgs)
        t1 = rospy.Time.now().to_sec()
        current_degree = angular_speed * (t1 - t0)
        loop_rate.sleep()

        print(current_degree)
        if current_degree > relative_degree:
            rospy.loginfo("REACHED")
            break
    velocity_msgs.angular.z = 0
    velocity_publisher.publish(velocity_msgs)


def moving_straight2():
    rospy.init_node('turtlesim_node', anonymous=True)
    vel_msg = Twist()
    vel_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    a = x
    b = y
    speed = float(1)
    distance = float(4)
    forward = (True)

    if forward:
        vel_msg.linear.x = abs(speed)
    else:
        vel_msg.linear.x = -abs(speed)

    distance_moved = 0.0
    rate = rospy.Rate(1)
    while True:
        rospy.loginfo("TURTLE MOVING")
        vel_publisher.publish(vel_msg)
        distance_moved = abs(math.sqrt((x - a) ** 2) + ((y - b) ** 2))
        print(distance_moved)
        print(x, y)
        if distance_moved > distance:
            rospy.loginfo("REACHED")
            break
    vel_msg.linear.x = 0
    vel_publisher.publish(vel_msg)


if __name__ == "__main__":
    try:
        position_topic = '/turtle1/pose'
        rospy.Subscriber(position_topic, Pose, callback)
        rotating()
        moving_straight()
        rotating1()
        moving_straight1()
        rotating2()
        moving_straight2()

    except rospy.ROSInterruptException:
        print("STOPPED")