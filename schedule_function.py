import time
import sched

def delayed_function(start_time, callback, *args):
    """Schedule manualy a function to be called at a certain time.

    Arguments:
    time -- the time at which the function should be called
    callback -- the function to be called
    args -- the arguments to be passed to the function
    """
    # Calculate the time to sleep
    sleep_time = start_time - time.time()
    # Sleep until the time is right
    time.sleep(sleep_time)
    # Call the function
    callback(*args)


def schedule_function(start_time, callback, *args):
    """Schedule a function to be called at a certain time.

    Arguments:
    time -- the time at which the function should be called
    callback -- the function to be called
    args -- the arguments to be passed to the function
    """

    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enterabs(start_time, 1, callback, args)
    print('Starting scheduler')
    scheduler.run()

if __name__ == '__main__':
    schedule_function(time.time() + 1, print, 'Howdy!')
    delayed_function(time.time() + 1, print, 'Howdy!')