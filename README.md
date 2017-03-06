# Publish IP to Slack Channel Bot
Two parts:
1) Public IP
2) Private IPs

I wanted a way to connect to my Raspberry Pi, even when network changes happened.  This solves for the following scenarios:
1) At-home public IP changes.  My tunnel to my Raspi will break.  Now I'll have this info in Slack.
2) At a new location, my Raspi will auto-tether to my phone if no other network is available.  When this happens, 
I'll be alerted of the private IP and I can SSH to the device from my phone.
3) I'd like to be able to manage the wireless networks entirely with the SenseHAT -- that will have to come later!

Enjoy!
