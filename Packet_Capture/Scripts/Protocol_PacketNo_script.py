import pandas as pd
import matplotlib.pyplot as plot

df = pd.read_csv('project.csv')
protocolVsPacket = df.groupby("Protocol").Source.count()
print(protocolVsPacket)
p = protocolVsPacket.plot(kind="bar")
p.set_title("No of packets vs Protocol")
p.set_xlabel("Protocol")
p.set_ylabel("Number of Packets")
rects = p.patches
labels = list(protocolVsPacket)
for rect, label in zip(rects, labels):
    height = rect.get_height()
    p.text(rect.get_x() + rect.get_width() / 2, height + 5, label,
           ha='center', va='bottom')
plot.show()
