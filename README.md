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
