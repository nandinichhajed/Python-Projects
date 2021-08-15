from pytube import YouTube
link = input("Enter the link od video: ")
yt = YouTube(link)
# steam all the available formats of vdo
videos = yt.streams.all()

# list all the format in list from index 0
video = list(enumerate(videos))

# print all the available format of the vdo
for i in video:
    print(i)

print("Enter the desigred option to download the format: ")
option = int(input("Enter the option: "))
video = videos[option]
video.download()

print("Done")
