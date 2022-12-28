from requests import get
import re

def get_todays_events():
    page = get("https://onthisday.com").text
    events_dump = re.findall('class="event-list__item".+', page)
    events = []
    for event in events_dump:
        current_event = re.sub('''<a href=".*?">|<a>|<b>|</a>|</b>|<li>|</li>|class="event-list__item">''',"",event)
        events.append(current_event)
    return events
