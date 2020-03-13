import requests
import time

payLoad = "https://blast.ncbi.nlm.nih.gov/Blast.cgi?" \
          "QUERY=NM_014229.3" \
          "&DATABASE=nt" \
          "&PROGRAM=blastn" \
          "&CMD=Put"
res = requests.get(payLoad)
content = res.text

toFind = "RID = "
start = content.find(toFind)+len(toFind)
end = content.find("\n", start)
RID = content[start:end]
print("RID ist "+RID)

toFind = "RTOE = "
start = content.find(toFind)+len(toFind)
end = content.find("\n", start)
RTOE = int(content[start:end])
print("RTOE ist "+str(RTOE))

#TODO Der RTOE ist vermutlich in Minuten zu verstehen und nicht in Sekunden (obwohl es so auf der Blast API Seite steht - bei Mathworks gibt es eine Info, die auf Minuten schließen lässt)
time.sleep(RTOE)
while 1:
    time.sleep(5)

    payLoad2 = "https://blast.ncbi.nlm.nih.gov/Blast.cgi?" \
               "FORMAT_OBJECT = SearchInfo" \
               "&RID="+RID+\
               "&CMD=Get"
    res2 = requests.get(payLoad2)
    content2 = res2.text

    toFind = "Status="
    start = content2.find(toFind)+len(toFind)
    end = content2.find("\n", start)
    blastStatus = content2[start:end]

    print("RID "+RID+" hat folgenden Status: "+blastStatus)
