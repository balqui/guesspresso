# ~ <script type="text/python">
from browser import document, alert # Brython in-browser support
# ~ from store import Store
from operator import *

about_str = """GuessPresso:

Using Brython to play the Expression Game.

Currently on Brython-3.8.0.

José L Balcázar (balqui at GitHub), spring and summer 2021."""


def about(ev):
    alert(about_str)

def done(ev):
	"capture contents of in and out, eval in, compare to out, choose alert contents"
	# ~ alert("Done called")
	e = ' '.join(document["in"].value.split('\n'))
	# ~ alert("read: " + e)
	try:
		v = repr(eval(e))
	except Exception as exc:
		v = "Error"
	w = document["out"].value
	if v == w:
		alert("Correct guess!")
	elif v.strip() == w.strip():
		alert("Correct guess, but be careful with spaces...")
	else:
		alert("No, sorry: " + w + " is wrong; outcome is " + v + ".")
	if v == "Error":
		alert("The type of error was: " + str(type(exc))[7:-1])

# main program: 
# bind buttons to processes and leave interaction for Brython to care for.

document['about'].bind('click', about)
document['done'].bind('click', done)
