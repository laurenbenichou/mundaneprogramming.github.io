import re
RX_LOREM    = "lorem|etaoin?shrdlu|asdf|quick brown fox|blah|etc"
RX_TODO       = "tk|cq|to[\-_]do|(?:[x?]{3,})"
RX_LOL      = "lol|wt[fh]|rtfm|lmao|rofl|\bw[au]t\b"
RX_ASS      = "\bass|arse|ass-?[fhks]|butt|anus"
RX_CARLIN   =  RX_ASS + "fu[\Wck]?k|shit|piss|cunt|\bcock|tit"
RS_VAIN     = "dam[mn]|god|jesus|hell|heck|holy"
RX_CUSS     = "douche||d[i1!]ck|boob|p[iu]ss|dildo|(?:re)?tard|whore|bi?tch|gay|porn"
RX_NEG      = "anal|stupid|jerk|dumb|nazi|douche|suck|screw|moron|turd|wank|bull|funk|fubar|snafu|doof|whatev|d[uo]h"
RX_PS       = "[^aeiou\s\W]{4}"