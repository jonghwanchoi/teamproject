import threading, requests, time

class Serial_control(threading.Thread):
    def __init__(self, Port, Baud_Rate)
        threading.Thread.__init__(self)
        self.Port = Port
        self.Baud_Rate = Baud_Rate

    def run(self):
        