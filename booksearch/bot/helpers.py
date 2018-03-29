from  bot.views import *

def book_request_handler(text):
        
    a = []
    if "@book" in text:
        a.append("book")
        text = text.replace("@book", "")
    if "@movie" in text:
        a.append("movie")
        text = text.replace("@movie", "")
    if "@tv" in text:
        a.append("tv")
        text = text.replace("@tv", "")

    if "@song" in text:
        a.append("song")
        text = text.replace("@song", "")


    MOVIE_API_KEY = "040b462a3e46fe07c098aae8c0d806d6"
    YOUR_BOOK_KEY = "z8BdUYyClBcYIiGglrXMBA"

    #Book Request
    res_book = ''

    breq = requests.get("https://www.goodreads.com/search.xml", params={"key": YOUR_BOOK_KEY,"q" : text})
    xml = breq.text
    dict = xmltodict.parse(xml)
    
    len = int(dict["GoodreadsResponse"]['search']['results-end'])
    try:
        book = dict["GoodreadsResponse"]['search']['results']['work'][0]
        rating = book['average_rating']
        title = book['best_book']['title']
        author = book['best_book']['author']['name']
        
        res_book = "Book Name: {0}\nAuthor: {1} \nRating:{2}\n".format(title, author, rating)
    except Exception as exp:
        print sys.exc_info()


    #Movie Request
    res_movie = ''
    req = requests.get("https://api.themoviedb.org/3/search/movie", params={"api_key":MOVIE_API_KEY,"query":text})
    res_mov = json.loads(req.text)
    try:
        result =  res_mov['results'][0]
        mov_title = result['title']
        release_date = result['release_date']
        overview = result['overview']
        res_movie = "\nMovie Details\nTitle:{0}\n Release Date: {1}\n Movie Overview: {2}".format(mov_title, str(release_date), overview)
    except Exception:
        print sys.exc_info()
    
    if "book" in a:
        return res_book
    if "movie" in a:
        return res_movie

    #TV Request
    res_tv = ''
    req = requests.get("https://api.themoviedb.org/3/search/tv", params={"api_key":MOVIE_API_KEY,"query":text})
    resp_tv = json.loads(req.text)
    try:
        result =  resp_tv['results'][0]
        tv_title = result['original_name']
        rating = result['vote_average']
        overview = result['overview']
        res_tv = "\nTV series Details\nTitle:{0}\n Average Rating: {1}\n Overview: {2}".format(tv_title, rating, overview)
    except Exception:
        print sys.exc_info()
    
    #Song Request
    YOUR_KEY = "ad78c75776b93da787d08df051b73e19"
    res_song = ''
    params={"method" : "track.search", "api_key": YOUR_KEY,"track" : text, "format" : "json"}
    req = requests.get("http://ws.audioscrobbler.com/2.0/", params=params)         
    res = json.loads(req.text)

    track = res['results']['trackmatches']['track'][0]
    artist = track['artist']
    name = track['name']
    
    res_song = '\nMusic Details\nName:{0}\nArtist: {1}'.format(name, artist)

    if "book" in a:
        return res_book
    if "movie" in a:
        return res_movie
    if "tv" in a:
        return res_tv
    if "song" in a:
        return res_song

    return res_book + res_movie + res_tv +res_song
