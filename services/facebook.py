DOMAIN = "facebook.com"
REQUIRED_FIELDS = [ "c_user" , "xs" , "presence" ]

def key( cookie ):
    return cookie[ "c_user" ]

def header( cookie ):
    return "http://" + url( cookie )

def url( cookie ):
    return DOMAIN + "/profile.php?id=" + cookie[ "c_user" ]
