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

def plot(filename):
    pkt_arr = []
    cap = pyshark.FileCapture(filename, only_summaries=True)
    
    pkt_arr.append((1, 66))
    print(cap)
    for packet in cap:
        # Create a plot point where (x=protocol, y=bytes)
        pkt_arr.append((int(packet.no), int(packet.length)))

    print(pkt_arr)

    # Create pygal instance
    pkt_size_chart = XY(width=600, height=400, style=LightGreenStyle, explicit_size=True)
    pkt_size_chart.title = 'Packets Analysis'
    # Add points to chart and render chart html
    pkt_size_chart.add('Size v/s No', pkt_arr)
    #pkt_size_chart.add('Packet Length', pkt_sizes)       to add more graphs on same chart
    chart = pkt_size_chart.render()
    #print(chart)
    html = """{}""".format(chart)
    return html 

def main():
	
    if len(sys.argv) != 2:
    	logger.error('Insufficient arguments')
    	print("Usage: <script_name>.py <pcap_file>")
    	sys.exit(1)

    filename = sys.argv[1]
    op2 = plot(filename)
    htmlFile = open('output.html', 'w')
    htmlFile.write('<pre>')
    htmlFile.write(op2)
    htmlFile.write('</pre>')


if __name__=="__main__":
    main()
