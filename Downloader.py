import click
import youtube_dl

@click.group()
def apis():
    """A CLI for getting transcriptions of YouTube videos"""

@click.argument('link')
@apis.command()
def download_video(link): #function to downlaod videos, run the file adding downlaod-video "youtube video link"
   ydl_opts = {
       'format': 'mp4',
       'outtmpl': "./%(id)s.%(ext)s",
   }
   _id = link.strip()
   meta = youtube_dl.YoutubeDL(ydl_opts).extract_info(_id)
   save_location = meta['id'] + ".mp4"
   print(save_location)
   return save_location



def main():
    apis(prog_name='apis')

if __name__ == '__main__':
    main()