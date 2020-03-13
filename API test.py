import requests
import time

payLoad = "https://blast.ncbi.nlm.nih.gov/Blast.cgi?" \
          "QUERY=NM_014229.3" \
          "&DATABASE=nt" \
          "&PROGRAM=blastn" \
          "&CMD=Put"
res = requests.get(payLoad)

#print(res)
content = res.text

print(content)

toFind = "RID = "
start = content.find(toFind)+len(toFind)
end = content.find("\n", start)
RID = content[start:end]
#print("RID ist "+RID)

toFind = "RTOE = "
start = content.find(toFind)+len(toFind)
end = content.find("\n", start)
RTOE = int(content[start:end])
#print("RTOE ist "+str(RTOE))

factor = 10
time.sleep(factor*(RTOE/1000))

payLoad2 = "https://blast.ncbi.nlm.nih.gov/Blast.cgi?" \
          "RID="+RID+"" \
          "&CMD=Get"
res2 = requests.get(payLoad2)
content2 = res2.text

print(content2)

toFind = "Status="
start = content2.find(toFind)+len(toFind)
end = content2.find("\n", start)
blastStatus = content2[start:end]

print("RID ist "+RID)
print("RID ist "+str(RTOE))
print("Status ist "+blastStatus)