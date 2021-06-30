
from fastapi import FastAPI

app = FastAPI()


# define a root `/` endpoint
@app.get("/")
def index():
    return {"ok": True}


# Implement a /predict endpoint
@app.get("/predict")
def predict(acousticness: str, danceability: str, duration_ms: str, energy: str, explicit: str, id: str, instrumentalness: str, key: str, liveness: str, loudness: str, mode: str, name: str, release_date: str, speechiness: str, tempo: str, valence: str, artist: str):

    return {
        "acousticness": acousticness, 
        "danceability": danceability, 
        "duration_ms": duration_ms, 
        "energy": energy, 
        "explicit": explicit, 
        "id": id, 
        "instrumentalness": instrumentalness, 
        "key": key, 
        "liveness": liveness, 
        "loudness": loudness, 
        "mode": mode, 
        "name": name, 
        "release_date": release_date, 
        "speechiness": speechiness, 
        "tempo": tempo, 
        "valence": valence, 
        "artist": artist
    }
