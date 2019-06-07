# --------------
import json
from collections import Counter
with open(path) as f:
       data = json.load(f)

 #print(data) 
 
# Code starts here

#  Can you find how many deliveries were faced by batsman  `SC Ganguly`.
ballCount=0
for deliveries in data['innings'][0]['1st innings']['deliveries']:
    if deliveries[list(deliveries.keys())[0]]['batsman']== "SC Ganguly":
       ballCount+=1
print(ballCount)
    


#  Who was man of the match and how many runs did he scored ?
Man_of_the_Match= data['info']['player_of_match'][0]
print(Man_of_the_Match)
runsScored=0
FirstInnDel=data['innings'][0]['1st innings']['deliveries']
#FirstInnDel
for Bren in FirstInnDel:
    #print(Bren)
   # print('**'*30)
    for key, val in Bren.items():
       # print('keys=',key,'Values=', val)
        if val['batsman']==data['info']['player_of_match'][0]:
            #print(key,'Value= ',val['runs']['batsman'])
            runsScored=runsScored+val['runs']['batsman']
print("Man of the match was ",Man_of_the_Match, 'and the number of runs scored were ',runsScored )


#  Which batsman played in the first inning?
L1=[]
FirstInnDel=data['innings'][0]['1st innings']['deliveries']
#print(FirstInnDel)
for batsmanVal in FirstInnDel:
   # print(batsmanVal)
    #print("**"*20)
    for key, val in batsmanVal.items():
       # print( "Values ", val['batsman'])
        if val['batsman'] not in L1:
            L1.append(val['batsman'])
print(L1)

# Which batsman had the most no. of sixes in first inning ?
Dictionary1={}
for rec in FirstInnDel:
   # print(rec)
   # print("@@"*20)
    for key,val in rec.items():
       # print(key,val['runs']['batsman'])
        if val['runs']['batsman']==6:
           # print(key,val)
            if val['batsman'] in Dictionary1:
                Dictionary1[val['batsman']]+=1
                #print(Dictionary1)
            else:
                Dictionary1[val['batsman']]=1
               # print(Dictionary1)
print(Dictionary1)


# Find the names of all players that got bowled out in the second innings.
SecondInnDel=data['innings'][1]['2nd innings']['deliveries']
L3=[]
for rec in SecondInnDel:
    #print(rec)
   # print("@@"*20)
    for key,val in rec.items():
       # print(key,val)
        if 'wicket'in val and val['wicket']['kind']=='bowled':
           # print(key, val)
            #print('##'*20)
            L3.append(val['batsman'])
print(L3)


# How many more "extras" (wides, legbyes, etc) were bowled in the second innings as compared to the first inning?
SecondInnExtras=0
for rec in SecondInnDel:
    for key,val in rec.items():
       # print(key,val)
        if val.get('extras'):
            SecondInnExtras+=1
#print(SecondInnExtras)
FirstInnDel=data['innings'][0]['1st innings']['deliveries']
FirstInnExtras=0
for rec in FirstInnDel:
    for key,val in rec.items():
        #print(key,val)
        if val.get('extras'):
            FirstInnExtras+=1
#print(FirstInnExtras)
SecondInnExtras-FirstInnExtras
#

# Code ends here


