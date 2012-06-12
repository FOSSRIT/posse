Day 4: Community
================
We'll be talking about the social aspects of collaboration, and a little bit today. Broadly speaking, it has it's own culture, and many subcultures within each project. Depending on the nature of the project, there are differences.

Outline of Discussions
----------------------

Handling Flames and Forks
`````````````````````````
What do disagreements look like in open source, and how can we help our students cope with a sometimes unpredictably blunt world?

Flames
******
Everyone has used mail lists yes?

Everyone in open source has to have a thick skin

Imagine you have an open source project that is your baby

how would you respond to the same questions over and over again, year
after year?

Folks entering open source project asking questions that are readily
answerable with publicly posted information are subject to flames.

Elitist mindset is common to many major projects

Not saying this is a good or bad thing, just something to be expected.

New contributors have to "Do his/her homework"

Perhaps you've heard the advice "DON'T FEED THE TROLLS"?
    i.e. ignore flames or Do not respond to trolls publicly.

People in the community usually know who the trolls are.

If you are moving in a direction and there are no objects in your way then you
are not actually moving. Haters, therefore, are one type of indication of
success (of sorts).

If you have operator privileges in IRC, you can ban or kick them from the
channel.

If you want it to be or seem more equitable, you can set up the com channel so
that people are only given voice through a formal request. This can pre-empt
"Trollish" tactics.

IRC has a couple of ways of dealing with the problem child. On a mailing list
it is a little harder to do. Make sure it is subscriber only for posting. This
eliminates (most) spammers. Try to filter folks on the way in. 

If a flame war starts, be honest, be yourself, if it is a problem of elitism,
"everyone is learning" is usually the right stance to take.

Hackers will often tell folks "you're doing it wrong"
    Don't take it personally, just say "Thank you, this is an open environment,
    we are all learning." This is a much better response than Blocking and
    kicking, which should only be used as a last resort.

    These issues are not that common in a student or classroom environment.
    Even with a decently sized open source project. FOSS project selection bias
    tends to eliminate trollish folks.

Large programs or projects may have some Tired crusty greybeards :)
https://plus.google.com/102150693225130002912/posts/UkoAaLDpF4i

Flames can be playful and fun. The Computer Science House at RIT
(http://csh.rit.edu) has a separate mailing list just for flames so that
flaming does not interfere with the normal conversation, and is segregated into
an "appropriate" context.

Forks
*****
   back in the early days forking was a dirty word.  I'm taking my ball and going home.  This was a scary term in Open Source because it could take away core contributors.  Still is an issue.  But fork is no longer a dirty word.  Look on Github there is a fork button.  The way that you protect your project is by licensing.  If you are going to take this code for your project and make patches on it, you have to send those patches back upstream.  PErmissisive licenses like BSD.  OSX runs Unix under the hood, right there in a Mac.  BSD license.  Remy likes it.  Many folks in the FOSS community don't like Apple because they don't release much back upstream.  NATE Apple does release things back upstream, by and large they are Copyleft licensed stuff.  Cocoa and some of the graphics stuff?  Carbon is.  NExt step and GNU Step.  All of the base libraries for OSX are available, but are not used much outside of OSX so their usefullness is questionable.  Many folks in the OS community are pushing Apple to move patches back upstream.  To avoid forks put the material under CopyLeft licencing.  
   NATE: copyleft is not a guarantee that such licensed code will remain open.  Oracle bought Sun and (oracle is hostile to OS projects that it consumes)  MySQL, Java--forked to Open JDK, Jenkins, Hudson, 
   So mysql is a long running open source project.  There was an immediate fork of mysql called Maria.  Very quickly the forked project picked up many of the mysql developers.  
   Oracle bought Open Office, which was forked to Libre Office which everyone moved to (except lame folks like myself who haven't had the time to switch). Again many of the developers have moved over to Libre.  
   "Recursive public" 
   Decisions in licensing software can have huge implications down the road.  One can even have the license held by a separate entity, or you can have the rights held by each of the contributors.  In the former, it is easy to make changes, in the latter each contributor has to agree to changes. 
   Forks can often create confusion amongst user bases.  Almost no one has heard of MariaDB; everyone still uses Mysql.  How do you get users to understand the changes?  There's no mechanism to get the word out to end users.  Which is why distros and bundles are so important--they reset the default version (or fork) of what folks will actually use.
   Firefox. Mozilla has very strict rules for distributing things that will be called "Firefox"  Debian's version of Firefox is forked to be "Iceweasel" because it is too different from Firefox for Mozilla.
   Does the public care and to what degree?
   There are plenty of people who are just consumers of software.  Not that one is better than the other.  We are all in this hybrid transitional state.  Software is so essential to current life
   The endless September  back in theearly days every September students would go to college and would get access to the internet for the first time and all of these students would come on line and would have to be taught the social rules and best practices.  Then as more folks came online September became all the time.
   http://www.codinghorror.com/blog/2012/05/please-dont-learn-to-code.html  Bloomberg wants to learn to code‽
   
   NATE there are a lot of new projects coming lately that attempt to do what existing projects already do well.  Folks are forking or recreating existing projects without need?  Concern is that it could become code Babel.  Not necessarily bad.  Seeing lots of projects doing this which will not likely be there in six months.  
   Students have to research the field of existing projects before they start new projects.  Hostility can result, will result from folks who see projects rehashing old ground, precisely because it is old ground and effort is obviously wasted.
   Open Video Chat project was created as a video chat tool for ASL communication on the XO (OLPC) laptop.  They hacked the project to double the frame rate (started at 5-6fps).  There were many hardware limitations, but there were community limitations as well.  Other groups in OLPC, there ended up being different release cycles for each of the interested communities.  We had to learn the lesson of doing our homework over and over again, even setting up a mailing list, which duplicated existing lists.  Setting up a new IRC channel was a source of flack.  Eventually we had enough development that we became accepted, hackathons.  The OLPC development team was able to see that the project was making progress.  If you think about your project as an element in an ecosystem then the flames do not seem so intense.  Real time video chat is still one of the first things that folks ask for.

Commarch Assignment
```````````````````

How do FOSS projects are presented/deisseminated, and how to attract contributors.

Picking Pertinent Problems
``````````````````````````
Articulating your work in a way the community cares about

You can go to the community and ask "What needs to be done?"  Remy is talking about Open States. --scrapes various state public databases and makes information public.  
   --"What can I do to help?"  the question you want to hear from the public
   Sunlight foundation & James Turk.  There is a standard way of finding the source data, but the more people you have in local communities they can help developers interpret locally based data.
   
   Developers may need specific technical and non-technical data.
   Think about your project on a milestone basis.  Inverted pyramid thinking.  Start with a general description that you may tell folks about what you are doing.  level 2, what are the main elements of the project?  What are the specific needs to each element of the stack?  How can folks without coding abliity contribute to the project?  Segmenting out your stack so that it is obvious what the various pieces are(to a third party).  This facilitates contributors jumping into/onto the project.  Level 3 tasks, specific 
   
   http://openstates.org/
   
   Segmenting the project. You want to break the project into tasks and then tickets.  Very small, granular level bugs.  Once you have your tickets in something like Track.  Github itself has a project management elements now, "issue tracker" in Github can be used to track tickets.  
   Bug trackers  Bugzilla, Track, 
 Once you've got the project segmented then you have to present it to the public.  openhatch.org
 
 Find a trivial bug and fix it.
Projects need to post easy bugs for new contributors to fix--as a means of setting a low bar to entry.  
Fedora keeps people engaged by putting their name on it.  Giving people a title or a role.  For students telling them that they are "Core Developers" makes them feel good about it and keeps them around.  GIVES THEM OWNERSHIP.  "You are helping to keep Open Source alive."  Don't just engage students when something goes wrong.  Use the carrot rather than the stick.  Redhat does pay folks but Fedora is a community managed project.  Hirees come from the developer community.  Folks who have proven themselves.  15 people on the paid Fedora engineering team.  Those developers depend on thousands of folks who are not paid. Most folks in Open Source are "Scratching their own itch."
http://openhatch.org/search/?q=&toughness=bitesize
http://openstates.org/api/
https://github.com/bksteele57/Commarch-Android
https://docs.google.com/document/d/1Dp0s_sh2Ba-UNVf7vRLCLO10MXmP1rvhEBWiXj8FWbE/edit?pli=1
https://docs.google.com/document/d/1Dp0s_sh2Ba-UNVf7vRLCLO10MXmP1rvhEBWiXj8FWbE/edit?pli=1
http://teachingopensource.org/index.php/Main_Page
http://teachingopensource.org/index.php/Main_Page
https://workflowy.com/shared/3ea5abdc-2513-aafc-ccc0-20bc7cf22cfb/#

Bus-/Raptor-proofing
````````````````````
Leveraging project teams to future-proof your work

Bus/Raptor Tests, speak to the notion of sustainability in development/collaboration. We've left a block open to particpants to post topics and issues related to FOSS. We'll poll people for specific topics.

if your entire dev team was on a bus and went off a cliff, what are the chances that your project would survive.  Raptor proofing is about if this happened to your chief dev, ....  All of this comes under the heading of futureproofing.  Will your project be able to survive.  Making sure that you are distributing your infrastructure and your developers.  Where are the dangerous places in your project.  how to protect you against disaster.
First tool gitbyabus  https://github.com/tomheon/git_by_a_bus/blob/master/README.txt  very simple and easy to use.  Can be really useful to answer some of the Commarch questions. 
https://github.com/Frencil/MultiGource/blob/master/log_generator.php
http://www.youtube.com/watch?v=YZ6ILsOIBgA
http://en.gravatar.com/
http://code.google.com/p/gource/
http://zmoazeni.github.com/gitspective/
https://github.com/tomheon/git_by_a_bus/blob/master/README.txt
http://narcissus.rc.rit.edu/map#2.10/35.80/-344.20
http://threebean.org/
http://readthedocs.org/docs/ritfloss/en/latest/lectures.html?highlight=threebean

Open Block
``````````
Participants can work on deep dive, Commarch Assignment, or direct discussion on an unplanned OS topic.

Home Stretch Dinner
-------------------
Thursday Night will be a celebration/graduation dinner.
