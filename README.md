Quick app I hacked together while mentoring students at HackNC (who were doing the same challenge). Using XAMPP, I hooked up to the backend of "RAPTOR" hardware that sensed the LED light states of various data storage device components. The available data is grabbed using the RAPTOR API and then parsed. I then display the names of these components along with a graphical representation of their light states on a webpage. I used Simple Grid to quickly get the elements arranged properly and Python's powerful Paramiko API to setup SSH. No actual command needs to be submitted using the HTML form on index.html, pushing "Submit" simply runs the command that gathers all of the LED light states at once. 