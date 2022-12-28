from pytube import YouTube


def download_from_youtube(link, choice):
    youtube_link = YouTube(link)
    if choice == 1:
        youtube_file = youtube_link.streams.get_highest_resolution()
    elif choice == 2:
        youtube_file = youtube_link.streams.get_lowest_resolution()
    elif choice == 3:
        youtube_file = youtube_link.streams.get_audio_only()
    else:
        print("Choice not valid.")
    try:
        youtube_file.download()
        return True
    except:
        print("Error: the file couldn't be downloaded.")


print("*** Welcome to your youtube downloader! ***")
new_link = str(input("\nPaste the URL: "))
print("\nWhat do you want to download?"
      "\n1 - Highest resolution video"
      "\n2 - Lowest resolution video"
      "\n3 - Audio only")
choice_value = int(input("\n[write a number] -> "))
if download_from_youtube(new_link, choice_value):
    print("File saved in your folder!")