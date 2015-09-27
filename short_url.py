__module_name__ = "Tinyurl service plugin"
__module_version__ = "1.0"
__module_description__ = "Turns a long URL into a much shorter one."
__author__ = "Mikica Ivosevic"

import hexchat
import urllib2

def get_short_url(url):
	res = urllib2.urlopen('http://tinyurl.com/api-create.php?url=' + url)
	return res.read()

def shorturl(word, word_eol, userdata):
	command = word[0]
	if len(word) < 2:
		print("Usage eg: /shorturl http://www.google.com")
	else:
		if command == "shorturl":
			print 'Short url: ' + get_short_url(word[1])

hexchat.hook_command("shorturl",shorturl)
hexchat.prnt(__module_name__ + ' version ' + __module_version__ + ' loadded.')
