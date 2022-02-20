import click
import youtube_dl

@click.group()
def apis():
    """A CLI for getting transcriptions of YouTube videos"""



def main():
    apis(prog_name='apis')

if __name__ == '__main__':
    main()