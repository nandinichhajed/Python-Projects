import pywhatkit as kit

# Sending whatsApp message
kit.sendwhatmsg_instantly("+919406655668", "Hiiiii")
kit.sendwhatmsg_to_group("group name", "Hiiiii", 22,33)
kit.sendwhats_image("+91**********", img_path="path", caption="caption")

# To search something on web browser
kit.search("python")

# To find information
kit.info("Python programing language")

# To convert text to hand written characters
kit.text_to_handwriting("Hiii Nandini This side", rgb = (0,0,225))

# To convert any image to ASCII art.
kit.image_to_ascii_art(r"Path")

# To search and play a particular video on YouTube by using just the keyword
kit.playonyt("2002 song")

print("done")