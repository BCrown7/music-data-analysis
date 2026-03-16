import musicbrainzngs
import time

musicbrainzngs.set_useragent("music-data-analysis", "1.0")

def get_artist_tags(artist_name: str) -> list:
    try:
        result = musicbrainzngs.search_artists(artist=artist_name, limit=1)
        artists = result['artist-list']
        
        if not artists:
            return []
        
        artist = artists[0]
        tags = artist.get('tag-list', [])
        return [tag['name'] for tag in tags]
    
    except Exception as e:
        print(f"Error buscando {artist_name}: {e}")
        return []

def enrich_dataset(df):
    artists = df['artist'].unique()
    genres_map = {}
    
    for i, artist in enumerate(artists):
        print(f'Procesando {i+1}/{len(artists)}: {artist}')
        genres_map[artist] = get_artist_tags(artist)
        time.sleep(1)  # Para evitar exceder el límite de solicitudes

    df['genres'] = df['artist'].map(genres_map)
    return df

if __name__ == '__main__':
    tags = get_artist_tags("Metallica")
    print(f"Géneros de Metallica: {tags}")