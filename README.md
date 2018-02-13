I couldn't find the option to sign up for delivery notifications on Lasership's website, but they have a nice API so I wrote a python script to let me know when my Laserhip packages get delivered. Here is what its execution looks like in a terminal window:

<p align="center"><img src=demo1.png width=598 height=259 /></p>

The sender's gmail credentials I provide the script with are for an account I set up just for this purpose, mainly because you need to [let less secure apps use your account][1] for the scheme to work. As long as the script is running, it checks the delivery status and prints out a log message about it every minute. Personally, I like to run this script on my Raspberry Pi since it's the only machine that can do it and is always on in my house. When the delivery status changes to delivered I get an email like this:

<p align="center"><img src=demo2.png width=320 height=568 /></p>

The script uses a few awesome packages to get the job done: _getpass_ prompts the user for a password without echoing, _json_ and _request_ parse the json file, _smtplib_ sends out the email, _time_ pauses execution and _datetime_ formats the output to the log.

  [1]: https://support.google.com/accounts/answer/6010255?hl=en "google's support article on this subject"
