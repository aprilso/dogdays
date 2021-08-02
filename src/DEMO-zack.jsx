import React from 'react';

import {
  MonthlyBody,
  MonthlyCalendar,
  MonthlyNav,
  DefaultMonthlyEventItem,
} from '@zach.codes/react-calendar';


export const MyMonthlyCalendar = () => {
  let [currentMonth, setCurrentMonth] = useState<Date>(
    startOfMonth(new Date())
  );

  return (
    <MonthlyCalendar
      currentMonth={currentMonth}
      onCurrentMonthChange={date => setCurrentMonth(date)}
    >
      <MonthlyNav />
      <MonthlyBody
        events={[
          { title: 'Call John', date: subHours(new Date(), 2) },
          { title: 'Call John', date: subHours(new Date(), 1) },
          { title: 'Meeting with Bob', date: new Date() },
        ]}
        renderDay={data =>
          data.map((item, index) => (
            <DefaultMonthlyEventItem
              key={index}
              title={item.title}
              date={item.date}
            />
          ))
        }
      />
    </MonthlyCalendar>
  );
};