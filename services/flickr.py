DOMAIN = "flickr.com"
REQUIRED_FIELDS = [ "fltoto" , "cookie_session" ]

def key( cookie ):
    return cookie[ "fltoto" ][-40:]

def header( cookie ):
    return "http://" + DOMAIN

def url( cookie ):
    return DOMAIN + "/people/me"
