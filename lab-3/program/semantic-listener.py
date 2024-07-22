import sys
from antlr4 import *
from gen.ConfRoomSchedulerLexer import ConfRoomSchedulerLexer
from gen.ConfRoomSchedulerParser import ConfRoomSchedulerParser
from gen.ConfRoomSchedulerListener import ConfRoomSchedulerListener

from datetime import datetime, timedelta

class ConfRoomSchedulerSemanticChecker(ConfRoomSchedulerListener):

    MAX_USAGE_TIME = timedelta(hours = 2)

    def __init__(self):
        super().__init__()
        self.reservations = []

    def create_datetime(self, date, time):
        return datetime.strptime(f"{date} {time}","%d/%m/%Y %H:%M")
        
    def validate_date(self, date):
        try:
            datetime.strptime(date, "%d/%m/%Y")
            return True
        except ValueError:
            return False
        
    def validate_time(self, time):
        try:
            hour, minute = map(int, time.split(':'))
            if 0 <= hour < 24 and 0 <= minute < 60:
                return True
            else:
                return False
        except ValueError:
            return False
        
    def is_overlapping(self, new_id, new_start, new_end):
        for id, _, _, start, end in self.reservations:
            if new_start < end and start <= new_start and new_id == id:
                return True
            elif new_end > start and end >= new_end and new_id == id:
                return True
            elif new_start <= start and new_end >= end and new_id == id:
                return True
            
        return False
        
    def enterReserveStat(self, ctx:ConfRoomSchedulerParser.ReserveStatContext):
        start_time = ctx.reserve().TIME(0).getText()
        end_time = ctx.reserve().TIME(1).getText()
        id = ctx.reserve().ID().getText()
        name = ctx.reserve().NAME().getText()
        date = ctx.reserve().DATE().getText()

        if not self.validate_date(date):
            raise ValueError(f"Error: Invalid date {date}")
        
        if not self.validate_time(start_time) or not self.validate_time(end_time):
            raise ValueError(f"Error: Invalid time {start_time} to {end_time}")

        start_datetime = self.create_datetime(date,start_time)
        end_datetime = self.create_datetime(date,end_time)
        

        if start_datetime >= end_datetime:
            raise ValueError(f"Error: The start time {start_time} must be before the end time {end_time}")
        
        duration = end_datetime - start_datetime

        if duration > self.MAX_USAGE_TIME:
            raise ValueError(f"Error: The reservation duration {duration} exceeds the maximum allowed time of {self.MAX_USAGE_TIME}")
        
        if self.is_overlapping(id, start_datetime, end_datetime):
            raise ValueError(f"Error: The reservation {date} {start_time} to {end_time} overlaps with an existing reservation")
        else:
            self.reservations.append((id, name, date, start_datetime, end_datetime))

    def enterToListStat(self, ctx:ConfRoomSchedulerParser.ToListStatContext):
        print("\n\nExisting Reservations:\n")
        if len(self.reservations)>0:
            for id, name, date, start, end in self.reservations:
                print(f"RESERVACION EN {id} PARA {start.strftime('%d/%m/%Y')} DE {start.strftime('%H:%M')} A {end.strftime('%H:%M')} POR {name}\n")
        else:
            print("There are no reservations\n")

    def exitCancelStat(self, ctx:ConfRoomSchedulerParser.CancelStatContext):
        start_time = ctx.cancel().TIME(0).getText()
        end_time = ctx.cancel().TIME(1).getText()
        id = ctx.cancel().ID().getText()
        name = ctx.cancel().NAME().getText()
        date = ctx.cancel().DATE().getText()

        start_datetime = self.create_datetime(date, start_time)
        end_datetime = self.create_datetime(date, end_time)

        value = (id, name, date, start_datetime, end_datetime)

        if value in self.reservations:
            self.reservations.remove(value)
        else:
            raise ValueError(f"Error: Non-existent reserve")
        
    def enterRescheduleStat(self, ctx:ConfRoomSchedulerParser.RescheduleStatContext):
        # Actual data
        start_time = ctx.reschedule().TIME(0).getText()
        end_time = ctx.reschedule().TIME(1).getText()
        id = ctx.reschedule().ID().getText()
        name = ctx.reschedule().NAME().getText()
        date = ctx.reschedule().DATE(0).getText()

        # New data
        new_start_time = ctx.reschedule().TIME(2).getText()
        new_end_time = ctx.reschedule().TIME(3).getText()
        new_date = ctx.reschedule().DATE(1).getText() 

        if not self.validate_date(new_date):
            raise ValueError(f"Error: Invalid date {new_date}")
        
        if not self.validate_time(new_start_time) or not self.validate_time(new_end_time):
            raise ValueError(f"Error: Invalid time {new_start_time} to {new_end_time}")

        start_datetime = self.create_datetime(date, start_time)
        end_datetime = self.create_datetime(date, end_time)

        new_start_datetime = self.create_datetime(new_date, new_start_time)
        new_end_datetime = self.create_datetime(new_date, new_end_time)
        value = (id, name, date, start_datetime, end_datetime)

        if value not in self.reservations:
            raise ValueError(f"Error: Non-existent reserve")
        
        if new_start_datetime >= new_end_datetime:
            raise ValueError(f"Error: The start time {new_start_datetime} must be before the end time {new_end_datetime}")
        
        duration = new_end_datetime - new_start_datetime

        if duration > self.MAX_USAGE_TIME:
            raise ValueError(f"Error: The reservation duration {duration} exceeds the maximum allowed time of {self.MAX_USAGE_TIME}")
        
        if self.is_overlapping(id, new_start_datetime, new_end_datetime):
            raise ValueError(f"Error: The reservation {date} {new_start_datetime} to {new_end_datetime} overlaps with an existing reservation")
        else:
            
            self.reservations[self.reservations.index(value)] = (id, name, new_date, new_start_datetime, new_end_datetime)

def main():
    input_stream = FileStream(sys.argv[1])
    lexer = ConfRoomSchedulerLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ConfRoomSchedulerParser(stream)
    tree = parser.prog()
    print(tree.toStringTree(recog=parser))
    
    semantic_checker = ConfRoomSchedulerSemanticChecker()
    walker = ParseTreeWalker()
    walker.walk(semantic_checker, tree)

if __name__ == '__main__':
    main()