import React from 'react';
import useCalendar from 'react-use-calendar';


export default function DemoCal() {

  const [state, actions] = useCalendar(null, {
    events: [
      { 
        startDate: new Date(2021, 7, 27), 
        endDate: new Date(2021, 7, 27),  
        note: 'Meeting with clients' 
      }
      // { 
      //   startDate: new Date(2021, 7, 22), 
      //   endDate: new Date(2021, 7, 25),
      //   note: 'Vacation'
      // }
    ]
  });

  return (
    <div>
    <button onClick= {evt => actions.addEvent ({ 
        startDate: new Date(2021, 7, 1), 
        endDate: new Date(2021, 7, 1),  
        note: 'Test Event' 
      })} >
    </button>
    
    <table>
      <thead>
        <tr>
          <td colSpan={5} style={{ textAlign: 'center' }}>
            <strong>{state.month} - {state.year}</strong>
          </td>
          <td colSpan={2} style={{ textAlign: 'right' }}>
            <button onClick={() => actions.getPrevMonth()}>
              &lt;
            </button>              
            <button onClick={() => actions.getNextMonth()}>
              &gt;
            </button>              
          </td>
        </tr>
        <tr>
          {state.days.map(day => <th key={day}>{day}</th>)}
        </tr>
      </thead>
      <tbody>
        {state.weeks.map((week, index) => 
          <tr key={index}>
            {week.map(day => {
              //console.log(day);

              return <td key={day.dayOfMonth} style={{ textAlign: 'center', backgroundColor: day.isToday ? '#ff0' : '#fff' }}>
                {day.dayOfMonth}
              </td>
              })}
          </tr>
        )}
      </tbody>
    </table>
    </div>
  );

}