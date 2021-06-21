
import pickle
import re
test = ['N:1900-2359', 'M:0500-2359', 'T:1700-2359', 'W:1700-2359', 'X:1700-2359', 'F:1700-2359', 'S:1900-2359']
class schedule():
    def __init__(self):
        pass
    def load(self):
        try:
            currentScheds = pickle.load(open("test.p", "rb"))
        except:
            currentScheds = []
            self.store(currentScheds)
        

        self.pullScheds(test)

    def store(self, currentScheds):
        pickle.dump(currentScheds, open("test.p", "wb"))

    def pullScheds(self,test):
        for i in test:
            days = {'N': 'Sunday', 'M': 'Monday', 'T': 'Tuesday', 'W': 'Wednesday', 'X': 'Thursday', 'F': 'Friday', 'S': 'Saturday'}
            today = days.get(i[0])
            time1, time2 = i[2:6], i[7:11]
            self.timeConversion(today, time1, time2)

            
    def timeConversion(self, day, time1, time2):
        def convert(time):
            AM, PM = False, False
            if time >= 1200:
                PM = True
                if time >= 1300:
                    time = time - 1200
            elif time <= 1199:
                AM = True
            if time >= 1000:
                time = str(time)
                time = time[:2] + ':' + time[2:]
            else:
                time = str(time)
                time = time[:1] + ':' + time[1:]

            if AM == True:
                time += 'AM'
            elif PM == True:
                time += 'PM'
            

            
                
            
            
            if count == 0:
                convert.time1 = time
            else:
                convert.time2 = time
                
            
        count = 0
        convert(int(time1))
        count += 1
        convert(int(time2))
        self.displayScheds(day, convert.time1, convert.time2)

    def displayScheds(self, day, time1, time2):
        currentScheds = pickle.load(open('test.p', 'rb'))
        currentScheds.append(day)
        currentScheds.append(time1)
        currentScheds.append(time2)
        print(currentScheds)



schedule().load()