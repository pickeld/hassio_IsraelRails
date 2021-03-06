"""
Israel Railways Scheduler.
Made By: pickeld 
"""
 
# -*- coding: utf-8 -*-
#import json
import requests
import datetime
import logging
from datetime import timedelta
from homeassistant.helpers.event import track_time_interval
from homeassistant.helpers.entity import Entity
from homeassistant.util import Throttle
 
_LOGGER = logging.getLogger(__name__)
UPDATE_MIN = timedelta(minutes=10)
 
DOMAIN = 'israel_rails'
CONF_TOPIC = 'topic'
 
stations = {'1220': 'לב המפרץ',
 '1240': 'יקנעם - כפר יהושע',
 '1250': 'מגדל העמק - כפר ברוך',
 '1260': 'עפולה',
 '1280': 'בית שאן',
 '1300': 'חוצות המפרץ',
 '1400': 'קריית מוצקין',
 '1500': 'עכו',
 '1600': 'נהריה',
 '1820': 'אחיהוד',
 '1840': 'כרמיאל',
 '2100': 'חיפה- מרכז השמונה',
 '2200': 'חיפה - בת גלים',
 '2300': "חיפה - חוף הכרמל (ש' רזיאל)",
 '2500': 'עתלית',
 '2800': 'בנימינה',
 '2820': 'קיסריה - פרדס חנה',
 '300': 'פאתי מודיעין',
 '3100': 'חדרה - מערב',
 '3300': 'נתניה',
 '3310': 'נתניה - ספיר',
 '3400': 'בית יהושע',
 '3500': 'הרצליה',
 '3600': 'תל אביב - אוניברסיטה',
 '3700': 'תל אביב - סבידור מרכז',
 '400': 'מודיעין - מרכז',
 '4100': 'בני ברק',
 '4170': 'פתח תקווה  - קריית אריה',
 '4250': 'פתח תקווה - סגולה',
 '4600': 'תל אביב - השלום',
 '4640': 'צומת חולון',
 '4660': 'חולון - וולפסון',
 '4680': 'בת ים - יוספטל',
 '4690': 'בת ים - קוממיות',
 '4800': 'כפר חב"ד',
 '4900': 'תל אביב - ההגנה',
 '5000': 'לוד',
 '5010': 'רמלה',
 '5150': 'לוד גני אביב',
 '5200': "רחובות (א' הדר) ",
 '5300': 'באר יעקב',
 '5410': 'יבנה מזרח',
 '5800': "אשדוד עד הלום (מ' בר כוכבא)",
 '5900': 'אשקלון',
 '6300': 'בית שמש',
 '6500': 'ירושלים - גן החיות התנכי',
 '6700': 'ירושלים - מלחה',
 '700': 'קריית חיים',
 '7000': 'קריית גת',
 '7300': 'באר שבע- צפון/אוניברסיטה',
 '7320': 'באר שבע - מרכז',
 '7500': 'דימונה',
 '8550': 'להבים - רהט',
 '8600': 'נמל תעופה בן גוריון',
 '8700': "כפר סבא - נורדאו (א' קוסטיוק)",
 '8800': 'ראש העין - צפון',
 '9000': 'יבנה מערב',
 '9100': 'ראשון לציון - הראשונים',
 '9200': 'הוד השרון - סוקולוב',
 '9600': 'שדרות',
 '9650': 'נתיבות',
 '9700': 'אופקים',
 '9800': 'ראשון לציון-משה דיין'}
 
 
 
def setup(hass, config):
    fromStation = config[DOMAIN].get('fromStation')
    toStation = config[DOMAIN].get('toStation')
    Tdate = int((datetime.date.today()).strftime("%Y%m%d")) #todays date
    Tgmt = config[DOMAIN].get('timeZone') # hass timezone
 
    israelrails(hass, fromStation, toStation, Tdate,Tgmt)
    hass.states.set('israel_rails.FromStation', (stations[str(fromStation)]))
    hass.states.set('israel_rails.ToStation', (stations[str(toStation)]))
    hass.states.set('israel_rails.Next_Train', str(nextTrain).split(" ")[1])
 
 
class israelrails(Entity):
    def __init__(self, fromStation, toStation, Tdate, Tgmt):
        self.parseData()
        self.fromStation = fromStation
        self.toStation= toStation
        self.Tdate= Tdate
        self.Tgmt= Tgmt
        self._state = None
        self.parseData()
   
    def icon(self):
        """Icon to use in the frontend, if any."""
        return 'mdi:calendar'
 
    def name(self):
        return self._name
 
 
    @Throttle(UPDATE_MIN)
    def parseData(self):
        i = 0
        #url = 'https://rail.co.il/apiinfo/api/Plan/GetRoutes?OId={}&TId={}&Date={}&Hour=2400&isGoing=true'.format(self.fromStation, self.toStation, self.Tdate)
        url = "http://www.rail.co.il/apiinfo/api/Plan/GetRoutes?OId=8800&TId=3600&Date=20171123&Hour=2200&isGoing=true"
        _LOGGER.info(url)
       
        data = requests.get(url).json()
 
        nextTrain = data["Data"]["Routes"][i]["Train"][0]["DepartureTime"]
        nextTrain = datetime.datetime.strptime(nextTrain , "%d/%m/%Y %H:%M:%S")
        TimeNow = datetime.datetime.now()
 
        while(TimeNow + datetime.timedelta(hours=2) - nextTrain).total_seconds() < 0:
            i=i+1
            nextTrain = data["Data"]["Routes"][i]["Train"][0]["DepartureTime"]
            nextTrain = datetime.datetime.strptime(nextTrain , "%d/%m/%Y %H:%M:%S")
 
 
        return (nextTrain)
