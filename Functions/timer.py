def start_time():
  start_time = time.time()
  start_time_now = datetime.datetime.now()
  print("START TIME: {0}".format(start_time_now))
  end_time_now = datetime.datetime.now()
def end_time(start_time):
    end_time = time.time()
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
    end_time_now = datetime.datetime.now()
    print('End time: {0}'.format(end_time_now))
def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    return("TIME ELAPSED &nbsp&nbsp: {0}:{1}:{2}".format(int(hours),int(mins),sec))
