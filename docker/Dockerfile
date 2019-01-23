# Download base image from yungshenglu/ubuntu-env:16.04
FROM yungshenglu/ubuntu-env:16.04

# Update software repository
RUN apt-get update

# Install software repository
RUN apt-get install -y tcpdump sudo

# Use argument to assign passwd to create image
RUN echo 'root:cn2018' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

# Set the envionment variables
ENV NOTVISIBLE "in users profile"
ENV LC_ALL C
RUN echo "export VISIBLE=now" >> /etc/profile

# Set the container listens on the specified ports at runtime
EXPOSE 22

# Set the entrypoint
CMD ["/usr/sbin/sshd", "-D"]

# Install Mininet and Open vSwitch controller
#RUN apt-get install -y mininet openvswitch-testcontroller
#RUN cp /usr/bin/ovs-testcontroller /usr/bin/ovs-controller
#RUN service openvswitch-switch start
RUN git clone git://github.com/mininet/mininet
WORKDIR /mininet/
RUN ./util/install.sh -a

# Clone the repository from GitHub
#RUN git clone https://github.com/yungshenglu/Network_Topology.git /root/Network_Topology/