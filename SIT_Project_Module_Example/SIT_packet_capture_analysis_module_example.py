#!/usr/bin/env python
#Usage           :python SIT_packet_capture_analysis_module_example.py <pcap_file> 
#description     :Module used to display the entire protocol list and heirarchy within the PCAP along with plotting packet size graph. The filter used for the same is "-qz io,phs". Output file generated is Protocol_Hierarchy.html
#date            :20200616
#version         :0.1
#notes           :
#python_version  :3.7.3
#==============================================================================

import sys
import logging
import subprocess
import pyshark
from datetime import datetime
from flask import Flask, request, redirect, url_for
from pygal import XY
from pygal.style import LightGreenStyle

logging.getLogger().setLevel(logging.DEBUG)
logger = logging.getLogger(__name__)


def task(filename):
    filters = '-qz io,phs'
    logger.info('Subprocess Call started')
    Out = subprocess.Popen(['tshark', '-nr', filename, '-qz','io,phs'], 
                stdout=subprocess.PIPE, 
                stderr=subprocess.STDOUT)
    stdout,stderr = Out.communicate()
    stdout = stdout.decode('utf-8')
    stdout = stdout.replace('=','')
    #print(stdout)
    return stdout


def plot(filename):
    pkt_sizes = []
    cap = pyshark.FileCapture(filename, only_summaries=True)
    for packet in cap:
        # Create a plot point where (x=time, y=bytes)
        pkt_sizes.append((float(packet.time), int(packet.length)))
    # Create pygal instance
    pkt_size_chart = XY(width=400, height=300, style=LightGreenStyle, explicit_size=True)
    pkt_size_chart.title = 'Packet Sizes'
    # Add points to chart and render chart html
    pkt_size_chart.add('Size', pkt_sizes)
    chart = pkt_size_chart.render()
    print(chart)
    html = """{}""".format(chart)
    return html 

def main():
	
    if len(sys.argv) != 2:
    	logger.error('Insufficient arguments')
    	print("Usage: <script_name>.py <pcap_file>")
    	sys.exit(1)

    filename = sys.argv[1]
    op = task(filename)
    op2 = plot(filename)
    htmlFile = open('Protocol_Hierarchy.html', 'w')
    htmlFile.write('<pre>')
    htmlFile.write(op)
    htmlFile.write(op2)
    htmlFile.write('/<pre>')


if __name__=="__main__":
    main()