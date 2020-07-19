import sys
import logging
import subprocess
import pyshark

def plot(filename):
    cap = pyshark.FileCapture(filename, only_summaries=True)

    contentarr="<center><h1><u>Captured Packets</u></h1></center><br>"
    contentarr+="<b><center>Packet Summary</center></b><br><br>"
    contentarr+="<b>\tNo  Time\tSource IP\t\tDest. IP\t\t\tProtoc.\tLen  Port  Info<br><br></b>"

    print(cap)
    for packet in cap:
        # Create a plot point where (x=protocol, y=bytes)
        contentarr+="\t"+packet.summary_line+"<br><br>"

    html = contentarr
    return html 

def main():
	
    if len(sys.argv) != 2:
    	logger.error('Insufficient arguments')
    	print("Usage: <script_name>.py <pcap_file>")
    	sys.exit(1)

    filename = sys.argv[1]
    op2 = plot(filename)
    htmlFile = open('Simply_print_output.html', 'w')
    htmlFile.write('<pre>')
    htmlFile.write(op2)
    htmlFile.write('</pre>')


if __name__=="__main__":
    main()
