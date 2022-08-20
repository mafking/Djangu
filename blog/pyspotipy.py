import spotipy
import spotipy.oauth2 as oauth
from . import billboardpy


auth_manager=oauth.SpotifyClientCredentials('b1d1e790842844a8b8849bdc51fa1ffd','7b6223994b04423a80990dbe4d41e13d')
sp=spotipy.Spotify(auth_manager=auth_manager)

def search_song(track,artist):
    song=sp.search('track:{i} artist:{j}'.format(i=track,j=artist),type='track',limit=2)
    if len(song['tracks']['items']) >0:
      image=song['tracks']['items'][0]['album']['images'][0]['url'] 
      return {'track':song['tracks']['items'][0]['preview_url' ],'image':image} 
    else: return None
      


if __name__ == '__main__' :
  print(billboardpy.get_current_100())