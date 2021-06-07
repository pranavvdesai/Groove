## Groove
# Aim
To create a carpooling service which matches people on the basis of their interests, and personality types. 
# Introduction
With the depreciation of air quality index in the major metropolitan cities in our country, the need for reduction in vehicular emissions is ever expanding. To cater to this demand we already have a versatile solution i.e ‘carpooling’ present. But if we look at the statistics, what we find is that people are reluctant towards the idea of sharing a ride with some stranger.
The main reasons why people are hesitant towards carpooling are:

1) Awkwardness with a stranger
2) Security
3) Longer waiting time.

Our project strips out all of that complexity from the process and provides a match based upon similar interests and personality traits in a user friendly interface.
# Solution Proposed
The project aims at destroying this barrier between the people who are sharing a ride by grouping up people with shared interests and compatible personality types into a pool.

We are able to achieve such results with the help of techniques like Natural Language Processing (To determine someone’s personality type) , Collaborative filtering and decision tree classification (For grouping people with similar tastes) .
# Tech Stack
Python (for Natural Language Processing and ML) 
Flask (Web backend)
HTML + CSS (Web frontend)
MYSQL(Database)
Heroku (Deployment)
# Implementation
Firstly while registering, the user will have to answer a short questionnaire  which will help us identify their interests.

After the registration is complete they can ‘Join the pool’ and use our service to find compatible people to commute with.

Users may select:-
1) Gender Preference
2) Pool Size






Once a user joins a pool and selects the pool size, the underlying machine learning algorithms does the following:

We first group people having nearby pickups, and having destinations in the same directions, find distance to be travelled and time required.
We then determine their personality by analyzing their twitter and create clusters of compatible people.

Then inside these clusters, we group people with most similar interests. 

Now we just group the N people with the maximum Compatibility index together. (Here N is the pool
size, and it is inclusive of the user)  

After the pool is chosen, A message containing details of the pool members is sent to each all, allowing them to coordinate between themselves and book a ride to their best convenience.

# Map system
During the drive we will be providing the users with details such as,

1)Estimated arrival time
2)Distance left
3)An interactive map interface
# Flagging system
We provide the users with the ability to report a user in case a user displays offensive behaviour. Each time a user is reported, they garner a flag depending on the severity of the situation and proportional action will be taken.

The security of our customers is of utmost importance to us, hence offensive behaviour will be dealt with extreme promptness. 
# Connect with your poolmates
At the end of each ride we will be asking the users to rate their poolmates and whether they’d like to share their socials and convey the respective information.
# Future Scope
1) Moderators:  We would be adding moderators to our service who will oversee all the security related issues. Normal people can voluntarily become moderators by staking a particular amount of money beforehand.
Moderators would be provided with extra benefits and rewards.

2) Better Pooling: We’ll be adding layers to our deep learning model and refining features to obtain a substantial betterment in results while matching users.

3) Choice of cab service: In the future we’d like to have a cab service of our own rather than having to redirect users to external cab service providers. 

4) Chat Service: We would like to add a chat service in the app through which pool members can coordinate rather than having to disclose their mobile numbers in the initial stage.


# Instructions

- See requirements.txt





