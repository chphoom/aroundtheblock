"""Sample Post models to use in the development environment.

These were intially designed to be used by the `script.reset_db` module."""

from ...models import Post
from datetime import datetime, timedelta

lucy1 = Post(id=0,
            img="https://cdnb.artstation.com/p/assets/images/images/032/998/319/large/christophe-young-134crp.jpg?1608102233",
            title="Swordwoman 1",
            desc="Art by https://www.artstation.com/christopheyoung",
            private=False,
            created=datetime.now(),
            challenge=12,
            user_id="lucy@lucy.com",
            comments=[],
            tags=[])

lucy2 = Post(id=1,
            img="https://cdnb.artstation.com/p/assets/images/images/024/888/131/large/seunghee-lee-9-final22s1000.jpg?1583861930",
            title="Swordwoman 2",
            desc="Art by https://www.artstation.com/seunghee",
            private=False,
            created=datetime.now(),
            challenge=12,
            user_id="lucy@lucy.com",
            comments=[],
            tags=[])

lucy3 = Post(id=2,
            img="https://cdnb.artstation.com/p/assets/images/images/005/530/553/large/hicham-habchi-katana-girl.jpg?1491746594",
            title="Swordwoman 3",
            desc="Art by https://www.artstation.com/hichamhabchi1",
            private=False,
            created=datetime.now(),
            challenge=12,
            user_id="lucy@lucy.com",
            comments=[],
            tags=[])

post3 = Post(id=3,
            img="",
            desc="Privacy test",
            private=True,
            created=datetime.now(),
            challenge=10,
            user_id="anonymous",
            comments=[],
            tags=[])

elaine1 = Post(id=4,
              img="https://cdn.discordapp.com/attachments/525419273888202795/1098122459997282394/IMG_3058.jpg",
              title="Dreamy Mountains",
              desc="I love the idea of using unique colors to paint landscapes.",
              private=False,
              created=datetime.now(),
              challenge=16,
              user_id="elaine13@email.unc.edu",
              comments=[],
              tags=["landscape", "impressionism","meChallenge"])

elaine2 = Post(id=5,
               img="https://cdn.discordapp.com/attachments/525419273888202795/1098263927130959882/IMG_2954.jpg",
               title="Venice on Fire",
               desc="Made with acrylics, inspired by Leonid Afremov.",
               private=False,
               created=datetime.now(),
               challenge=17,
               user_id="elaine13@email.unc.edu",
               comments=[],
               tags=["impressionism", "meChallenge"])

elaine3 = Post(id=6,
               img="https://cdn.discordapp.com/attachments/525419273888202795/1098288726834167838/IMG_3054.jpg",
               title="Love Birds",
               desc="I wanted to draw a cityscape but also fit the prompt, so this is my rather loose interpretation.",
               private=False,
               created=datetime.now(),
               challenge=18,
               user_id="elaine13@email.unc.edu",
               comments=[],
               tags=["urban", "meChallenge"])

olivia1 = Post(id=7,
               img="https://cdna.artstation.com/p/assets/images/images/053/302/294/large/royalskies-moonswing.jpg?1661891003",
               title="Construction",
               desc="AI art generated by https://www.artstation.com/royalskies",
               private=False,
               created=datetime.now(),
               challenge=19,
               user_id="olivia@olivia.com",
               comments=[],
               tags=["urban", "meChallenge"])

olivia2 = Post(id=8,
               img="https://cdnb.artstation.com/p/assets/images/images/053/302/305/large/royalskies-adventurewithfriends.jpg?1661891015",
               title="Man's Best Friend",
               desc="AI art generated by https://www.artstation.com/royalskies",
               private=False,
               created=datetime.now(),
               challenge=19,
               user_id="olivia@olivia.com",
               comments=[],
               tags=["nature", "meChallenge"])

olivia3 = Post(id=9,
               img="https://cdnb.artstation.com/p/assets/images/images/053/302/365/large/royalskies-thelake.jpg?1661891102",
               title="Lonely Nights",
               desc="AI art generated by https://www.artstation.com/royalskies",
               private=False,
               created=datetime.now(),
               challenge=19,
               user_id="olivia@olivia.com",
               comments=[],
               tags=["nature", "meChallenge"])

models = [
    lucy1,
    lucy2,
    lucy3,
    post3,
    elaine1,
    elaine2,
    elaine3,
    olivia1,
    olivia2,
    olivia3,
]
