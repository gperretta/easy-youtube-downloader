from pytube import YouTube
import os


def download_from_youtube(link, choice):
    youtube_video = YouTube(str(link))
    try:
        if choice == 1:
            output_path = youtube_video.streams.get_highest_resolution().download()
        elif choice == 2:
            output_path = youtube_video.streams.get_lowest_resolution().download()
        elif choice == 3:
            output_path = youtube_video.streams.filter(only_audio=True).first().download()
            separated_name = os.path.splitext(output_path)
            new_name = separated_name[0]+'.mp3'
            os.rename(output_path, new_name)
        else:
            print("Choice not valid.")

        print("\nDownload completed!\nFind your file: " + output_path.title())
    except:
        print("Error: the file couldn't be downloaded.")


print("*** Welcome to your youtube downloader! ***")
new_link = str(input("\nPaste the URL: "))
print("\nWhat do you want to download?"
      "\n1 - Highest resolution video"
      "\n2 - Lowest resolution video"
      "\n3 - Audio only")
choice_value = int(input("\n[write a number] -> "))

download_from_youtube(new_link, choice_value)



