import datetime

# get date and tiem to guarantee unique file name:
currentDT = datetime.datetime.now()
# formatted date and time:
time_stamp = currentDT.strftime("%Y_%m_%d_%Hh%Mm%Ss")

# new image name:
new_image_name = "new_images/IMG" + time_stamp + ".png"

# now save image

