"""Sample Challenge models to use in the development environment.

These were intially designed to be used by the `script.reset_db` module."""

from ...models import Challenge
from datetime import datetime, timedelta

#date variables
num = 7
wks = []
wks.append(datetime.now()- timedelta(days=num))  #wk14 or wks[0] should be a wek from today's date
for i in range(1,15):      #wk1-13 or wks[1:13] should automatically be the previously created week's start date minus 7 days
    wks.append(wks[i-1] - timedelta(days=num))

wks.reverse() #now wks[0] = wk0 (the farthest date from today) and wks[14] = wk14 (today's date)

models = []

models.append(Challenge(id=1,                    
            posts=[],
            noun="",
            verb="",
            adj="default",
            emotion="",
            style="",
            colors=[],
            start=None,                              
            end=None,
            createdBy="elaine13@email.unc.edu")) 

models.append(Challenge(id=2,                    
            posts=[],
            noun="woman",
            verb="wielding",
            adj="fierce",
            emotion="",
            style="",
            colors=[],
            start=wks[11],                              
            end=wks[11] + timedelta(days=num),
            createdBy=None))    

models.append(Challenge(id=3,                    
            posts=[],
            noun="balloon",
            verb="dancing",
            adj="tragic",
            emotion="",
            style="",
            colors=[],
            start=wks[12],                              
            end=wks[12] + timedelta(days=num),
            createdBy=None))    

models.append(Challenge(id=4,                    
            posts=[],
            noun="fire",
            verb="tempting",
            adj="wicked",
            emotion="",
            style="",
            colors=[],
            start=wks[13],                              
            end=wks[13] + timedelta(days=num),
            createdBy=None))    

models.append(Challenge(id=5,                    
            posts=[],
            noun="fox",
            verb="jumping",
            adj="quick",
            emotion="",
            style="",
            colors=[],
            start=wks[14],                              
            end=wks[14] + timedelta(days=num),
            createdBy=None))    

models.append(Challenge(id=6,                    
            posts=[],
            noun="mountains",
            verb="",
            adj="",
            emotion="",
            style="",
            colors=["#c87987", "#636385", "#301312"],
            start=None,
            end=None,
            createdBy="elaine13@email.unc.edu")) 

models.append(Challenge(id=7,                    
            posts=[],
            noun="city",
            verb="burning",
            adj="",
            emotion="",
            style="impressionism",
            colors=[],
            start=None,
            end=None,
            createdBy="elaine13@email.unc.edu")) 

models.append(Challenge(id=8,                    
            posts=[],
            noun="birds",
            verb="watching",
            adj="",
            emotion="love",
            style="",
            colors=[],
            start=None,
            end=None,
            createdBy="elaine13@email.unc.edu")) 

models.append(Challenge(id=9,                    
            posts=[],
            noun="intelligence",
            verb="",
            adj="artificial",
            emotion="",
            style="",
            colors=[],
            start=None,                              
            end=None,
            createdBy="olivia@olivia.com"))

models.append(Challenge(id=10,                    
            posts=[],
            noun="meme",
            verb="",
            adj="",
            emotion="",
            style="",
            colors=[],
            start=None,                              
            end=None,
            createdBy="elaine13@email.unc.edu")) 
