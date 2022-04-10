# ReviewSense API
Reviewsense retrieves its data from a backend server hosted on an AWS EC2 service. The Flask instance running on the server uses a series of endpoints as detailed below.

## Table of Contents
1. [Movies](##Movies)
    * [Retrieve Movie](###Retrieve-Movie)
    * Search Movies
    * Retrieve Lowest Rated Movies
    * Retrieve Highest Rated Movies
    * Retrieve Most Popular Movies
2. Reviews
    * Display a Single Review
    * Display a Movie's Reviews
    * Display Sentiment of a Movie's Reviews
    * Display Sentiment Ratio of a Movie's Reviews
    * Display Keywords of a Movie's Reviews
    * Display All Reviews for a Movie Sharing a Keyword
4. Users
    * Retrieve User


## Movies

### Retrieve Movie
**URL** : `/movies`


**Params** : 
| Type        | Name           |
| ------------- |:-------------:|
| `string`    | `ref_num` |

**Method** : `GET`

**Response** :
```python
{
  "name": "The Valhalla Murders (2019\u2013 )", 
  "ref_num": 1
}
```

### Search Movies
**URL** : `/moviessearches`


**Params** : 
| Type        | Name           |
| ------------- |:-------------:|
| `string`    | `title` |
| `int`       | `page`  |

**Method** : `GET`

**Response** :
```python
[
  {
    "name": "Halloween III: Season of the Witch (1982)", 
    "ref_num": 72
  }, 
  {
    "name": "Good Witch (2015\u2013 )", 
    "ref_num": 329
  }, 
  {
    "name": "Strike Witches: Operation Victory Arrow: Episode #1.1 (2014) Season 1, Episode 1", 
    "ref_num": 508
  }, 
  {
    "name": "Brave Witches (2016\u2013 )", 
    "ref_num": 514
  }, 
  {
    "name": "The Chronicles of Narnia: The Lion, the Witch and the Wardrobe (2005)", 
    "ref_num": 535
  }, 
  {
    "name": "The Witcher (2019\u2013 )", 
    "ref_num": 895
  }, 
  {
    "name": "Bewitched (1964\u20131972)", 
    "ref_num": 998
  }, 
  {
    "name": "The Blair Witch Project (1999)", 
    "ref_num": 1466
  }, 
  {
    "name": "Wild Witch (2018)", 
    "ref_num": 1520
  }, 
  {
    "name": "Bewitched (2005)", 
    "ref_num": 1600
  }, 
  {
    "name": "Star Wars: The Clone Wars: Witches of the Mist (2011) Season 3, Episode 14", 
    "ref_num": 1828
  }, 
  {
    "name": "The Switch (I) (2010)", 
    "ref_num": 2148
  }, 
  {
    "name": "Little Witch Academia (2013)", 
    "ref_num": 2734
  }, 
  {
    "name": "Alfred Hitchcock Presents: The Big Switch (1956) Season 1, Episode 15", 
    "ref_num": 3184
  }, 
  {
    "name": "The Witches (1966)", 
    "ref_num": 4131
  }, 
  {
    "name": "The Last Witch (2013 TV Movie)", 
    "ref_num": 4537
  }, 
  {
    "name": "A Discovery of Witches (2018\u2013 )", 
    "ref_num": 5997
  }, 
  {
    "name": "Witchcraft III: The Kiss of Death (1991 Video)", 
    "ref_num": 6034
  }, 
  {
    "name": "The Witches of Eastwick (1987)", 
    "ref_num": 6042
  }, 
  {
    "name": "Escape to Witch Mountain (1975)", 
    "ref_num": 6199
  }
]
```

### Retrieve Lowest Rated Movies
**URL** : `/movies/lowest`


**Params** : 
| Type        | Name           |
| ------------- |:-------------:|
|     |  |

**Method** : `GET`

**Response** :
```python
[
  {
    "name": "Everfall (2017)", 
    "ref_num": 76369
  }, 
  {
    "name": "The Haunting of Grady Farm (2019)", 
    "ref_num": 75168
  }, 
  {
    "name": "Ouija Seance: The Final Game (2018 TV Movie)", 
    "ref_num": 83904
  }, 
  {
    "name": "The Sacred Riana: Beginning (2019)", 
    "ref_num": 28547
  }, 
  {
    "name": "Mad House: A Paranormal Documentary (2019)", 
    "ref_num": 18918
  }, 
  {
    "name": "5Gang: VIP (2019 Video)", 
    "ref_num": 150096
  }, 
  {
    "name": "Trico Tri Happy Halloween (2018)", 
    "ref_num": 129549
  }, 
  {
    "name": "Til vi falder (2018)", 
    "ref_num": 38470
  }, 
  {
    "name": "Muerte: Tales of Horror (2018)", 
    "ref_num": 33029
  }, 
  {
    "name": "2 Jennifer (2016)", 
    "ref_num": 99808
  }, 
  {
    "name": "Ikkayude Shakadam (2019)", 
    "ref_num": 85869
  }, 
  {
    "name": "Wreck (2020)", 
    "ref_num": 93658
  }, 
  {
    "name": "A Dangerous Date (2018 TV Movie)", 
    "ref_num": 20019
  }, 
  {
    "name": "Amityville Clownhouse (2017)", 
    "ref_num": 14728
  }, 
  {
    "name": "Feride (2020)", 
    "ref_num": 108319
  }, 
  {
    "name": "The Terrible Two (2018)", 
    "ref_num": 57647
  }, 
  {
    "name": "\u6bba\u624b\u4e92\u52a9\u540c\u76df (2019)", 
    "ref_num": 88977
  }, 
  {
    "name": "Awaken the Shadowman (2017)", 
    "ref_num": 23207
  }, 
  {
    "name": "El Coyote (2019)", 
    "ref_num": 37119
  }, 
  {
    "name": "Bad Frank (2017)", 
    "ref_num": 54555
  }
]
```

### Retrieve Highest Rated Movies
**URL** : `/movies/highest`


**Params** : 
| Type        | Name           |
| ------------- |:-------------:|
|     |  |

**Method** : `GET`

**Response** :
```python
[
  {
    "name": "Sword Art Online: Ray of Light (2019) Season 4, Episode 12", 
    "ref_num": 132342
  }, 
  {
    "name": "Wheels (2020)", 
    "ref_num": 81213
  }, 
  {
    "name": "Hilda: Chapter 9: The Deerfox (2020) Season 2, Episode 9", 
    "ref_num": 142835
  }, 
  {
    "name": "Pacified (2019)", 
    "ref_num": 66481
  }, 
  {
    "name": "Jewel Thief (1967)", 
    "ref_num": 25486
  }, 
  {
    "name": "My Loneliness Is Killing Me (2018)", 
    "ref_num": 19982
  }, 
  {
    "name": "A Peck on the Cheek (2002)", 
    "ref_num": 81890
  }, 
  {
    "name": "Transition (I) (2018)", 
    "ref_num": 166791
  }, 
  {
    "name": "We are a conversation (2014)", 
    "ref_num": 114856
  }, 
  {
    "name": "Michael Jackson: Remember the Time (1992 Video)", 
    "ref_num": 160049
  }, 
  {
    "name": "48 Hours with Muhammad Ali (2019)", 
    "ref_num": 111579
  }, 
  {
    "name": "Forget Me Not (II) (2019)", 
    "ref_num": 142106
  }, 
  {
    "name": "Quai des Orf\u00e8vres (1947)", 
    "ref_num": 72485
  }, 
  {
    "name": "Blue Bloods: Family Secrets (2020) Season 10, Episode 19", 
    "ref_num": 16759
  }, 
  {
    "name": "The Vision (2015 Video)", 
    "ref_num": 105766
  }, 
  {
    "name": "With - A Journey to the Slow Life (2020)", 
    "ref_num": 122187
  }, 
  {
    "name": "Trash (I) (2020)", 
    "ref_num": 67901
  }, 
  {
    "name": "Between the Shades (2017)", 
    "ref_num": 176297
  }, 
  {
    "name": "Lie Exposed (2019)", 
    "ref_num": 73710
  }, 
  {
    "name": "Don\"t Despair (2020)", 
    "ref_num": 145445
  }
]
```

### Retrieve Most Popular Movies
**URL** : `/homepage`


**Params** : 
| Type        | Name           |
| ------------- |:-------------:|
|     |  |

**Method** : `GET`

**Response** :
```python
[
  {
    "name": "Dil Bechara (2020)", 
    "ref_num": 1516
  }, 
  {
    "name": "\u5c0f\u4e11 (2019)", 
    "ref_num": 7468
  }, 
  {
    "name": "Wonder Woman 1984 (2020)", 
    "ref_num": 135315
  }, 
  {
    "name": "STAR WARS\uff1a\u5929\u884c\u8005\u7684\u5d1b\u8d77 (2019)", 
    "ref_num": 86977
  }, 
  {
    "name": "Laxmii (2020)", 
    "ref_num": 60962
  }, 
  {
    "name": "Gunjan Saxena: The Kargil Girl (2020)", 
    "ref_num": 11816
  }, 
  {
    "name": "Supernatural: Carry On (2020) Season 15, Episode 20", 
    "ref_num": 60851
  }, 
  {
    "name": "Tenet (2020)", 
    "ref_num": 1407
  }, 
  {
    "name": "Scam 1992: The Harshad Mehta Story (2020)", 
    "ref_num": 55188
  }, 
  {
    "name": "Mrs. Serial Killer (2020)", 
    "ref_num": 41
  }, 
  {
    "name": "Batman v Superman: Dawn of Justice (2016)", 
    "ref_num": 1744
  }, 
  {
    "name": "Coolie No. 1 (2020)", 
    "ref_num": 135316
  }, 
  {
    "name": "\u7375\u9b54\u58eb (2019\u2013 )", 
    "ref_num": 111188
  }, 
  {
    "name": "Mulan (2020)", 
    "ref_num": 25437
  }, 
  {
    "name": "Joker (2019)", 
    "ref_num": 596
  }, 
  {
    "name": "Asur: Welcome to Your Dark Side (2020\u2013 )", 
    "ref_num": 4246
  }, 
  {
    "name": "Terminator: Dark Fate (2019)", 
    "ref_num": 759
  }, 
  {
    "name": "The Shawshank Redemption (1994)", 
    "ref_num": 138
  }, 
  {
    "name": "Star Wars: The Rise Of Skywalker (2019)", 
    "ref_num": 269
  }, 
  {
    "name": "1917 (2019)", 
    "ref_num": 255
  }
]
```

## Reviews

### Display a Single Review
**URL** : `/reviews`


**Params** : 
| Type        | Name           |
| ------------- |:-------------:|
| `string`    | `review_id` |


**Method** : `GET`

**Response** :
```python
{
  "date": "30 September 2013", 
  "name": "brett-janovich", 
  "review": "The whole documentary is about a group of filmmakers going into the woods documenting the Blair witch but when then mysterious things go on and a friend goes missing but u never ever see the activity all u see is a shaking tent hear rocks being thrown then u see a dude standing up dead at the end like What the heck how can u stand up dead thats not even possible and the girl is screaming out of her lungs going downstairs then falls and dies how does that happen u don't see nothing else u never see anyone die u just stupid teens in the damn woods do yourselves a favor don't watch it because its the most dumbest film that I've ever seen go for grave encounters and 7 nights of darkness and the crying dead those films are better.", 
  "sentiment": -0.026260707320330343, 
  "title": "The Blair Witch Project Most Dumbest films ever"
}
```

### Display a Movie's Reviews
**URL** : `/reviewlists`


**Params** : 
| Type        | Name           |
| ------------- |:-------------:|
| `string`    | `movie_id` |
| `int`       | `page`      |

**Method** : `GET`

**Response** :
```python

  {
    "date": "1 September 2020", 
    "name": "gfmcniven", 
    "review": "If you love the idea of a movie that shows you the ground for an hour and you're terrified by a rock and a stick,this movie is for you. If you want to be scared,stay away you won't find any here. The reason I gave it 3 stars is because the setup was great,I wish they showed that movie!!!The most overrated movie in history", 
    "review_id": "rw6051989", 
    "sentiment": -0.020136379674918433, 
    "title": "Terrible"
  }, 
  {
    "date": "11 December 2008", 
    "name": "lucash42-1", 
    "review": "I was 16 when the Blair Witch Project came out on the big screen. At this time, it was the talk of the over-populated high school I attended. So one Friday night, I asked my girlfriend if she wanted to see it, she tentatively agreed. Once in our seats, many people around us were laughing and joking about the story, and what to expect.A man came in from the side door, and put both of his arms in the air in an attempt to quiet the young audience. He was an employee of the cinema and he began to speak with an incredible tone of seriousness.'Everyone please keep all of you're talking to a minimum, and please silence your pagers(cell phones weren't owned by many at this point). He said. 'This is a true story of these three young adults, and of how they lost their lives in a very tragic way.' With that, he exited.The hecklers were reduced to a minority, and it seemed as if no one spoke for quite some time. There was an uneasiness in the air that both myself and my girlfriend felt. Suddenly she leaned over and whispered in my ear.'Come on let's go see something else...' Before she could even finish her sentence, the lights died down, and the story began. We sat, glued to our seats, as it unfolded in such a way that you could barely tear your eyes away, and if you did, you were fearful that you would miss something vital.At this point, I was totally convinced that what I was witnessing was real. There was no room in my mind for doubt or logic, and the employee that spoke up in the beginning took care of that.The Blair Witch Project concluded, and I could never be more content with a movie after the first viewing. Normally I would focus on flaws, continuity, and the ever so popular question, 'Why didn't they just...' At 16 years old, I had found the first movie that scared the hell out of me. A decade later, it still makes me uneasy.", 
    "review_id": "rw1988460", 
    "sentiment": -0.007210550571166364, 
    "title": "Groundbreaking...in a sense"
  }, 
  {
    "date": "3 September 2011", 
    "name": "jbowslee", 
    "review": "This movie scared the heck out of me. What surprises me is that people I know who are scared watching any horror film thought this movie was boring. I believe a wild imagination is necessary to truly get this film. What scared me about this movie is what my imagination was doing every step of the way. What was happening while they were sleeping? What was happening when they heard screaming of their friend when he went missing? What was making those banging noises and why? Because this film does not show anything horrific, it is up to the viewer to fill in the missing spaces and this is what frightened me. I am sure what was going on in my mind could not have been portrayed in a film and still received an 'R' rating. The unknown and what could be happening is what made this film frightening. And the true horror in the eyes and voices of the filmmakers in this film more than reinforced my worst fears. Overall, this film did something that has not happened to me since I was about 10 years old. It made me afraid of the dark and of the strange noises in nature that we hear every day.", 
    "review_id": "rw2483607", 
    "sentiment": -0.013090005161243208, 
    "title": "Imagination is key"
  }, 
  {
    "date": "4 September 2011", 
    "name": "pk19652001", 
    "review": "Where do you begin. This is the worse movie i have viewed and on all levels. Just bad. Bad acting, bad camera work. People were afraid of this pos. You got to be kidding. Anyone giving this about a 4 is out of there minds. Its almost like its a spoof. Like a college movie with a bunch of idiots go out into the Forest and make a stupid movie on purpose. The premise is good and thats about it. And enough with this modern day shaking camera syndrome. This isn't Saving Private Ryan. What happen to the days of steady camera work, even on the amateur level. Please, if you haven't watched this crappy movie yet, don't waste 90 minutes of your life with it.", 
    "review_id": "rw2483893", 
    "sentiment": -0.06234614814877099, 
    "title": "Worse movie ever."
  }, 
  {
    "date": "6 September 2011", 
    "name": "annevejb", 
    "review": "Spoilers properly fitted some early drafts of this review due to politics. It is not so relevant now.I understand that this feature was released in 1999; a recently made story by a USA storyteller; using USA resources and personnel and locations.I purchased my Blu-ray as I considered that it was likely to be able to be interpreted as a comment about UK politics of around 1999. I was not disappointed though it took me some musing to realise that I could see parallels that felt real.It helped that I could wait until I found a lower than usual low cost second hand Blu-ray, for this I would not have wanted to pay typical second hand Blu-ray prices. Why pay that much if one is likely to get scared? So, I was purchasing a Blu-ray of something that was mostly filmed in 8mm. Except that is not as pointless as I would have once thought.An example of some detail that stood out for me: The team leader being the one with a map and compass, yet showing symptoms of giving outward indicators of using them properly and results that might come from trusting one's heart rather than what technical indicators say? So, very rarely there might be times when even social outcasts might benefit from that, but to quote Full House series: How rude of me to consider feminist warfare in such terms. Not many might agree with my opinion if I clearly say what it is based on.I expect that this story is more likely to relate to USA politics of circa 1992 to 98 than UK 1999, but why that title for a USA story?", 
    "review_id": "rw2484951", 
    "sentiment": 0.004548450347466976, 
    "title": "A guess about the politics, v1.01"
  }, 
  {
    "date": "8 July 2020", 
    "name": "nashw82", 
    "review": "Love it or hate it you have to admit it changed the horror movie landscape and introduced a new sub genre and style of film making. Without the success of Blair Witch you wouldn't have series like Paranormal Activity and other found footage flicks. As far as the movie goes, I watched it with little prior knowledge and while it was definitely a slow and shakily shot it managed to ratchet up the fear and intensity with simple but effective methods and annoying though fitting acting. Each night they spent in the forest added to the tension as you wondered what they would encounter next. The abrupt and frightening ending was suitable for a found footage film and it left me with a fear of people quietly facing walls without responding haha.So, however you feel about it, you can't deny that its left its mark on the horror movie landscape.", 
    "review_id": "rw5890666", 
    "sentiment": -0.005114608643360498, 
    "title": "Brilliant but Divisive."
  }, 
  {
    "date": "20 December 2008", 
    "name": "diegoavilarodriguez", 
    "review": "OK, I have to be honest here, I saw this movie when I was 6 years old and later on watched it again to remember what was so bad about this movie... and now I remember why I hate this movie so much. First the bad things on this movie, this movie is so low budget that the whole documentary-like style of the camera had to obligatory cause they couldn't afford any camera men(though that style did change the world of movie making). Next, the plot, wow lost in the woods how original, that was seen in Friday the 13th so the whole lost in the woods things isn't so original, now the reason why they are lost in the woods was original but worst part of this film is the fact that it builds suspense for nothing(like the scene when they ran out of the tent, screaming and scared, suspenseful but not scary cause you don't even know what they running from.)For all I care it could be Bigfoot attacking them. Now the main thing people say about why this movie was so great was because they claim that the movie activates their 'imagination', and I think that means that this movie leaves out so many unanswered questions that to them it's fun to fill in the blanks, of course not like the movie disappearance in which they leave out so many blanks it makes the movie awful, well that wasn't the case with the Blair witch project, but still even if it is fun to fill in the blanks with this film that is no excuse for the people who don't like to fill in the blanks, so to me it sounds like people like this movie because it basically wastes their time. And now we come to the center question of this film which is: Why did they not show the witch?! Now if they had shown the witch, I would just recommend you rent this movie but no, this movie is like a nightmare on elm street without Freddy Krueger, you wait around for something to happen, and when they finally come the ending the idiot chick drops the camera which honestly is a disappointment, you expect something creepy and all that, when nothing really happens at all, and really if a 6 year old doesn't get scared watching this film how can an entire nation get scared over some movie which is nothing more than a publicity stunt to gain quick cash. Alright, now though the whole movie was a waste of time there is the upside of the fact that this movie did have an original storyline and did have the potential to be a horror classic, but of course it was not a true horror classic, now this movie is like the Hulk which was a good idea pretty much screwed up so this film needs a remake seriously and it needs it right now.", 
    "review_id": "rw1993007", 
    "sentiment": -0.0358037916210845, 
    "title": "this movie needs a remake... BADLY!!!!"
  }, 
  {
    "date": "7 May 2020", 
    "name": "pesaresigiovanni", 
    "review": "'The Blair Witch Project' feels authentic, even if it's not a documentary. Characters are realistic and well devoloped. The scary thing about this movie is the fear of being trapped in a forest without a map and without food, the fear of losing your mind in to this, the fear of what you can't see and the fear of the supernatural.", 
    "review_id": "rw5716107", 
    "sentiment": -0.00596342278198673, 
    "title": "How to make a very good movie with very low budget."
  }, 
  {
    "date": "21 February 2016", 
    "name": "eric262003", 
    "review": "In the 1999 horror classic 'The Blair Witch Project', we see three aspiring young filmmakers in 1994 set out on journey to do a documentary project based on a mysterious urban legend of the Blair Witch, who resides in a forest outside of a small town in Maryland. At first we're given the impression that this film was based off of their raw footage. The research going into the documentary is pretty shoddy in execution. The camera is purely out of focus and plus that Heather (Heather Donahue) repetitively utilizes 'u-huhs and yeahs' when she's asking questions towards the residents in the area. The opening scenes will surely make you gnash your teeth in annoyance. In fact this whole movie within a movie can be contrived at times. But once the young students enter the woods in search of the Blair Witch, the annoyance becomes more paranoiac as the fears and the anxieties start to send chills down our spines. Fortunately, the real filmmakers (Daniel Myrick and Eduardo Sanchez) were not as inept as the student filmmakers. We get some believable settings as the determined crew makes their way into the Maryland forests, where they are lost and the more trapped they are in the labyrinth of tress and shrubs, the more the adrenaline level goes up rapidly as the fears and paranoia become overwhelming. The daytime scenes start off quite equivocal as just the sounds of twigs from tree or on the ground snap can surely garner scares where expect the unexpected becomes focal in our minds as much as theirs. The rock piles that bear a resemblance of grave markers epitomizes a sense of unsettling tension of the students as though their eyes are playing tricks on them. These supernatural elements that the threesome face would likely drive anyone insane. The daytime fears seem pretty tame at first because the paranormal activity doesn't generate as much fear as the gang might shed some hope of finding their ways out of the woods, if they could trace back to where they begun their journey. When night comes and when things go bump in the night, the fear factor really gets the boost. The strange sounds nearby can be chillingly frightful and our brave but naive, unequipped students can do nothing but stick together. But nightfall the horror party finally gets tense and the audience watching this can feel this level of fear that anyone sneaking up behind them in the theaters can get someone a cardiac arrest. The forest is black, the theater is dark, everything is painted black during these scenes. The main prop in this movie is the cheap first-person camcorder which eventually becomes a character in itself as we become a part of this movie courtesy of the camera as well as the terror the gang faces it lingers on us as well as we feel convinced that there might be a Blair Witch lurking in these forests. These camera traits show adults that it is normal that human beings are scared of the dark and nothing shameful about that. The lack of preparation when entering the woods, the students have been faced in a sort of predicament they can't seem to get out of and the more they struggle the worst it gets. When Heather the booger- dripping leader of the team she confesses that it was her stubborn ways and determination to finding the truth she begs her cohorts Josh and Michael for forgiveness, we actually feel for her without the audience feeling manipulated.'The Blair Witch Project' is utilized as a staple on why we're obligated to watch and let alone produce films. When the students start to get restless, hungry and feared, Heather decides that now's the time to close the camera. Finally, the more restrained Joshua takes her camera and retaliates by pointing it back at her and shouting back at her as though, the camera rules her life while it affects the other two characters caught in the middle of the mess she put them in. In some ways this movie helped spawn shows like 'Ghost Hunters' and 'Ghost Adventures' where paranormal experts go around the world in seek of the truth in that there is life beyond our mortal lives.", 
    "review_id": "rw3419452", 
    "sentiment": -0.006245479921376352, 
    "title": "A Horror Film Where Fear is The Real Monster"
  }, 
  {
    "date": "23 September 2011", 
    "name": "itamarscomix", 
    "review": "The Blair Witch Project is an interesting mockumentary with an intriguing concept, that was the victim of many bad decisions, in the process of making it and especially of promoting it. The ambition, it seems, was to create an experimental art-house film that would appeal to mainstream audiences, and by marketing it as a 'horror' movie, create surprise and buzz. The attempt to bridge the gap between the two viewer groups was quite positive, but what it actually achieved is alienating both: the horror crowd was disappointed and annoyed, especially younger viewers who sneaked into an R rated movie expecting gore and heads-on horror; and the more sophisticated, avant garde crowd, turned off from day one by the film's promotion, didn't even bother to go see it.A decade later, it's easier to put all that aside, as well as the internet-based hype generated by the producers at the time. The film can now be appraised as what it is, an exercise in experimental filmmaking, and an interesting one at that. It takes a lesson from the true great classics of horror - in that the fear of the unknown, the anxiety and anticipation of violence are much more effective than explicit violence in itself - and indeed, it's scarier than almost any horror movie created in the last twenty years, although the teenagers who usually go for that kind of movie will probably disagree. The Blair Witch Project creates tension and anxiety, and draws the viewer into the characters' world. And it doesn't matter one bit whether or not you think it might be real - in fact it's more impressive when you know that it's not.Unfortunately, it doesn't achieve true greatness in that respect either. In its attempt to bridge between mainstream horror and experimental indie movie-making, the film reaches a sort of middle ground that isn't quite here nor there, not quite satisfying anybody. The Blair Witch Project is not a classic or a great film, nor will it ever be, but it should be watched by fans of independent and experimental cinema and of classic horror, and remembered as a brave and innovative experiment that didn't quite make it.", 
    "review_id": "rw2492527", 
    "sentiment": -0.0027683637053605424, 
    "title": "Mis-marketing in action"
  }, 
  {
    "date": "10 July 2020", 
    "name": "gardnernrg", 
    "review": "I'll start off by saying this. In no regards is this film bad. Absolutely not. This is a good film that still lives up to its hype, 21 years after release. It is a classic in the horror genre, that every horror fan needs to watch.That being said, this isn't a perfect film either. Many times throughout the film I found myself dozing off, as there wasn't much happening, and it wasn't integral to the storyline/plot. And while I'll rip on the found footage style right now, I'll praise it in a second. The sudden jumps in footage as the characters stopped recording and then resumed can be terribly confusing. I found myself once or twice chasing my tail trying to figure out what just happened. These are most of the bad things, and of course there are others, but these are the things that made me rate it 6.Now for the good things. Estimated $60,000. For instance, Jordan Peele's 'Us' has an overall rating .4 higher than this. The budget for that? Estimated $20mil. For $60k this movie does so much! It delivers such an amazing performance for the little budget it had. Now, I said I'd get to the found footage style. I already ripped on that, now to praise. Coincidentally, they are kind of the same thing. The found footage style, where I found myself chasing my tail, was an incredible way t deliver this story. Earlier on, the characters are sane and have their wits about them. The storyline is clean and precise. Slowly as the movie progresses more and more sudden and big cuts/jumps come along, and almost simulate what the characters were feeling in that moment. For what this film promises, it delivers. A college film student documentary. Not professional acting, editing, shooting, etc. This film does what it says and does it in a great way. Has its flaws, but a good horror film nonetheless.", 
    "review_id": "rw5895781", 
    "sentiment": -0.005718680334146557, 
    "title": "The Blair Witch Project?"
  }, 
  {
    "date": "12 July 2020", 
    "name": "mikiv-65616", 
    "review": "This movie if watched alone is much more frightening than many others, it makes you feel alone and scattered so watch it alone", 
    "review_id": "rw5899444", 
    "sentiment": 0.0029371710276636584, 
    "title": "Watch this movie alone,is more frightening than the others 'jumpscare' movies"
  }, 
  {
    "date": "1 January 2009", 
    "name": "fuzzyfacefreak", 
    "review": "This has to be the absolute worst movie ever! Scary as Hell??? What part? Boring as Hell? Most definitely!! The only scary part was having to see a very long close up of the girl's nostrils moving. Seeing someone's grandmother in the shower would be much scarier!!The whole movie was so drawn out waiting for something to happen. You were expecting hillbillies, cannibals, hell even a zombie would have maybe saved this crap. Blair witch? What witch? There was way to much 'documentary filming' that was totally unnecessary.Screaming at piles of sticks? And don't forget the key to this disaster for our three young heroes... They lost the map...the f***ing map!!", 
    "review_id": "rw1999829", 
    "sentiment": -0.046125554649495214, 
    "title": "Seeing someone's grandmother in the shower would be much scarier!!"
  }, 
  {
    "date": "8 September 2020", 
    "name": "marco-47826", 
    "review": "She clearly is the witch everyone's been talking about. The scariest thing about this movie is how annoying and unlike able characters are. Especially her. When they don't scream and run around like lunatics, they yell and blame each other for mistakes they eventually make themselves. I will always be thankful to this movie for creating that awful sub-genre. Found footage. It is extremely unpleasant and directors seem to be hiding behind the excuse of close ups and pitch black shots, to create the cheapest effects. As far as this one goes, you never see anything that proves the existence of supernatural forces. And you mostly lean towards bad joke theory. On and off screen. You can imagine any explanation except the one the title is referring to. At least the sequel, as mediocre as it can be, tried to have a script and a plausible conclusion. Which the first movie lacked, and all you're left with, is an unbelievable so called mysterious tape that never gives you the impression of being anything but a home movie friends made. Pretending to be lost in the woods, while evil forces are taunting them...", 
    "review_id": "rw6075431", 
    "sentiment": -0.03488562807528235, 
    "title": "The Heather Donahue project."
  }, 
  {
    "date": "30 September 2013", 
    "name": "brett-janovich", 
    "review": "The whole documentary is about a group of filmmakers going into the woods documenting the Blair witch but when then mysterious things go on and a friend goes missing but u never ever see the activity all u see is a shaking tent hear rocks being thrown then u see a dude standing up dead at the end like What the heck how can u stand up dead thats not even possible and the girl is screaming out of her lungs going downstairs then falls and dies how does that happen u don't see nothing else u never see anyone die u just stupid teens in the damn woods do yourselves a favor don't watch it because its the most dumbest film that I've ever seen go for grave encounters and 7 nights of darkness and the crying dead those films are better.", 
    "review_id": "rw2878569", 
    "sentiment": -0.026260707320330343, 
    "title": "The Blair Witch Project Most Dumbest films ever"
  }, 
  {
    "date": "7 October 2011", 
    "name": "LuvzHorror", 
    "review": "As a major fan of the horror genre I heard about The Blair Witch project and simply HAD to go and see it! Thinking of myself as a hardened horror buff I was pretty sure that I'd enjoy every second, and I did, but I was terrified! The fact that I was heavily pregnant and had to return home to an empty house as my husband was working away should have been a deterrent, but I thought I'd be fine!My sister (who loathes horror movies with a passion) had seen Blair Witch the night before and said she was disappointed in it. She said it was over-hyped and simply not frightening. How wrong she was!The film starts with 3 student film makers, Heather, Josh and Mike, heading to Burketsville to make a documentary about the legend of The Blair Witch. They visit various sites of interest, speak to local people and hear the story of Rustin Parr. Parr was a local man who kidnapped, tortured and murdered 7 local children in the 40's. During his trial Parr claimed that he was possessed by the spirit of Elly Kedward, a woman burnt as a witch in the town of Blair. Burketsville was formerly known as Blair.The trio then head out into The Black Woods. They visit Coffin Rock, the site of the murder of 5 men. As the film progresses the students move further into the woods. Inevitably they become lost. What follows still scares me to this day. As fear takes over the sensibilities of the trio they begin to fight and argue with each other. Then, when night falls, strange happenings occur. Children are heard laughing, strange objects are left outside the tents. The students slowly descend into absolute terror. To go any further would mean including spoilers, which I always hate in a review. Needless to say the frustration of the students is passed on to the viewer. Shaky camera-work (this film being one of the first 'handheld camera' movies) only adds to the fear as we are unable to see what it is that is terrifying the students.I watched this film on the edge of my seat. On my return home I was physically afraid to be alone. I actually ended up staying the night at my parent's house! That's not to say that everyone will be afraid, judging by some of these reviews I think I must be an absolute coward for being scared by a film that some people have claimed made them fall asleep!But I will leave this review by saying one thing:I went into labour the next day - 3 weeks early!", 
    "review_id": "rw2499456", 
    "sentiment": -0.00798370360894845, 
    "title": "Unnerving!"
  }, 
  {
    "date": "25 October 2020", 
    "name": "uonlywish500", 
    "review": "I can understand that some like it, but for me this movie is just flat ... They say that knowing next to nothing reinforces the horror of the movie, but I disagree! I agree that we cannot explain everything orally, but there is a limit!It's flat, it's not scary, the characters are not really endearing and therefore, we are not invested in the film, and every thing that happens to them left me unmoved, I almost didn't care.The final scene, for example, did absolutely nothing to me.I still want to say that there are some good ideas, like the idea of dolls that really freaked me out, but it stops there! They do nothing of this story, it was useless!It's a pity, but I don't like this movie. It is at the best just bad, if not really bad.", 
    "review_id": "rw6204504", 
    "sentiment": -0.03617342995137113, 
    "title": "How to say it like that...?"
  }, 
  {
    "date": "26 October 2020", 
    "name": "kmezdi", 
    "review": "I didn't rate it after I watched it because I didn't know what to make of it. But after some time, or the day after, that's when I started feeling agitated. I kept looking at my back and whatnot. Which is unusual for me. Maybe it's the thought of the unknown that made this movie a popular horror.I liked the pace and the scene where the girl didn't want to blink, that was a good bit. Though the characters' ways on how to deal with a situation is mindless and it made me laugh.", 
    "review_id": "rw6207510", 
    "sentiment": -0.006518403178194256, 
    "title": "Different."
  }, 
  {
    "date": "11 September 2020", 
    "name": "tchitouniaram", 
    "review": "Considering,that there are almost no horrors,that I didn't watch)))the Blair witch remains the favorite,timeless and respected film ever!The minimalist style,with tiny budget,but enormous talent,makes it a wonder movie,for me!The creators masterfully play on basic human fears:unknown,getting lost,darkness and night forest.Without any special effects,gore and jump scares,it still remains one of the scariest horrors ever made.Just absolutely love it!", 
    "review_id": "rw6085122", 
    "sentiment": 0.009920469615892972, 
    "title": "One and only!"
  }, 
  {
    "date": "24 November 2020", 
    "name": "johnathanenfinger", 
    "review": "It's an hour and a half of obnoxious yelling, arguing, and expletives. Please save yourself the time and watch absolutely ANYTHING else.", 
    "review_id": "rw6304554", 
    "sentiment": -0.06829584834923069, 
    "title": "Yikes"
  }, 
  {
    "Review Tokens": [
      [
        "horror", 
        23
      ], 
      [
        "like", 
        16
      ], 
      [
        "camera", 
        13
      ], 
      [
        "fear", 
        13
      ], 
      [
        "found", 
        11
      ], 
      [
        "bad", 
        11
      ], 
      [
        "woods", 
        11
      ], 
      [
        "scared", 
        10
      ], 
      [
        "people", 
        9
      ], 
      [
        "story", 
        9
      ], 
      [
        "characters", 
        9
      ], 
      [
        "time", 
        8
      ], 
      [
        "night", 
        8
      ], 
      [
        "lost", 
        8
      ], 
      [
        "ever", 
        8
      ], 
      [
        "good", 
        8
      ], 
      [
        "footage", 
        8
      ], 
      [
        "nothing", 
        8
      ], 
      [
        "students", 
        8
      ], 
      [
        "first", 
        7
      ]
    ]
  }, 
  {
    "Overall Sentiment": -0.019015952305979817
  }
]
```

### Display Sentiment of a Movie's Reviews
**URL** : `/reviewlists/sentiment`


**Params** : 
| Type        | Name           |
| ------------- |:-------------:|
| `string`    | `review_id` |
| `int`       | `page`      |
| `string`    | `sentiment` |


**Method** : `GET`

**Response** :
```python
[
  {
    "date": "6 September 2011", 
    "name": "annevejb", 
    "review": "Spoilers properly fitted some early drafts of this review due to politics. It is not so relevant now.I understand that this feature was released in 1999; a recently made story by a USA storyteller; using USA resources and personnel and locations.I purchased my Blu-ray as I considered that it was likely to be able to be interpreted as a comment about UK politics of around 1999. I was not disappointed though it took me some musing to realise that I could see parallels that felt real.It helped that I could wait until I found a lower than usual low cost second hand Blu-ray, for this I would not have wanted to pay typical second hand Blu-ray prices. Why pay that much if one is likely to get scared? So, I was purchasing a Blu-ray of something that was mostly filmed in 8mm. Except that is not as pointless as I would have once thought.An example of some detail that stood out for me: The team leader being the one with a map and compass, yet showing symptoms of giving outward indicators of using them properly and results that might come from trusting one's heart rather than what technical indicators say? So, very rarely there might be times when even social outcasts might benefit from that, but to quote Full House series: How rude of me to consider feminist warfare in such terms. Not many might agree with my opinion if I clearly say what it is based on.I expect that this story is more likely to relate to USA politics of circa 1992 to 98 than UK 1999, but why that title for a USA story?", 
    "review_id": "rw2484951", 
    "sentiment": 0.004548450347466976, 
    "title": "A guess about the politics, v1.01"
  }, 
  {
    "date": "12 July 2020", 
    "name": "mikiv-65616", 
    "review": "This movie if watched alone is much more frightening than many others, it makes you feel alone and scattered so watch it alone", 
    "review_id": "rw5899444", 
    "sentiment": 0.0029371710276636584, 
    "title": "Watch this movie alone,is more frightening than the others 'jumpscare' movies"
  }, 
  {
    "date": "11 September 2020", 
    "name": "tchitouniaram", 
    "review": "Considering,that there are almost no horrors,that I didn't watch)))the Blair witch remains the favorite,timeless and respected film ever!The minimalist style,with tiny budget,but enormous talent,makes it a wonder movie,for me!The creators masterfully play on basic human fears:unknown,getting lost,darkness and night forest.Without any special effects,gore and jump scares,it still remains one of the scariest horrors ever made.Just absolutely love it!", 
    "review_id": "rw6085122", 
    "sentiment": 0.009920469615892972, 
    "title": "One and only!"
  }, 
  {
    "date": "16 October 2013", 
    "name": "RecceR", 
    "review": "Three film students visit a small rural town in Maryland in order to make a documentary about its dark history. Things begin going wrong once they are in the woods and gradually become a living nightmare that unfolds from their point of view. The Blair Witch Project is one of the most effectively creepy and scary horror movies of our time. The situations, the people and the acting all seem so real and help create this fictional legend. Because there is pretty much a complete lack of visuals (that most modern movies use as a crutch) and the audience must rely on the reactions from the cast makes this pure genius. Of course, it wouldn't have worked had the actors failed in their performances. But that was definitely not the case with this film. I have only seen it a few times, but nearly every moment sticks with me because The Blair Witch Project is such an unnerving and haunting film.", 
    "review_id": "rw2888312", 
    "sentiment": 0.0034899923978285513, 
    "title": "unnerving and haunting film"
  }, 
  {
    "date": "27 October 2020", 
    "name": "geeward-73776", 
    "review": "As the title says its a cult classic and worth a watch but I wouldn't say it's the best film I've ever watched. From what I understand this sparked the handheld elements to movies and its a really well thought out and put together film. It is quite believable but could be scarier. The element that this could be real is a good addition and really adds to the film. Although I'm not sure exactly what happened at the end but I'm sure this is intended.", 
    "review_id": "rw6211225", 
    "sentiment": 0.004624545794243136, 
    "title": "Cult Classic and worth the watch"
  }, 
  {
    "date": "18 March 2020", 
    "name": "leplatypus", 
    "review": "This movie is actually a stroke of genius.I heard it from my brother who had a friend who was terrified by it!At this time, i was in Strasbourg studying Human Rights and befriended a greek student. I was excited by this kind of experience and for a date, i propose her to go watch it together and i sold it to her with the same argument: ' i heard it's really frightening !'.Honestly i don't remember to have been scared maybe because i already known the context but my friend liked it so i suppose it's OK!", 
    "review_id": "rw5559403", 
    "sentiment": 0.0018237504807831078, 
    "title": "an unbelievable word of mouth (screen)"
  }, 
  {
    "date": "13 December 2013", 
    "name": "AaronCapenBanner", 
    "review": "Eduardo Sanchez & Daniel Myrick co-directed this surprisingly effective film that is presented as the realistic 'found footage' of a documentary made by three college filmmakers Heather Donahue, Michael Williams, & Joshua Leonard(who play themselves) and how they set out to make a film about a local legend called the Blair Witch, who is rumored to haunt the woods in rural Maryland after being left to die by townspeople who feared she was a witch. The students, after done interviewing locals, go into the woods and see some strange things before getting lost, as they literally go in circles with no idea how or why. After hearing sinister sounds at night, one of them goes missing, as tensions flair and hopes are dashed... Surprise hit in 1999 is still an exceptionally well-done horror film, which uses imagination and suggestion to tell its story(except for the rampant profanity!). Creates a genuinely unsettling atmosphere of fear and dread, and the acting is good too, leading to a most stunning end.", 
    "review_id": "rw2921183", 
    "sentiment": 0.0014464117357063293, 
    "title": "Where Are They?"
  }, 
  {
    "date": "23 September 2020", 
    "name": "boomitsrudi", 
    "review": "Watching this alone at night with no lights on for the first time was a great horror movie experienceanother shot wasn't that spectacular at all i have to admit but first sight was pretty good", 
    "review_id": "rw6116975", 
    "sentiment": 0.0026202189888965967, 
    "title": "great shocker"
  }, 
  {
    "date": "28 May 2020", 
    "name": "XxEthanHuntxX", 
    "review": "The film's main strength lies in its authenticity, in its impressive restraint and the actor's efforts, and how much intelligence and storytelling was hidden in a movie that looks so raw and authentic. Irritation slides over into fear and rising panic, slow-building tension and psychological melt-downs results in a painstakingly genuine filmmaking. But as an Horror picture, 'The Blair Witch Project' rather suffer from a important problem, and that is that it is not very horrifying.", 
    "review_id": "rw5780717", 
    "sentiment": 0.007455599520329752, 
    "title": "The Blair Witch Project"
  }, 
  {
    "date": "7 December 2020", 
    "name": "LnineB", 
    "review": "This film will always be one of the most inventive and original horror films in my book. Although it wasn't the first found footage film, it definitely set off the trend of so many followers for the next two decades. In addition to that , this film will also be known as the film that probably had the most inventive marketing strategies ever. It literally went viral before anyone even knew the term or anyone even knew that such a thing could be accomplished with the internet. With all of that said, the film is constantly knocked by horror fans for not being 'scary' or not realistic or 'cheesy'. To me the film shows how anyone can execute a powerfully suspenseful story with little to no violence and a very low budget. It all starts with the acting. The performances by the actors in this film are absolutely remarkable. I was 14 when I first saw it and literally still thought it was 'real' when I went to the theater to see it. This was accomplished by the believable and realistic performances by everyone , especially the lead female. The story is simple but down right scary and honestly would've held its own as just a survivalist film. This leads to my only gripe with the film and that's the fact that it really didn't need to develop, the supernatural and/or murderer plot beyond what it did in the beginning. It really only served the purpose of giving others a reason to hate on it. Just being lost in the woods is scary enough and to me the director did an amazing job of creating an extreme level of intensity just with that part of the story. The ending was open ended enough to send chills down your spine, once again without showing any blood or gore. It's affective with just atmosphere and acting. Like I said earlier , some people really hate this film but what I find interesting is that many people who hate it love films that were obviously influenced by it. Without Blair Witch we would not have Paranormal activity, Quarantine or even the most recent The Host.", 
    "review_id": "rw6344724", 
    "sentiment": 0.00014897603137961241, 
    "title": "The originator in so many ways."
  }, 
  {
    "date": "26 January 2014", 
    "name": "Asentiff2004", 
    "review": "Three film students travel into the woods of Burketsville, Maryland to document the legend of the Blair Witch only to never return, only there footage is discovered.The film that contributed to and help revitalize the genre for found footage/ first person films. Now in that aspect the film was truly trend-setting. Its story though original failed in many aspects. The film does a decent job in building tension as does its pacing, but for the most part this film only comes off as slightly creepy. A lot of the potential of this film is lost in its three amateur actors who do little but bicker, argue and fight throughout the length of the film. What made this film so immensely popular when it first came out was in its marketing. A lot of film goers at the time felt as though this film was actual true footage, when in turn it was just a low grade horror film. Though a nod has to be given to this film as it did create a new genre within film, that went on to span such films as Cloverfield and Chronicle. All in all for a horror film it misses its mark in some aspects but in others it does very well, which is in its pacing and its tension, but ultimately falls short, mostly in its conclusion, which leaves much to be desired.", 
    "review_id": "rw2949549", 
    "sentiment": 7.750106294475793e-05, 
    "title": "Oh thats an old story..."
  }, 
  {
    "date": "14 November 2020", 
    "name": "deanesposito", 
    "review": "While it is pretty slow and not much happensThis movie is amazing, it feels so real and the performances will never be met.Easily one of the scariest and realistic movies ever made", 
    "review_id": "rw6268759", 
    "sentiment": 0.015387361443455504, 
    "title": "Slow burning masterpiece"
  }, 
  {
    "date": "9 August 2020", 
    "name": "avamacdougall", 
    "review": "Wow a 10/10 masterpiece. I had to turn on the lights near the end of the film. This film balances heavy tension and foreboding mysteries with grace, ultimately creating, while yes a slow burn, a film with integrity. this right here is a classic", 
    "review_id": "rw5976703", 
    "sentiment": 0.01826327364027116, 
    "title": "is this real?"
  }, 
  {
    "date": "6 October 2020", 
    "name": "qotgp", 
    "review": "Truly a classic and a gateway to the greatness of found footage horror. The acting is phenomenal and the ending scene leaves me with chills every time. It's one of the movies that leaves me uncomfortable every time that I watch it.", 
    "review_id": "rw6151661", 
    "sentiment": 0.01214323501880448, 
    "title": "The greatest found footage horror film. Ever."
  }, 
  {
    "date": "16 October 2020", 
    "name": "a-11737", 
    "review": "Let me get this out of the way. The scary part of this film isn't the witch, but rather the paranoia and unending stress and fear that the characters in this film experience. I first saw this film on Amazon Prime, and currently own it on DVD, and I love it. The characters are likable and feel quite realistic, and the best part of this film is that not much truly happens. It's not like Paranormal Activity where there is something supernatural going on, and the fear of that entity is driving them to insanity. However, I feel that the lack of any true supernatural occurrences except for a few key moments in the film adds to the suspense and the fact that these characters are being driven to near insanity by their own fear, stress, and anxiety of the fact they think there's something out there.If you saw this film back when it first came out (which I did not), you likely thought that the occurrences and events in this film actually happened, and this truly was a piece of found footage film. But I don't think that's the scary part of The Blair Witch Project. The scariest part, as I stated before, is the fear and anxiety the characters in this film experience even though there may not truly be anything out there. But I suppose that it's all left up to your interpretation of the film.Either way, watch it if you're a fan of found footage horror or just horror films in general. Seriously though, check it out if you haven't yet.", 
    "review_id": "rw6180731", 
    "sentiment": 0.0006516052401118428, 
    "title": "A fantastic found footage horror flick"
  }, 
  {
    "date": "30 November 2004", 
    "name": "malkane316", 
    "review": "POSSIBLE SPOILERS!!The wild hysteria surrounding this movie proves that the majority of the cinema going audience can still be fooled into believing anything they see or hear, or think they do, but that doesn't change the fact that it is an extremely convincing and effective horror flick. A certain number of people on these boards, and who have reviewed B. Witch Project HATE the film for varying, understandable reasons. When i first watched this, i watched intently, knowing exactly what the directors were playing at, and i found great enjoyment in watching the reactions of those who thought it was real. Did it unsettle me? No. Did it make me jump like the horror movies that rely on loud noises to scare (the Ring Remake) ? No. But it was the first horror movie in a very long time to put a smile on my face, and make me shiver. If you can remember back to when you played hide and seek as a kid- the feeling you had when the person looking for you was 10 feet away and coming closer- that is what this film gives, in a much greater quantity.It is slow moving, and if you do not enjoy the pace, then you may not enjoy the film, but it compensates this by being short and concise, juxtaposed against how the 3 campers must have felt as the hours dragged by- the point i take from this is that in life we only remember a series of memories, images pasted together to make little sense, and life seems much shorter than it actually was.The camera use and grainy feel again may be fuel for hatred or love, but it works perfectly- they don't know what is going on, and neither do we, but that doesn't matter because in an uncertain and threatening situation, the natural human reaction is to run or fight. Drained, exhausted, paranoid, they run. Ever had a nightmare about running away from something, but not knowing exactly what it was, or why you are running?The best part of the movie (apart from the hilarious 'i kicked the map into the river' scene) is the last few minutes when Michael and Heather enter the house following Josh's screams. I get the 'shivering' feeling throughout this (probably 'spine tingling' or 'chilling' is the 'correct term'), especially when Heather screams, and the ending is excellent as our feelings and fear somehow builds and climaxes (apologies for the sexual connotations) in perfect harmony with what is happening on screen. The actors are clearly convincing, again look at the hysteria for proof, and although they are not called upon to do much, they do it well. Oh yeah, the only scene i do not like is the 'Heather snot' scene- it is too long and breaks up the momentum. Few great horror films come along these days, this is one- embrace it, let yourself be sucked in to feel the full effect, don't be critical, and realize how good it is. 9 out of 10", 
    "review_id": "rw0972529", 
    "sentiment": 0.0006693562848403724, 
    "title": "Quick Reviews!!"
  }, 
  {
    "date": "30 December 2010", 
    "name": "horrormoviefan101", 
    "review": "Who would've thought that a movie filmed in grainy camera quality and by a completely unknown cast and crew would still be remembered and talked about to this day. Despite being eleven years old, this movie doesn't feel dated at all and remains incredibly horrifying. Everything about this movie hits the bullseye. The three actors are all magnificent, especially Heather Donahue, who's gut-wrenching (and often parodied) final confession to the camera is truly chilling. The shaky camera effects are poor quality, but that's what make this film so believable. And although this isn't the first time that a first-person perspective has been used, this is definitely the most well done version. The movie just feels so raw in its presentation and every little thing about it works in. But what really makes this film stand out (at least to me) is the fact that the audience is never given a view of the monster. In nearly every single horror film, we are given the chance to at least get a glimpse of the thing causing all of the death and destruction, however it's left entirely up to the imagination as to what's really going on. So many questions are left unanswered by the end and it's definitely for the better. 'Blair Witch' is a movie that truly redefined the horror genre, opening the door for a wave of imitators and copycats. Even if you're not a horror fan, you should still at least check this wonderful piece of cinema out.", 
    "review_id": "rw2361466", 
    "sentiment": 0.000701140243692641, 
    "title": "a film that truly redefined the horror genre"
  }, 
  {
    "date": "6 October 2015", 
    "name": "CinemaClown", 
    "review": "Incorrectly labelled by many as the film that launched the found footage subgenre of horror, The Blair Witch Project was a new type of scare for the majority of mainstream audience at its time of release. It was promoted as retrieved footage before its premiere, the fate of the cast was kept secret, and it was filmed in a way most home movies are made, due to which many were easily sold by its gimmick.The Blair Witch Project concerns three film students who decide to produce a documentary about a local legend known as the Blair Witch. They travel to Maryland forest on a two day hike to find evidence to support the myth but never returned. A year later, their camera was found in the woods with the film in it. The surviving footage was eventually compiled into a movie that captures what really happened to them.Written, directed & edited by Daniel Myrick & Eduardo S\u00e1nchez, The Blair Witch Project is a cleverly crafted cinema that gets right where most found-footage films go wrong. Here, the reason why its camera is on & around all the time actually makes sense. The story is simple and its the simplicity of it all that makes it interesting. And by not showing any supernatural entity on camera, it allows the viewers' imagination to run wild.The shooting location & setting add a few elements of its own to the picture. Using the real names of the cast brings more plausibility to what the film claims to be. The camera-work is raw, unrefined, grainy & poorly handled, which ultimately works in its favour. Its 81 minutes of footage raises the tempo quite nicely. And since the cast is responsible for shooting the film & keep the dialogue running in a natural manner, they did a pretty good job at it.On an overall scale, The Blair Witch Project may not look as effective today as it did during its time of release but it still ranks amongst the best examples of found footage horror. And what it lacks in conventional horror elements, it makes up with the fear of the unknown that connects its viewers with those trio of characters plus the situation they find themselves in, and that, in my opinion, is its biggest strength. A landmark in horror filmmaking and still the most influential of all found-footage flicks, this faux documentary comes recommended.", 
    "review_id": "rw3330243", 
    "sentiment": 0.0003594384334231052, 
    "title": "A Landmark In Horror Filmmaking And Still The Most Influential Found Footage Film"
  }, 
  {
    "date": "24 October 2019", 
    "name": "coneill97", 
    "review": "What Blair Witch Project does so well, is create an unsettling, uncomfortable tone that lingers throughout the movie. There is a constant feeling of unease that takes place as soon as the three lead characters enter the woods.The film does a great job of making a tale about witchcraft feel so realistic. This is primarily due to the incredibly believable performances of the cast, especially the main three, who we spent much of the runtime with. They always feel like real people, and their frustrations and fights with one another never feel forced but feel as if the oppressive atmosphere of the woods is influencing their actions.The movie has an incredibly effective setup, with locals from the town telling stories of the Blair Witch legend. The fact that these stories feel like they're being told from the perspective of real people gives them a chilling quality.The low quality, found-footage documentary style also adds to the grounded tone. It does not feel like a conventional movie due to the lack of a narrative structure or musical score. The occasional use of a 16mm black and white cameras is very effective in adding a chilling quality to the film, especially the daytime scenes in the woods.The use of sounds in this film is incredible. A lot of this movie takes place at night with a blank black screen, where we can hear only distant noises. By not showing us anything, it allows the audience to imagine what is out there in the woods, which makes it even scarier. This also applies to the Blair Witch, who we never see throughout the movie at all. Our imagination is more terrifying than anything that could have been put on screen. Despite not appearing, her presence is felt throughout.The final ten minutes of this movie is genuinely terrifying, with simple images such as children's handprints on the walls of the abandoned house in the woods, sticking with the viewer long after the film ends. And while it does end very abruptly, the final shot is very unsettling and gets under your skin.While the sense of realism created by the filmmakers works so effectively throughout the movie, it also has its negatives. By creating such realistic and believable central characters, they become unremarkable and uninteresting with minimal characterisation. This is only a minor flaw, however in an otherwise excellent horror movie.", 
    "review_id": "rw5210148", 
    "sentiment": 0.00418843229343802, 
    "title": "A Chillingly Realistic Found Footage Movie"
  }, 
  {
    "date": "25 October 2019", 
    "name": "droog-56936", 
    "review": "The cultural phenomenon that was The Blair Witch Project cannot be overstated. The found footage era of filmmaking caught hold and became the main way to put forth the horror genre for years. Despite the hundreds of movies that have used this technique only a handful have been any good.The Blair Witch Project succeeds more on what you can't see than what you can. The human terror of darkness is used to full effect here and the actors do such a stellar job of being immersed in the fear of the unknown that it swoops you right along with them. The Blair Witch Project stands as a classic that is still unsettling but also stretched the rules of a genre and how films were made and seen.", 
    "review_id": "rw5212623", 
    "sentiment": 0.0014589893646434723, 
    "title": "A Reworking Of The Horror Genre"
  }, 
  {
    "Review Tokens": [
      [
        "horror", 
        50.43478260869565
      ], 
      [
        "footage", 
        31.304347826086957
      ], 
      [
        "found", 
        27.82608695652174
      ], 
      [
        "feel", 
        20.869565217391305
      ], 
      [
        "time", 
        19.130434782608695
      ], 
      [
        "first", 
        19.130434782608695
      ], 
      [
        "story", 
        15.652173913043478
      ], 
      [
        "woods", 
        15.652173913043478
      ], 
      [
        "real", 
        15.652173913043478
      ], 
      [
        "fear", 
        15.652173913043478
      ], 
      [
        "realistic", 
        13.91304347826087
      ], 
      [
        "truly", 
        13.91304347826087
      ], 
      [
        "actors", 
        12.17391304347826
      ], 
      [
        "part", 
        12.17391304347826
      ], 
      [
        "like", 
        12.17391304347826
      ], 
      [
        "genre", 
        12.17391304347826
      ], 
      [
        "characters", 
        12.17391304347826
      ], 
      [
        "camera", 
        12.17391304347826
      ], 
      [
        "though", 
        10.434782608695652
      ], 
      [
        "ever", 
        10.434782608695652
      ]
    ]
  }
]
```

### Display Sentiment Ratio of a Movie's Reviews
**URL** : `/reviewlists/sentiment/count`


**Params** : 
| Type        | Name           |
| ------------- |:-------------:|
| `string`    | `movie_id` |
| `OPTIONAL string`    | `keyword` |


**Method** : `GET`

**Response** :
```python
[
  {
    "name": "Positive", 
    "value": 13
  }, 
  {
    "name": "Negative", 
    "value": 67
  }
]
```

### Display Keywords of a Movie's Reviews
**URL** : `/reviewlists/keywords`


**Params** : 
| Type        | Name           |
| ------------- |:-------------:|
| `string`    | `movie_id` |
| `OPTIONAL string`    | `sentiment` |


**Method** : `GET`

**Response** :
```python
[
  [
    "horror", 
    54.909090909090914
  ], 
  [
    "like", 
    40.72727272727273
  ], 
  [
    "footage", 
    40.36363636363637
  ], 
  [
    "found", 
    39.27272727272727
  ], 
  [
    "woods", 
    37.81818181818182
  ], 
  [
    "time", 
    31.636363636363637
  ], 
  [
    "scary", 
    28.727272727272727
  ], 
  [
    "people", 
    25.81818181818182
  ], 
  [
    "good", 
    23.636363636363637
  ], 
  [
    "first", 
    22.181818181818183
  ], 
  [
    "camera", 
    22.181818181818183
  ], 
  [
    "characters", 
    18.90909090909091
  ], 
  [
    "never", 
    18.181818181818183
  ], 
  [
    "story", 
    17.81818181818182
  ], 
  [
    "heather", 
    17.81818181818182
  ], 
  [
    "real", 
    17.09090909090909
  ], 
  [
    "nothing", 
    15.272727272727273
  ], 
  [
    "fear", 
    14.90909090909091
  ], 
  [
    "feel", 
    14.90909090909091
  ], 
  [
    "documentary", 
    14.90909090909091
  ]
]
```

### Display All Reviews for a Movie Sharing a Keyword
**URL** : `/reviewlists/keymatch`


**Params** : 
| Type        | Name           |
| ------------- |:-------------:|
| `string`    | `movie_id` |
| `int`    | `page` |
| `string`    | `keyword` |


**Method** : `GET`

**Response** :
```python
[
  {
    "date": "3 September 2011", 
    "name": "jbowslee", 
    "review": "This movie scared the heck out of me. What surprises me is that people I know who are scared watching any horror film thought this movie was boring. I believe a wild imagination is necessary to truly get this film. What scared me about this movie is what my imagination was doing every step of the way. What was happening while they were sleeping? What was happening when they heard screaming of their friend when he went missing? What was making those banging noises and why? Because this film does not show anything horrific, it is up to the viewer to fill in the missing spaces and this is what frightened me. I am sure what was going on in my mind could not have been portrayed in a film and still received an 'R' rating. The unknown and what could be happening is what made this film frightening. And the true horror in the eyes and voices of the filmmakers in this film more than reinforced my worst fears. Overall, this film did something that has not happened to me since I was about 10 years old. It made me afraid of the dark and of the strange noises in nature that we hear every day.", 
    "review_id": "rw2483607", 
    "sentiment": -0.013090005161243208, 
    "title": "Imagination is key"
  }, 
  {
    "date": "8 July 2020", 
    "name": "nashw82", 
    "review": "Love it or hate it you have to admit it changed the horror movie landscape and introduced a new sub genre and style of film making. Without the success of Blair Witch you wouldn't have series like Paranormal Activity and other found footage flicks. As far as the movie goes, I watched it with little prior knowledge and while it was definitely a slow and shakily shot it managed to ratchet up the fear and intensity with simple but effective methods and annoying though fitting acting. Each night they spent in the forest added to the tension as you wondered what they would encounter next. The abrupt and frightening ending was suitable for a found footage film and it left me with a fear of people quietly facing walls without responding haha.So, however you feel about it, you can't deny that its left its mark on the horror movie landscape.", 
    "review_id": "rw5890666", 
    "sentiment": -0.005114608643360498, 
    "title": "Brilliant but Divisive."
  }, 
  {
    "date": "20 December 2008", 
    "name": "diegoavilarodriguez", 
    "review": "OK, I have to be honest here, I saw this movie when I was 6 years old and later on watched it again to remember what was so bad about this movie... and now I remember why I hate this movie so much. First the bad things on this movie, this movie is so low budget that the whole documentary-like style of the camera had to obligatory cause they couldn't afford any camera men(though that style did change the world of movie making). Next, the plot, wow lost in the woods how original, that was seen in Friday the 13th so the whole lost in the woods things isn't so original, now the reason why they are lost in the woods was original but worst part of this film is the fact that it builds suspense for nothing(like the scene when they ran out of the tent, screaming and scared, suspenseful but not scary cause you don't even know what they running from.)For all I care it could be Bigfoot attacking them. Now the main thing people say about why this movie was so great was because they claim that the movie activates their 'imagination', and I think that means that this movie leaves out so many unanswered questions that to them it's fun to fill in the blanks, of course not like the movie disappearance in which they leave out so many blanks it makes the movie awful, well that wasn't the case with the Blair witch project, but still even if it is fun to fill in the blanks with this film that is no excuse for the people who don't like to fill in the blanks, so to me it sounds like people like this movie because it basically wastes their time. And now we come to the center question of this film which is: Why did they not show the witch?! Now if they had shown the witch, I would just recommend you rent this movie but no, this movie is like a nightmare on elm street without Freddy Krueger, you wait around for something to happen, and when they finally come the ending the idiot chick drops the camera which honestly is a disappointment, you expect something creepy and all that, when nothing really happens at all, and really if a 6 year old doesn't get scared watching this film how can an entire nation get scared over some movie which is nothing more than a publicity stunt to gain quick cash. Alright, now though the whole movie was a waste of time there is the upside of the fact that this movie did have an original storyline and did have the potential to be a horror classic, but of course it was not a true horror classic, now this movie is like the Hulk which was a good idea pretty much screwed up so this film needs a remake seriously and it needs it right now.", 
    "review_id": "rw1993007", 
    "sentiment": -0.0358037916210845, 
    "title": "this movie needs a remake... BADLY!!!!"
  }, 
  {
    "date": "21 February 2016", 
    "name": "eric262003", 
    "review": "In the 1999 horror classic 'The Blair Witch Project', we see three aspiring young filmmakers in 1994 set out on journey to do a documentary project based on a mysterious urban legend of the Blair Witch, who resides in a forest outside of a small town in Maryland. At first we're given the impression that this film was based off of their raw footage. The research going into the documentary is pretty shoddy in execution. The camera is purely out of focus and plus that Heather (Heather Donahue) repetitively utilizes 'u-huhs and yeahs' when she's asking questions towards the residents in the area. The opening scenes will surely make you gnash your teeth in annoyance. In fact this whole movie within a movie can be contrived at times. But once the young students enter the woods in search of the Blair Witch, the annoyance becomes more paranoiac as the fears and the anxieties start to send chills down our spines. Fortunately, the real filmmakers (Daniel Myrick and Eduardo Sanchez) were not as inept as the student filmmakers. We get some believable settings as the determined crew makes their way into the Maryland forests, where they are lost and the more trapped they are in the labyrinth of tress and shrubs, the more the adrenaline level goes up rapidly as the fears and paranoia become overwhelming. The daytime scenes start off quite equivocal as just the sounds of twigs from tree or on the ground snap can surely garner scares where expect the unexpected becomes focal in our minds as much as theirs. The rock piles that bear a resemblance of grave markers epitomizes a sense of unsettling tension of the students as though their eyes are playing tricks on them. These supernatural elements that the threesome face would likely drive anyone insane. The daytime fears seem pretty tame at first because the paranormal activity doesn't generate as much fear as the gang might shed some hope of finding their ways out of the woods, if they could trace back to where they begun their journey. When night comes and when things go bump in the night, the fear factor really gets the boost. The strange sounds nearby can be chillingly frightful and our brave but naive, unequipped students can do nothing but stick together. But nightfall the horror party finally gets tense and the audience watching this can feel this level of fear that anyone sneaking up behind them in the theaters can get someone a cardiac arrest. The forest is black, the theater is dark, everything is painted black during these scenes. The main prop in this movie is the cheap first-person camcorder which eventually becomes a character in itself as we become a part of this movie courtesy of the camera as well as the terror the gang faces it lingers on us as well as we feel convinced that there might be a Blair Witch lurking in these forests. These camera traits show adults that it is normal that human beings are scared of the dark and nothing shameful about that. The lack of preparation when entering the woods, the students have been faced in a sort of predicament they can't seem to get out of and the more they struggle the worst it gets. When Heather the booger- dripping leader of the team she confesses that it was her stubborn ways and determination to finding the truth she begs her cohorts Josh and Michael for forgiveness, we actually feel for her without the audience feeling manipulated.'The Blair Witch Project' is utilized as a staple on why we're obligated to watch and let alone produce films. When the students start to get restless, hungry and feared, Heather decides that now's the time to close the camera. Finally, the more restrained Joshua takes her camera and retaliates by pointing it back at her and shouting back at her as though, the camera rules her life while it affects the other two characters caught in the middle of the mess she put them in. In some ways this movie helped spawn shows like 'Ghost Hunters' and 'Ghost Adventures' where paranormal experts go around the world in seek of the truth in that there is life beyond our mortal lives.", 
    "review_id": "rw3419452", 
    "sentiment": -0.006245479921376352, 
    "title": "A Horror Film Where Fear is The Real Monster"
  }, 
  {
    "date": "23 September 2011", 
    "name": "itamarscomix", 
    "review": "The Blair Witch Project is an interesting mockumentary with an intriguing concept, that was the victim of many bad decisions, in the process of making it and especially of promoting it. The ambition, it seems, was to create an experimental art-house film that would appeal to mainstream audiences, and by marketing it as a 'horror' movie, create surprise and buzz. The attempt to bridge the gap between the two viewer groups was quite positive, but what it actually achieved is alienating both: the horror crowd was disappointed and annoyed, especially younger viewers who sneaked into an R rated movie expecting gore and heads-on horror; and the more sophisticated, avant garde crowd, turned off from day one by the film's promotion, didn't even bother to go see it.A decade later, it's easier to put all that aside, as well as the internet-based hype generated by the producers at the time. The film can now be appraised as what it is, an exercise in experimental filmmaking, and an interesting one at that. It takes a lesson from the true great classics of horror - in that the fear of the unknown, the anxiety and anticipation of violence are much more effective than explicit violence in itself - and indeed, it's scarier than almost any horror movie created in the last twenty years, although the teenagers who usually go for that kind of movie will probably disagree. The Blair Witch Project creates tension and anxiety, and draws the viewer into the characters' world. And it doesn't matter one bit whether or not you think it might be real - in fact it's more impressive when you know that it's not.Unfortunately, it doesn't achieve true greatness in that respect either. In its attempt to bridge between mainstream horror and experimental indie movie-making, the film reaches a sort of middle ground that isn't quite here nor there, not quite satisfying anybody. The Blair Witch Project is not a classic or a great film, nor will it ever be, but it should be watched by fans of independent and experimental cinema and of classic horror, and remembered as a brave and innovative experiment that didn't quite make it.", 
    "review_id": "rw2492527", 
    "sentiment": -0.0027683637053605424, 
    "title": "Mis-marketing in action"
  }, 
  {
    "date": "10 July 2020", 
    "name": "gardnernrg", 
    "review": "I'll start off by saying this. In no regards is this film bad. Absolutely not. This is a good film that still lives up to its hype, 21 years after release. It is a classic in the horror genre, that every horror fan needs to watch.That being said, this isn't a perfect film either. Many times throughout the film I found myself dozing off, as there wasn't much happening, and it wasn't integral to the storyline/plot. And while I'll rip on the found footage style right now, I'll praise it in a second. The sudden jumps in footage as the characters stopped recording and then resumed can be terribly confusing. I found myself once or twice chasing my tail trying to figure out what just happened. These are most of the bad things, and of course there are others, but these are the things that made me rate it 6.Now for the good things. Estimated $60,000. For instance, Jordan Peele's 'Us' has an overall rating .4 higher than this. The budget for that? Estimated $20mil. For $60k this movie does so much! It delivers such an amazing performance for the little budget it had. Now, I said I'd get to the found footage style. I already ripped on that, now to praise. Coincidentally, they are kind of the same thing. The found footage style, where I found myself chasing my tail, was an incredible way t deliver this story. Earlier on, the characters are sane and have their wits about them. The storyline is clean and precise. Slowly as the movie progresses more and more sudden and big cuts/jumps come along, and almost simulate what the characters were feeling in that moment. For what this film promises, it delivers. A college film student documentary. Not professional acting, editing, shooting, etc. This film does what it says and does it in a great way. Has its flaws, but a good horror film nonetheless.", 
    "review_id": "rw5895781", 
    "sentiment": -0.005718680334146557, 
    "title": "The Blair Witch Project?"
  }, 
  {
    "date": "7 October 2011", 
    "name": "LuvzHorror", 
    "review": "As a major fan of the horror genre I heard about The Blair Witch project and simply HAD to go and see it! Thinking of myself as a hardened horror buff I was pretty sure that I'd enjoy every second, and I did, but I was terrified! The fact that I was heavily pregnant and had to return home to an empty house as my husband was working away should have been a deterrent, but I thought I'd be fine!My sister (who loathes horror movies with a passion) had seen Blair Witch the night before and said she was disappointed in it. She said it was over-hyped and simply not frightening. How wrong she was!The film starts with 3 student film makers, Heather, Josh and Mike, heading to Burketsville to make a documentary about the legend of The Blair Witch. They visit various sites of interest, speak to local people and hear the story of Rustin Parr. Parr was a local man who kidnapped, tortured and murdered 7 local children in the 40's. During his trial Parr claimed that he was possessed by the spirit of Elly Kedward, a woman burnt as a witch in the town of Blair. Burketsville was formerly known as Blair.The trio then head out into The Black Woods. They visit Coffin Rock, the site of the murder of 5 men. As the film progresses the students move further into the woods. Inevitably they become lost. What follows still scares me to this day. As fear takes over the sensibilities of the trio they begin to fight and argue with each other. Then, when night falls, strange happenings occur. Children are heard laughing, strange objects are left outside the tents. The students slowly descend into absolute terror. To go any further would mean including spoilers, which I always hate in a review. Needless to say the frustration of the students is passed on to the viewer. Shaky camera-work (this film being one of the first 'handheld camera' movies) only adds to the fear as we are unable to see what it is that is terrifying the students.I watched this film on the edge of my seat. On my return home I was physically afraid to be alone. I actually ended up staying the night at my parent's house! That's not to say that everyone will be afraid, judging by some of these reviews I think I must be an absolute coward for being scared by a film that some people have claimed made them fall asleep!But I will leave this review by saying one thing:I went into labour the next day - 3 weeks early!", 
    "review_id": "rw2499456", 
    "sentiment": -0.00798370360894845, 
    "title": "Unnerving!"
  }, 
  {
    "date": "25 October 2020", 
    "name": "uonlywish500", 
    "review": "I can understand that some like it, but for me this movie is just flat ... They say that knowing next to nothing reinforces the horror of the movie, but I disagree! I agree that we cannot explain everything orally, but there is a limit!It's flat, it's not scary, the characters are not really endearing and therefore, we are not invested in the film, and every thing that happens to them left me unmoved, I almost didn't care.The final scene, for example, did absolutely nothing to me.I still want to say that there are some good ideas, like the idea of dolls that really freaked me out, but it stops there! They do nothing of this story, it was useless!It's a pity, but I don't like this movie. It is at the best just bad, if not really bad.", 
    "review_id": "rw6204504", 
    "sentiment": -0.03617342995137113, 
    "title": "How to say it like that...?"
  }, 
  {
    "date": "26 October 2020", 
    "name": "kmezdi", 
    "review": "I didn't rate it after I watched it because I didn't know what to make of it. But after some time, or the day after, that's when I started feeling agitated. I kept looking at my back and whatnot. Which is unusual for me. Maybe it's the thought of the unknown that made this movie a popular horror.I liked the pace and the scene where the girl didn't want to blink, that was a good bit. Though the characters' ways on how to deal with a situation is mindless and it made me laugh.", 
    "review_id": "rw6207510", 
    "sentiment": -0.006518403178194256, 
    "title": "Different."
  }, 
  {
    "date": "11 September 2020", 
    "name": "tchitouniaram", 
    "review": "Considering,that there are almost no horrors,that I didn't watch)))the Blair witch remains the favorite,timeless and respected film ever!The minimalist style,with tiny budget,but enormous talent,makes it a wonder movie,for me!The creators masterfully play on basic human fears:unknown,getting lost,darkness and night forest.Without any special effects,gore and jump scares,it still remains one of the scariest horrors ever made.Just absolutely love it!", 
    "review_id": "rw6085122", 
    "sentiment": 0.009920469615892972, 
    "title": "One and only!"
  }, 
  {
    "date": "16 October 2013", 
    "name": "RecceR", 
    "review": "Three film students visit a small rural town in Maryland in order to make a documentary about its dark history. Things begin going wrong once they are in the woods and gradually become a living nightmare that unfolds from their point of view. The Blair Witch Project is one of the most effectively creepy and scary horror movies of our time. The situations, the people and the acting all seem so real and help create this fictional legend. Because there is pretty much a complete lack of visuals (that most modern movies use as a crutch) and the audience must rely on the reactions from the cast makes this pure genius. Of course, it wouldn't have worked had the actors failed in their performances. But that was definitely not the case with this film. I have only seen it a few times, but nearly every moment sticks with me because The Blair Witch Project is such an unnerving and haunting film.", 
    "review_id": "rw2888312", 
    "sentiment": 0.0034899923978285513, 
    "title": "unnerving and haunting film"
  }, 
  {
    "date": "28 October 2013", 
    "name": "horrorflicklover", 
    "review": "Maybe I don't get the critics of this movie. I think we can all agree that by the late 1980's, the horror genre was beaten to death. Scream eventually came along in the mid-90's and gave it the shot in the arm that it needed. However, soon after the genre was flooded again with much lesser films cashing in on Scream's success. So what was the Blair Witch Project? A very different horror film indeed. While not the first of the found footage genre, it made a much larger impact than previous movies of the sub-genre had. And like Scream before it, it gave something fresh and original to the horror film scene. Isn't that what we wanted all along? By 1990, slasher flicks were a dime a dozen. Same in 1999 with the films that followed Scream. Blair Witch went in to an entirely different direction. Sure, it was proposed before Scream (and filmed the following year of it's release), however, it came at a great time. Just as horror movies were yet again becoming tired parodies of themselves. I don't even know why we need to put spoilers, seeing as just about everyone whose heard of the film knows how it ends. But know this: If you're expecting a bogeyman to jump out at you, then you'll be disappointed. If that's what you must have in a horror film, then keep going. Blair Witch operates largely on the elements of intrigue and suspense. Suspense, intrigue, both important elements to any great horror film (like Halloween). But unlike many of these films, there is no bogeyman on screen. Everything is left open to interpretation, with the general idea being the same. You clearly see these things happen in Blair Witch, but you have no real idea why they're happening, or who's responsible. You're not given an answer, you're not given violence and gore, you're not given big, on-screen effects, you never even see the antagonist's face. But you are given clues, ways to connect the dots.But THAT is just what made this film great. It was a solid, original idea that was executed remarkably. It didn't follow a typical formula, but why should that matter? If this film couldn't be enjoyed for what it was, then it's not the fault of the film. Because it's simply not a bad movie. To dislike it because it wasn't well-written, executed, or interesting, I can understand. But if that's what you think, then are we even talking about the same film here?It doesn't have the typical ending, or the typical 'bad guy jumps out at you' moment. But it's a sure horror thriller, and the rhyme and reason is all made obvious if you've paid attention throughout.The Blair Witch Project is a classic. A movie that laid the groundwork for mainstream acceptance of it's sub-genre, and became a masterpiece of it's main genre in it's own right. This is a must-see for any horror fan.", 
    "review_id": "rw2895873", 
    "sentiment": -0.011031329217610708, 
    "title": "Unique, Intriguing, Suspenseful"
  }, 
  {
    "date": "17 May 2020", 
    "name": "mathieulaurent", 
    "review": "It's a slow horror flick. Absolutely not scary....until the last minutes. Only the end is quite worthy.", 
    "review_id": "rw5746732", 
    "sentiment": -0.04010593211083551, 
    "title": "Boring as hell !"
  }, 
  {
    "date": "31 October 2013", 
    "name": "nimstic", 
    "review": "This movie is serious business, very frightening experience to say the least. Since I am someone who always wanted to make a documentary of my own, I could relate to it more but I am pretty sure, all of us film ourselves during such expeditions these days. The film triumphs in two areas. One in consuming your entire attention span to travel with these three characters, the other in presenting it to you in a more believable, frightening manner (pieced through amateur footage) This movie is an influential work because it then spawned a slew of similarly made movies (although Cannibal Holocaust was made earlier, this seemed more real and entertaining to this day and age). I thoroughly enjoyed the horror aspect of this movie, and I am not someone who finds horror movies very shaking (Except for The Exorcist, of course) but this was quite scary. I felt mind- numbing frustration in situations when the main characters' spirit & tolerance started to decline, and slowly begin to realize how meek, insignificant we are if we are not part of our society or within our comfort zone or left it the dark with an unknown fear factor, with very crazy things happening around you but you can't see or tell what it is. The makers manage to infuse terror in a very natural way too, that's the main success feature of the film. I feel sorry for some viewers in this forum who couldn't enjoy the film because they were trying to make 'sense' out of the characters shooting such frightening situations, calling it unrealistic etc. Probably why IMDb has a low rating for this movie too. It never bothered me, my suggestion is either you don't notice it/disregard it OR you look at film as their passion, or something humans can do in hopeless situations (ie, if I know my fate is sealed in such a terrifying situation, I would consider filming myself so that the world gets to know what happened to me someday, now that I can't save myself anymore). Watch the early interviews with locals carefully (real people) for you to understand the ending very well. Excellent movie. Definitely goes down as one of my all favourites. Cannot think of a major flaw.", 
    "review_id": "rw2897329", 
    "sentiment": -0.0014512128430482086, 
    "title": "One of the most frightening films ever"
  }, 
  {
    "date": "30 October 2020", 
    "name": "Habibi-Universe", 
    "review": "Well... that was rather unsatisfying.'The Blair Witch Project' (1999) was directed by Daniel Myrick and Eduardo S\u00e1nchez and it is about three film students vanishing after traveling into a Maryland forest to film a documentary on the local 'Blair Witch' legend, leaving only their footage behind. This film basically started the whole 'found footage' trend or at least popularized it as far as I know!How is this film? First of all, what was really striking to me, was that the film's runtime is only about 80 minutes which is very short for a feature film. Having said that, I would have probably cut the film down to about an hour to make it a bit fresher and tighter!A majority of this film takes place in the forest. I think it is very relatable that being in the forest while it's completely dark is a pretty scary and unsettling thought.One thing that I definitely need to commend this film for, is that the characters are very well written.Here we have a bunch of youngsters trying to make the next big thing happen, very quickly realize that they got themselves into a situation that they did not anticipate and therefore don't know how to deal with!If you think that there are not those kind of people out there, then you have way too much faith in the human race!My big problem with this film is that, even though it is pretty entertaining, it is such an incredibly slow burn without anything really happening!This film lacks substance!In my opinion this horror picture doesn't do anything ground-breaking that I can appreciate. As far as the found footage usage is concerned, I can at least say that it makes the best possible use out of that specific film technique, a technique that I am generally speaking not a fan of.Overall, 'The Blair Witch Project' (1999) is a horror film that only fans of that particular style will gravitate towards!", 
    "review_id": "rw6219347", 
    "sentiment": -0.014398695153868523, 
    "title": "Do you believe in the 'Blair Witch'?"
  }, 
  {
    "date": "4 November 2013", 
    "name": "alexcomputerkid", 
    "review": "'In October 1994, three film student filmmakers disappeared in the woods near Burkittsville, Maryland while shooting a documentary....' 'A year later their footage was found' This great quote in short tells the details of the Blair Witch plot. It is a plot that like most horror films can be questioned. How can the woods be the only setting? What is the purpose to this? Could it really work with only three cast members? Taking this all together, still The Blair Witch Project is something we could never have experienced or predicted what it was going to be.By using a small budget of only $20,000 to $25,000 aside from the opening shots, The Blair Witch Project is set only in the woods. The setting of the woods helps this film break the norm for horror movies. The woods here have a strange eerie feel, and is very original. You have the feeling along with characters of never getting out and no doubt it will you make at wilderness quite differently.With the small budget, the film only needs three cast members. Heather (Heather Donahue) is the only girl of the group and really emerges as the leader as they try to get out of the woods. Mike (Michael Williams) is a character who becomes very creepy once the harmful effects in the woods prey on him. Josh (Joshua Leonard) is the quiet member of the group in this bad situation. The cast really works due to the good acting by actors who are unknowns who we don't recognize making it realistic.After a plot and story that seems like it can't get much better, the ending is one that REALLY can't much better. The ending comes out of nowhere as again it is in the woods and in a place that seems like it's in the middle of nowhere. It is a heart-pounding and very scary ending. The final shot is very clever as there are different possible theories raised about what just happened. This is one of the best endings in movie history, no doubt.The Blair Witch Project is not normal horror. It is horror that goes way above the normal common ground and makes it's own mark on the movie world. We know we are going to get good horror films in the years to come but The Blair Witch Project will always be beside those at the top.", 
    "review_id": "rw2899766", 
    "sentiment": -0.012101583294743257, 
    "title": "We know we are going to get good horror films in the years to come but The Blair Witch Project will always be beside those at the top"
  }, 
  {
    "date": "31 October 2020", 
    "name": "repojack", 
    "review": "The trailblazer of found footage , viral marketing, and shoe-string budget horror, Blair Witch deserves a place in the 'Horror House of Fame.' That doesn't make it a great movie. While there are some very spooky scenes, it meanders a lot, both literally (nausea inducing shaky cameras) and figuratively.", 
    "review_id": "rw6220772", 
    "sentiment": -0.029118499543438602, 
    "title": "Slower than you'd expect for the buzz it gets"
  }, 
  {
    "date": "31 October 2020", 
    "name": "curtish2809", 
    "review": "Where the genre (horror found footage) began! This movie proves that you don't need gore to be scared! Our imaginations can be much worse than what we see. Definitely an enjoyable movie!", 
    "review_id": "rw6221714", 
    "sentiment": -0.011835370213175536, 
    "title": "The original found footage horror film"
  }, 
  {
    "date": "1 November 2020", 
    "name": "MadMark96", 
    "review": "Blair Witch project is one of the better made found footage horror movies. As someone who grew up watching 90s home video movies such as CKY, Jackass, or the Pantera home videos; I found this movie just felt like one of those which was a great thing. The acting is the films strong suit for sure, the characters actually feel like real people and it feels like you're watching something that might've actually happened. Even the interviews of 'town residents' in the beginning feel like you're listening to real interviews of real people. Very nicely done. The movie is structured like a documentary so it's not all that eventful. The atmosphere of the movie is very well done and you're on edge for a while. Apart from one or two scenes there wasn't anything too chilling or crazy, so don't expect some super gory and deeply disturbing horror movie with a riveting plot. The ending is probably the weakest part of the film. Without spoiling anything, the movie just ends very abruptly. It makes you go 'thats it?'. If the movie was about 10-20 minutes longer it would've been a lot better, however I suppose that is kind of the point since it's a found footage movie. Overall a good watch, I'd recommend it but it's probably not something you're gonna want to re-watch.", 
    "review_id": "rw6227453", 
    "sentiment": -0.007259303430048676, 
    "title": "One of the better found footage movies."
  }, 
  {
    "date": "21 April 2016", 
    "name": "sierrabonny", 
    "review": "The Blair Witch Project follows three teens (Heather, Mike, and Josh) as they trek out into the woods to do research behind the legend of the Blair Witch. They begin by interviewing several of the folks that live in the town near the woods, and almost everybody knows something about this witch. With the creepy tales of the witch swimming in their minds, they venture into the woods for what is meant to be just a three day camp out to shoot some scenes in the home of the 'fictional' witch. Once they enter the woods things start declining from there. The first problem is that the circle- walking begins. Classic in any 'woodsy' horror film. Because of the bewitchment of the woods, Heather, Mike, and Josh become hopelessly lost wandering in circles. While things definitely do get worse for them, the circle wandering is a very large chunk of the film. After they become lost in the woods, the film really has only 2 elements to it: wandering in hopeless circles in the woods, and listening to sticks crack at night. Are both of those things scary? Yes of course! Scary for an audience to watch for an hour and forty-five minutes? You can answer that for yourself. After they become lost in the woods, they begin to hear many strange noises and find mysterious, unexplained symbols placed all around them. Slowly the characters are forced to come to the realization that they aren't just lost. They are hunted. Josh is the first of them to disappear, then suddenly Heather and Mike are left alone to walk in circles and listen to sticks crack. Oh no! The film comes to what could be called a climax in the last five minutes when Heather and Mike venture out to find Josh, for the third time, and they are lead to an old abandoned house. Once inside, they follow his screams, and wind up in a basement where the film ends as you see Mike standing in the corner of the room. The camera goes black. After at least fifteen minutes of pure running, screaming and chasing, that is the end it comes to. Everyone dies. But are we really surprised?", 
    "review_id": "rw3455641", 
    "sentiment": -0.019750366717841753, 
    "title": "The 'Bored' Witch Project"
  }, 
  {
    "Review Tokens": [
      [
        "horror", 
        48.78048780487805
      ], 
      [
        "woods", 
        24.390243902439025
      ], 
      [
        "like", 
        21.46341463414634
      ], 
      [
        "found", 
        18.536585365853657
      ], 
      [
        "footage", 
        18.536585365853657
      ], 
      [
        "characters", 
        13.658536585365853
      ], 
      [
        "people", 
        11.707317073170731
      ], 
      [
        "things", 
        11.707317073170731
      ], 
      [
        "know", 
        10.73170731707317
      ], 
      [
        "camera", 
        10.73170731707317
      ], 
      [
        "heather", 
        10.73170731707317
      ], 
      [
        "fear", 
        9.75609756097561
      ], 
      [
        "bad", 
        9.75609756097561
      ], 
      [
        "great", 
        9.75609756097561
      ], 
      [
        "good", 
        9.75609756097561
      ], 
      [
        "students", 
        9.75609756097561
      ], 
      [
        "real", 
        9.75609756097561
      ], 
      [
        "scared", 
        8.78048780487805
      ], 
      [
        "lost", 
        8.78048780487805
      ], 
      [
        "documentary", 
        8.78048780487805
      ]
    ]
  }
]
```

## Users

### Retrieve User
**URL** : `/users`


**Params** : 
| Type        | Name           |
| ------------- |:-------------:|
| `string`    | `name` |

**Method** : `GET`

**Response** :
```python
[
  {
    "movie": "Halloween III: Season of the Witch (1982)", 
    "rating": 4, 
    "review": "Makes some really wild leaps in logic, including the main character being inexplicably popular with the ladies. Really campy and not even in a good way.", 
    "review_date": "3 May 2020", 
    "review_id": "'rw5704572'", 
    "review_summary": "Ridiculous", 
    "sentiment": -0.021672029285479743
  }, 
  {
    "movie": "Rootwood (2018)", 
    "rating": 2, 
    "review": "Everything about this movie is bad. The writing is bad, the acting is bad, and the plot is bad.", 
    "review_date": "9 December 2019", 
    "review_id": "'rw5309295'", 
    "review_summary": "Utterly bad", 
    "sentiment": -0.14616203277558384
  }, 
  {
    "movie": "Near Dark (1987)", 
    "rating": 3, 
    "review": "Utter lack of chemistry between the male and female lead and really unbelievable relationship, made even worse by bad acting. Their scenes were painful and tedious. The vampires are not cool at all and seem to have a mediocre way of staying alive, which is strange since they've been at it for awhile. There wasn't much to their back stories. Many aspects about them were illogical as well.", 
    "review_date": "5 May 2020", 
    "review_id": "'rw5711941'", 
    "review_summary": "Painful and illogical", 
    "sentiment": -0.0523169732004904
  }, 
  {
    "movie": "Sonic the Hedgehog (2020)", 
    "rating": 4, 
    "review": "Sonic was just written as really annoying and unlikeable, and also a bad example for children. Many plot holes as well.", 
    "review_date": "8 March 2020", 
    "review_id": "'rw5534119'", 
    "review_summary": "Unlikeable Sonic", 
    "sentiment": -0.04979142885442971
  }, 
  {
    "movie": "Lake of Death (2019)", 
    "rating": 4, 
    "review": "Slow and trying too hard to be artistic. Characters are bland. A painful watch.", 
    "review_date": "17 July 2020", 
    "review_id": "'rw5911455'", 
    "review_summary": "Bland, bleak, boring", 
    "sentiment": -0.06317726248406004
  }, 
  {
    "movie": "Patient Seven (2016)", 
    "rating": 5, 
    "review": "Pretty well produced and entertaining stories. Two of the stories had a similar theme and I thought that was unnecessary, but otherwise it was an interesting anthology movie.", 
    "review_date": "14 March 2020", 
    "review_id": "'rw5549244'", 
    "review_summary": "Fairly entertaining watch!", 
    "sentiment": 0.00034978890676455685
  }, 
  {
    "movie": "Bram Stoker\"s Dracula (1992)", 
    "rating": 3, 
    "review": "Horribly over-acted, ridiculously cheesy events, just a wild ride of campiness through and through.", 
    "review_date": "15 March 2020", 
    "review_id": "'rw5551476'", 
    "review_summary": "Epitome of cheesiness", 
    "sentiment": -0.039548793135471993
  }, 
  {
    "movie": "The Conspiracy (2012)", 
    "rating": 6, 
    "review": "This stands out from the pool of found footage movies because it is pretty well made in terms of production quality, has an interesting plot, and is just unique in its premise. Not a bad watch for sure.", 
    "review_date": "16 March 2020", 
    "review_id": "'rw5554283'", 
    "review_summary": "Different and well made", 
    "sentiment": -0.019718860036688424
  }, 
  {
    "movie": "Amityville II: The Possession (1982)", 
    "rating": 3, 
    "review": "The acting here is just horrible, like they were all in a school play or something. Loose plot that was not very compelling, and very draggy ending. The soundtrack was great though.", 
    "review_date": "17 March 2020", 
    "review_id": "'rw5556483'", 
    "review_summary": "Horrible acting, draggy ending", 
    "sentiment": -0.03032616067114405
  }, 
  {
    "movie": "Errementari (2017)", 
    "rating": 8, 
    "review": "Rich story with great characters and a good sense of humor.", 
    "review_date": "17 March 2020", 
    "review_id": "'rw5558486'", 
    "review_summary": "Imaginative and fun", 
    "sentiment": 0.02695019674445464
  }, 
  {
    "movie": "The Ranger (2018)", 
    "rating": 6, 
    "review": "I disagree with the other reviews about this being a humdrum slasher. It had many elements that made it an entertaining and different watch for me. Definitely not a cinematic masterpiece, but I believe it stands out from films in the similar genre that have a similar budget.", 
    "review_date": "18 March 2020", 
    "review_id": "'rw5560473'", 
    "review_summary": "Has character", 
    "sentiment": 0.017929980643435157
  }, 
  {
    "movie": "Itsy Bitsy (II) (2019)", 
    "rating": 3, 
    "review": "I thought the concept and the first half of the movie as the plot developed was okay. It was still pretty interesting. However, the effects are really bad, so the spider looks like a halloween decoration. The acting is bad and none of the characters are likeable.", 
    "review_date": "4 September 2019", 
    "review_id": "'rw5098729'", 
    "review_summary": "Had promise but nothing else", 
    "sentiment": -0.04804685189387822
  }, 
  {
    "movie": "The Banana Splits Movie (2019)", 
    "rating": 2, 
    "review": "This could have been good. I thought it was an amusing concept and it developed okay. However, it quickly went from a 5 to a 2 right around the middle of the movie. There is no semblance of logic in the creatures' behavior and the victims' reactions.", 
    "review_date": "5 September 2019", 
    "review_id": "'rw5100658'", 
    "review_summary": "Awfully written", 
    "sentiment": -0.04474311544837168
  }
]
```
