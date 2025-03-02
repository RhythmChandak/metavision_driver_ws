from setuptools import find_packages, setup

package_name = 'event_cam_subscriber'

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
    maintainer='pi',
    maintainer_email='rhythm@seas.upenn.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'event_cam_subscriber = event_cam_subscriber.subscriber_node:main',
            'evfly_interface = event_cam_subscriber.evfly_interface:main',
        ],
    },
)
