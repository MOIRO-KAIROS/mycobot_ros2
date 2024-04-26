import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, Command, PathJoinSubstitution

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
import yaml

def generate_launch_description():
    # Launch configuration variables specific to simulation
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    urdf_file_name = 'mycobot.urdf.xacro'
    urdf = os.path.join(get_package_share_directory('mycobot_description'), 'urdf', urdf_file_name)
    srdf = os.path.join(get_package_share_directory('mycobot_moveit'), 'config', 'mycobot.srdf.xacro')
   

    # Launch configuration variables specific to MoveIt
    kinematics_parma = PathJoinSubstitution([FindPackageShare('mycobot_moveit'), 'config', 'kinematics.yaml'])
    moveit_controllers_yaml = PathJoinSubstitution([FindPackageShare('mycobot_moveit'), 'config', 'controllers.yaml'])
    joint_limits_parm = PathJoinSubstitution([FindPackageShare('mycobot_moveit'), 'config', 'joint_limits.yaml'])
    ompl_planning_pipeline_config = os.path.join(get_package_share_directory('mycobot_moveit'), 'config', 'ompl_planning_pipeline.yaml')

    # Robot description From Xacro
    robot_description_content = Command(
        PathJoinSubstitution([FindExecutable(name="xacro")]),
        " ",
        urdf
    )

    # RViz
    rviz_config_file = os.path.join(get_package_share_directory('mycobot_moveit'), 'config', 'mycobot.rviz')

    # Declare the launch arguments
    declare_use_sim_time_argument = DeclareLaunchArgument(
        'use_sim_time',
        default_value='true',
        description='Use simulation (Gazebo) clock if true')

    # Publish the URDF to the parameter server
    publish_mycobot_description = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'use_sim_time': use_sim_time}, {'robot_description': robot_description_content}]),

    
