class Call(object):
    def __init__(self, call_id, name, phone, time, reason):
        self.call_id = call_id
        self.name = name
        self.phone = phone
        self.time = time
        self.reason = reason

    def display():
        print "ID:", call_id
        print "Name:", name
        print "Phone Number:", phone
        print "Time:", time
        print "Reason:", reason
        return self

class Call_center(object):
    def __init__(self, calls):
        self.calls = calls
        self.queue_size = len(calls)

    def add(self, call):
        self.calls.append(call)
        self.queue_size = len(self.calls)
        return self

    def remove(self):
        self.calls.pop(0)
        self.queue_size = len(self.calls)
        return self

    def remove_specific(self, phone):
        for idx, call in enumerate(self.calls):
            if call.phone == phone:
                self.calls.pop(idx)
                self.queue_size = len(self.calls)
                print "Removed call #" + str(idx + 1) +":"
                print "--------------------------------"
                return self
        print "Couldn't find that number."
        print "--------------------------------"
        return self

    def info(self):
        print "Queue length: " + str(self.queue_size) + " calls."
        for idx, call in enumerate(self.calls):
            print "Call #" + str(idx + 1) + ":"
            print "Name: " + call.name
            print "Phone Number: " + call.phone
        print "--------------------------------"
        return self

call1 = Call(1, "Ryan", "206-123-4567", "3:00P", "Saying hi")
call2 = Call(2, "Bob", "206-555-5555", "5:00P", "Asking question")
call3 = Call(3, "Jeff", "206-111-1111", "5:15P", "Returning a call")

center = Call_center([call1, call2, call3])
# center.info()
call4 = Call(4, "Sarah", "206-222-2222", "6:00P", "Asking question")
center.add(call4).info()
# center.remove().info()
center.remove_specific("206-222-2222")
center.remove_specific("206-444-4444").info()
