# hassio_IsraelRails
Israel Rails component for HomeAssistant

![alt text](https://github.com/pickeld/hassio_IsraelRails/blob/master/img/ha1.PNG)
![alt text](https://github.com/pickeld/hassio_IsraelRails/blob/master/img/ha2.PNG)

BETA!

I woulnt be able to make this without the help of @TomerFi, thank you!

instructions:
  1. create a folder "custom_components" under you config folder
  2. copy the "israel_rails.py" file into "custom_components"
  3. in your configuration yaml add the following:
  ```
israel_rails:
  rosh_haayin_zafon_to_ta_university:
    name: Home To School
    from_station: '8800'
    to_station: '3600'
  ta_university_to_rosh_haayin_zafom:
    name: School To Home
    from_station: '3600'
    to_station: '8800'
```

      
pick your fromStation and toStation from the list below:
```
1220 - לב המפרץ
1240 - יקנעם - כפר יהושע
1250 - מגדל העמק - כפר ברוך
1260 - עפולה
1280 - בית שאן
1300 - חוצות המפרץ
1400 - קריית מוצקין
1500 - עכו
1600 - נהריה
1820 - אחיהוד
1840 - כרמיאל
2100 - חיפה- מרכז השמונה
2200 - חיפה - בת גלים
2300 - "חיפה - חוף הכרמל (ש רזיאל)"
2500 - עתלית
2800 - בנימינה
2820 - קיסריה - פרדס חנה
300 - פאתי מודיעין
3100 - חדרה - מערב
3300 - נתניה
3310 - נתניה - ספיר
3400 - בית יהושע
3500 - הרצליה
3600 - תל אביב - אוניברסיטה
3700 - תל אביב - סבידור מרכז
400 - מודיעין - מרכז
4100 - בני ברק
4170 - פתח תקווה  - קריית אריה
4250 - פתח תקווה - סגולה
4600 - תל אביב - השלום
4640 - צומת חולון
4660 - חולון - וולפסון
4680 - בת ים - יוספטל
4690 - בת ים - קוממיות
4800 - כפר חב"ד
4900 - תל אביב - ההגנה
5000 - לוד
5010 - רמלה
5150 - לוד גני אביב
5200 - "רחובות (א הדר) "
5300 - באר יעקב
5410 - יבנה מזרח
5800 - "אשדוד עד הלום (מ בר כוכבא)"
5900 - אשקלון
6300 - בית שמש
6500 - ירושלים - גן החיות התנכי
6700 - ירושלים - מלחה
700 - קריית חיים
7000 - קריית גת
7300 - באר שבע- צפון/אוניברסיטה
7320 - באר שבע - מרכז
7500 - דימונה
8550 - להבים - רהט
8600 - נמל תעופה בן גוריון
8700 - "כפר סבא - נורדאו (א קוסטיוק)"
8800 - ראש העין - צפון
9000 - יבנה מערב
9100 - ראשון לציון - הראשונים
9200 - הוד השרון - סוקולוב
9600 - שדרות
9650 - נתיבות
9700 - אופקים
9800 - ראשון לציון-משה דיין
```
