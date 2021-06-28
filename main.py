from pytube import YouTube
import time

url = input("Enter the url of the video to download it: ")
resv = input("Choose the resolutin: (e.g. 720p) ")
try:

    yt = YouTube(url)

    # download if that specific resolution is possible
    try:
        print("Downloading now")
        a = time.time()
        yt.streams.filter(progressive=True).filter(rev=resv).download()
        print("Download completed")
        b = time.time()

    # If resolution is not available
    except:
        print(f"{resv} was not available")
        print("press y to download best resolution possible")
        print("press any character or number key to quit")
        choice = input()

        # download if preses y
        if choice == 'y':
            print("Downloding the best resolution present")
            a = time.time()
            yt.streams.filter(
                progressive=True).get_highest_resolution().download()
            b = time.time()
        else:
            exit()

    print("Time taken: ", b-a)

except Exception as e:
    print(e)
