Getting set up on IRC
=====================

Register your nickanme on freenode
----------------------------------

 - `Overview of registering a nickname on freenode.net <http://freenode.net/faq.shtml#nicksetup>`_

 It is useful to register a nickname with the IRC server you are using, first so that you can always have your nickname when you log on (other users will be kicked if they try to use your nickname) and so that others can be sure that they are talking to the same person each time.

 The following directions are for Freenode only, though other IRC servers will have similar instructions.

 Once you are connected to freenode with the nickanme that you would like to register, send the following text in any channel connected to freenode:

 - /msg NickServ register <password> <email>

 This sends a private message to the NickServ bot which stores your nickname, password, and an email you can use to identify yourself with the freenode staff should you need to recover the password.

 Additionally, you should receive an email verifying your address to finish the registration process.  Once that process is complete you will have to use the following text to identify yourself to freenode each time you log in:

 - /msg NickServ identify <password>

 Sometimes, due to a lost connection or another computer running IRC seperately, you will not be able to get your main IRC nickname.  In this case, most IRC clients will try appending an underscore (_) to your desired nickname.  You can add these names to your registered nick without registering a new nickname.  To do this, change your nickname to the next nickname, identify with NickServ again, and then group your current nick with your registered nick

 - /nick <new nickname>

 - /msg NickServ identify <registered nickname> <password>

 - /msg NickServ group

 Note that this time you specify the nicname you registered with NickServ, as it is now different than your current nickname.
