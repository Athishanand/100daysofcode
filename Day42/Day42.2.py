<launch>
  <param command="$(find xacro)/xacro $(find rover_description)/urdf/rover.xacro" name="robot_description"/>
  <node args="-param robot_description -urdf -model ircrover" name="spawn_urdf" pkg="gazebo_ros" type="spawn_model"/>
  <include file="$(find gazebo_ros)/launch/empty_world.launch">
    <arg name="world_name" value="$(find rover_description)/world/square.world"/>
    <arg name="paused" value="false"/>
    <arg name="use_sim_time" value="true"/>
    <arg name="gui" value="true"/>
    <arg name="headless" value="false"/>
    <arg name="debug" value="false"/>
  </include>
</launch>
