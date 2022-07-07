#import library
import pandas as pd

#load csv
cid = pd.DataFrame(pd.read_csv(r"C:\Users\JackF\Documents\dev\csv_gen\src\cid.csv"))
iab = pd.DataFrame(pd.read_csv(r"C:\Users\JackF\Documents\dev\csv_gen\src\iab.csv"))
mam = pd.DataFrame(pd.read_csv(r"C:\Users\JackF\Documents\dev\csv_gen\src\mam.csv"))
oui = pd.DataFrame(pd.read_csv(r"C:\Users\JackF\Documents\dev\csv_gen\src\oui.csv"))
oui36 = pd.DataFrame(pd.read_csv(r"C:\Users\JackF\Documents\dev\csv_gen\src\oui36.csv"))

#build datarame list
frames = [cid, iab, mam, oui, oui36]

#concat datarames
result = pd.concat(frames)

for i in result["Assignment"]:
    i[3].append(':')
    print(i)



#save to csv
#result.to_csv("mac_decoded.csv")
