#!/usr/bin/env python

from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSController
from mininet.node import RemoteController
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI

import sys
import json
from pprint import pprint

'''
Topology Generator
'''
class TopoGen(Topo):
    def __init__(self, topojson):
        # Initialize topology
        Topo.__init__(self)
        
        # Store hosts, switches, and links from JSON
        hostsList = topojson['hosts']
        switchesList = topojson['switches']
        linksList = topojson['links']

        # Add switches to a topology
        switches = []
        for i in range(len(switchesList)):
            switches.append(self.addSwitch(switchesList[i]))
        
        # Add hosts to a topology
        hosts = []
        for i in range(len(hostsList)):
            hosts.append(self.addHost(hostsList[i]))

        # Add links to a topology
        for i in range(len(linksList)):
            self.addLink(
                linksList[i]['link'][0],
                linksList[i]['link'][1],
                bw = linksList[i]['bw'],
                delay = linksList[i]['delay'],
                loss = linksList[i]['loss'])

'''
Create and test a simple network
'''
def simpleTest(topojson):
    topo = TopoGen(topojson = topojson)
    
    # Create and manage a network with OvS controller and use TCLink
    net = Mininet(
        topo = topo,
        controller = OVSController,
        link = TCLink)

    # Start a network
    net.start()
    
    # Dump connections to/from a set of nodes
    print("Dumping host connections")
    dumpNodeConnections(net.hosts)
    dumpNodeConnections(net.switches)

    # Open Mininet CLI
    CLI(net)

    # Stop a network
    #net.stop()

'''
Read topology in JSON file
'''
def readTopo(filename):
    topo = ''
    with open(filename) as file:
        topo = json.load(file)
    return topo

'''
Main (entry point)
'''
if __name__ == '__main__':
    # Error handling of input arguments
    if (len(sys.argv) == 2 and sys.argv[0] == './topoGen.py') or (len(sys.argv) == 3 and sys.argv[0] == 'python' and sys.argv[1] == 'topoGen.py'):
        # Read the topology form the input file
        if len(sys.argv) == 2:
            topojson = readTopo('./input/' + sys.argv[1])
        else:
            topojson = readTopo('./input/' + sys.argv[2])
    else:
        # The format of command is wrong and exit the program
        print('[ERROR] The format of command is WRONG')
        print('[INFO] sudo ./topoGen.py filename.json')
        print('[INFO] sudo python topoGen.py filename.json')
        sys.exit(0)

    # Tell mininet to print useful information
    setLogLevel('info')

    # Generate the network topology in Mininet
    simpleTest(topojson)