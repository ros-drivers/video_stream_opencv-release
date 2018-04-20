Name:           ros-lunar-video-stream-opencv
Version:        1.1.1
Release:        0%{?dist}
Summary:        ROS video_stream_opencv package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/video_stream_opencv
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-camera-info-manager
Requires:       ros-lunar-cv-bridge
Requires:       ros-lunar-image-transport
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-rospy
Requires:       ros-lunar-sensor-msgs
BuildRequires:  ros-lunar-camera-info-manager
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-cv-bridge
BuildRequires:  ros-lunar-image-transport
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-rospy
BuildRequires:  ros-lunar-sensor-msgs

%description
The video_stream_opencv package contains a node to publish a video stream (the
protocols that opencv supports are supported, including rtsp, webcams on
/dev/video and video files) in ROS image topics, it supports camera info and
basic image flipping (horizontal, vertical or both) capabilities, also adjusting
publishing rate.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Fri Apr 20 2018 Sammy Pfeiffer <Sammy.Pfeiffer@student.uts.edu.au> - 1.1.1-0
- Autogenerated by Bloom

* Fri Mar 23 2018 Sammy Pfeiffer <Sammy.Pfeiffer@student.uts.edu.au> - 1.1.0-0
- Autogenerated by Bloom

