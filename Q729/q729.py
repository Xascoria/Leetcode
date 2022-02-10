class MyCalendar:

    def __init__(self):
        self.calendar_arr = []

    def book(self, start: int, end: int) -> bool:
        # if len(self.calendar_arr) == 0:
        #     self.calendar_arr.append( (start,end) )
        #     return True

        current_ptr = 0
        while current_ptr < len(self.calendar_arr):
            cur_range = self.calendar_arr[current_ptr]
            ## Range is larger
            if cur_range[1] < start:
                current_ptr += 1
                continue
            ## Fit right into next entry
            if cur_range[1] == start:
                if current_ptr == len(self.calendar_arr) - 1:
                    self.calendar_arr.append( (start,end) )
                    return True
                nxt_range = self.calendar_arr[current_ptr + 1]
                if end <= nxt_range[0]:
                    self.calendar_arr = self.calendar_arr[:current_ptr+1] + [(start,end)] + self.calendar_arr[current_ptr+1:]
                    return True
                else:
                    return False
            else:
                if cur_range[0] >= end:
                    self.calendar_arr = self.calendar_arr[:current_ptr] + [(start,end)] + self.calendar_arr[current_ptr:]
                    return True
                return False
        
        self.calendar_arr.append( (start,end) )
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)