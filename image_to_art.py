import pywhatkit

fromfile = input('Enter image path:')
to = input('Enter text file name:')

pywhatkit.image_to_ascii_art(fromfile,to)