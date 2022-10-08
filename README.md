# pihole-blocking-lists
List of full services (not their ads) - used to block one specific website and it's related domains (such as facebook, twitter, twitch, etc)

# Usage

## Install

Install script dependencies 

```bash
pip3 install -r requirements.txt
```

Find the service that you want to block using the pihole.log (/var/log) as an input source (after visiting/using it for a while);

```bash 
[sudo] grep 'twitch' /var/log/pihole.log > ~/loginput.txt
```

Then, run the domain detector to generate the list

```bash
domain-detection.py ~/loginput.txt > list.txt   
```

