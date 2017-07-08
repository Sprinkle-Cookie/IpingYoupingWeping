# IpingYoupingWeping


## Perchè ping packets


* When you ping Y from X, a round trip time is reported measured by the
  local clock in the pinging computer.
* We have to issue a particular number of ping commands(say 10), so we
  will get an average of all the pings.
* Ping times correlates roughly to the geographical distance. But since
  linus is the websocket server in our case for all the sync-up ops, the
latency added by the geographical location needs to be taken into
consideration.


## Come youtube even listening can be done

* We will have to use the Youtube API to listen to the events on the
  player: https://developers.google.com/youtube/iframe_api_reference?csw=1#Events
* The above documentation is only for iframe embeddings. But looks like
  we can use the same for Videos on youtube selecting the object
'movie_payer'. If you inspect the player, you will see that this is the
div that has the player mode being toggled when you pause/resume/seek the
video.

