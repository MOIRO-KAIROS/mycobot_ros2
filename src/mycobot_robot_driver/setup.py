from setuptools import find_packages, setup

package_name = 'mycobot_robot_driver'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='godssi',
    maintainer_email='godssi@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sync_play = mycobot_robot_driver.sync_play:main',
            'listen_real = mycobot_robot_driver.listen_real:main',
            'follow_display = mycobot_robot_driver.follow_display:main'
        ],
    },
)
