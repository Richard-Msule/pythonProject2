from pytube import Playlist

playlist_url = 'https://www.youtube.com/playlist?list=PL1N57mwBHtN0rk48S0rTQqFN2vujutMyY'

yt_playlist = Playlist(playlist_url)
yt_playlist.download_all()
