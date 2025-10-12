from core.imports import engine,spotipy,SpotifyOAuth,webbrowser
from core.speaker import speak
from core.listener import listen

#spotify credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="5a6ed23ab2c74616ab303bb02dc608a3",
    client_secret="ac8751843ff542bca0f9e10159d7e882",
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="user-read-playback-state"
))

def spotify(song_name=None):
    # If no song name is given, ask the user again
    while not song_name or song_name.strip() == "":
        speak("What song would you like to play, sir?")
        song_name = listen()
        if not song_name or song_name.strip() == "":
            speak("I didn't hear anything, please try again.")
        else:
            break

    try:
        results = sp.search(q=song_name, limit=1, type="track")
        if not results['tracks']['items']:
            speak(f"Sorry, I couldn’t find {song_name} on Spotify.")
            return

        track = results['tracks']['items'][0]
        track_url = track['external_urls']['spotify']

        speak(f"Opening {song_name} on Spotify.")
        webbrowser.open(track_url)

    except Exception as e:
        speak("Something went wrong while searching Spotify.")
        print("Error:", e)
