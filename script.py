from pytube import YouTube

print("""
     _   _ _ _       _       _   _ _      _
    | | | (_) |_ ___| |__   | | | (_) ___| | _____ _ __
    | |_| | | __/ __| '_ \  | |_| | |/ __| |/ / _ \ '__|
    |  _  | | || (__| | | | |  _  | | (__|   <  __/ |
    |_| |_|_|\__\___|_| |_| |_| |_|_|\___|_|\_\___|_|   """)

print("""
  ===================YouTube Videos Download===================""")

print("""   Author : Parth Panchal""")

print("""  =============================================================""")

links = open('links_file.txt','r')

print("\n\tPlease Wait...")
j=1
for i in links:
    try:
        yt = YouTube(i)
    except:
        print('\tconnection error')

    try:    
        stream = yt.streams.first()
        stream.download('videos/')
        print("\n\tVideo",j,"is downloaded...")
        j = j+1
    except:
        print("\tError !!")
    
print("\n\tAll Videos are downloaded")