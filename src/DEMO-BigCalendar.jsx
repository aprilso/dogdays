// import BigCalendar from 'react-big-calendar'
// import moment from 'moment'
// import 'react-big-calendar/lib/css/react-big-calendar.css';
// require('react-big-calendar/lib/css/react-big-calendar.css');

import { Calendar, momentLocalizer  } from 'react-big-calendar' 
import 'react-big-calendar/lib/css/react-big-calendar.css';
import moment from 'moment'




export default function DemoBigCal() {

  const MyComponent = props => {
    const localizer = momentLocalizer(moment)
    return(
      <div>
        <Calendar localizer={localizer}/>
      </div>
    )
  }
  


// Setup the localizer by providing the moment (or globalize) Object
// to the correct localizer.
// const localizer = BigCalendar.momentLocalizer(moment) // or globalizeLocalizer

// const MyCalendar = props => (
//   <div>
//     <BigCalendar
//       localizer={localizer}
//       events={myEventsList}
//       startAccessor="start"
//       endAccessor="end"
//     />
//   </div>
// )
} 