"""Sample Challenge models to use in the development environment.

These were intially designed to be used by the `script.reset_db` module."""

from ...models import Challenge
from datetime import datetime, timedelta

#date variables
num = 7
wks = []
wks.append(datetime.now())  #wk14 or wks[0] should be today's date
for i in range(1,15):      #wk1-13 or wks[1:13] should automatically be the previously created week's start date minus 7 days
    wks.append(wks[i-1] - timedelta(days=num))

wks.reverse() #now wks[0] = wk0 (the farthest date from today) and wks[14] = wk14 (today's date)

# we challenges
# filler challenges
models = []
for i in range(11):                                 #for each week in wks[0:10]
    models.append(Challenge(id=i,                       #makes a new Challenge objs w id = i
            posts=[],
            noun="fairy",
            verb="swims",
            adj="",
            emotion="happy",
            style="",
            colors=[],
            start=wks[i],                               #and start date = wks[1]
            end=wks[i] + timedelta(days=num),
            createdBy=None))                        #so models[0] = wks[0] = wk0 = the 0th week if today is the 14th week
    
models.append(Challenge(id=11,                    
            posts=[],
            noun="cat",
            verb="sunbathes",
            adj="stout",
            emotion="",
            style="",
            colors=[],
            start=wks[11],                              
            end=wks[11] + timedelta(days=num),
            createdBy=None))    

models.append(Challenge(id=12,                    
            posts=[],
            noun="balloon",
            verb="dances",
            adj="tragic",
            emotion="",
            style="",
            colors=[],
            start=wks[12],                              
            end=wks[12] + timedelta(days=num),
            createdBy=None))    

models.append(Challenge(id=13,                    
            posts=[],
            noun="fire",
            verb="tempts",
            adj="wicked",
            emotion="",
            style="",
            colors=[],
            start=wks[13],                              
            end=wks[13] + timedelta(days=num),
            createdBy=None))    

models.append(Challenge(id=14,                    
            posts=[],
            noun="fox",
            verb="jumps",
            adj="quick",
            emotion="",
            style="",
            colors=[],
            start=wks[14],                              
            end=wks[14] + timedelta(days=num),
            createdBy=None))    

models.append(Challenge(id=15,                    
            posts=[],
            noun="city",
            verb="",
            adj="pink",
            emotion="melancholic",
            style="",
            colors=[],
            start=None,                              
            end=None,
            createdBy="elaine13@email.unc.edu")) 

print(models)
# models = [
 
# ]
