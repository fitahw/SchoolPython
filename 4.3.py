from time import sleep

# ASSUMPTION: format either hhxmmxss or ssxmmxhh (with x being any symbol)
# ^ inaczej chyba nie ma sensu wyswietlac czasu
# bezparametrowe, jedyny argument (self), funkcje nic nie zwracaja

class Timer:
    def __init__(self, time_format, start_time, stop_time):
        self.time_format = time_format
        self.start_time = start_time
        self.stop_time = stop_time
        self.current_time = start_time

    def print_time(self):
        print(f"Aktualny czas: {self.current_time}")

    def increase_time(self):
        splitter = self.time_format[2]
        #FORMAT CHECK (to mogla byc funkcja, ale musiala by zwracac wartosc)
        hFirst = True
        if self.time_format.lower().rfind('h') > self.time_format.lower().rfind('m'):
            hFirst = False

        if hFirst:
            hour, minute, second = map(int, self.current_time.split(splitter))
        else:
            second, minute, hour = map(int, self.current_time.split(splitter))
        
        #Recalculate
        second += 1
        if second == 60:
            second = 0
            minute += 1
            if minute == 60:
                minute = 0
                hour += 1
                if hour == 24:
                    hour = 0

        if hFirst:
            self.current_time = f"{hour:02d}{splitter}{minute:02d}{splitter}{second:02d}"
        else:
            self.current_time = f"{second:02d}{splitter}{minute:02d}{splitter}{hour:02d}"

    def decrease_time(self):
        splitter = self.time_format[2]
        #FORMAT CHECK
        hFirst = True
        if self.time_format.lower().rfind('h') > self.time_format.lower().rfind('m'):
            hFirst = False

        if hFirst:
            hour, minute, second = map(int, self.current_time.split(splitter))
        else:
            second, minute, hour = map(int, self.current_time.split(splitter))

        #Recalculate
        second -= 1
        if second < 0:
            second = 59
            minute -= 1
            if minute < 0:
                minute = 59
                hour -= 1
                if hour < 0:
                    hour = 23
        
        if hFirst:
            self.current_time = f"{hour:02d}{splitter}{minute:02d}{splitter}{second:02d}"
        else:
            self.current_time = f"{second:02d}{splitter}{minute:02d}{splitter}{hour:02d}"

    def countdown(self):
        updown = int(input(print(f"Count UP (1) or DOWN (0) to {self.stop_time}?\n")))

        if updown:
            while self.current_time != self.stop_time:
                self.increase_time()
                self.print_time()
                sleep(1)
        else:
            while self.current_time != self.stop_time:
                self.decrease_time()
                self.print_time()
                sleep(1)


    def start(self):
        print(f"Start czasu: {self.start_time}")
        self.countdown()
        print(f"Koniec czasu: {self.stop_time}")

if __name__ == "__main__":
    timer = Timer("hhPmmPss", "23P59P55", "00P00P02")
    timer.start()