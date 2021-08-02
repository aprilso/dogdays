import React from "react";
import { useParams } from "react-router-dom";
// renamed from App to DogSchedule, exported so App.jsx can import
export default function DogSchedule() {
  // instead of getting URL and parsing it for the ID, use
  // hook from React Router
  let { dogId } = useParams();
  return (
    <div>
      <Greeting />
      <ViewSchedule />
      <div>{dogId}</div>
    </div>
  );
}

function Greeting(props) {
  // let date = new Date("2021-07-30" + 'T00:00:00');
  // calendar.addEvent({
  //   title: 'Test event',

  //   start: date,
  //   allDay: true
  // });
  return <div>Hello</div>;
  // return <h1>Hello {props.name}</h1>;
}
// Need to add the existing database tasks to the calendar when you view the page - populate the existing database tasks
// into the calendar - something like Calendar.AddEvent with the data



function Task({ taskName, instructions, frequency, userId }) {
  return (
    <div className="task">
      <p>Task: {taskName} </p>
      <p>Instructions: {instructions} </p>
      <p>Frequency: {frequency}</p>
      <p>Created by (optional): {userId}</p>
    </div>
  );
}

function ViewSchedule() {
  const [schedule, setSchedule] = React.useState([]);
  let { dogId } = useParams();
  console.log (schedule);

  function deleteTask(taskId) {
    let currentSchedule = [...schedule]
    currentSchedule = currentSchedule.filter(s => s.taskId !== taskId)
    //returns an array that matches these conditions, everything that doesn't have that task id
    setSchedule(currentSchedule)
    fetch(`/api/delete-task/${taskId}`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((jsonResponse) => {
        // const [Reload, True] = React.useState([]);
        // Right now, it deletes the task but needs to change the state to reload ViewSchedule
        // The li needs to be a React Component
      });
  }


  React.useEffect(() => {
    fetch(`/api/dogschedule/${dogId}`)
      .then((response) => response.json())
      .then((result) => {
        setSchedule(result);
      });
  }, []);

  return (
    <>
      <h2>Current Overall Schedule: </h2>
      <ul>
        {schedule.map((each) => {
          return <li key={each.taskId}>
            {each.taskName} | {each.frequency} | {each.instructions} |
            <button type="button" onClick={() => deleteTask(each.taskId)}>
              Delete Task
            </button>
          </li>;
        })}
      </ul>
      <AddTaskToSchedule setSchedule={setSchedule} schedule={schedule} />
    </>
  );
}

function AddTaskToSchedule(props) {
  const [task_name, setTask] = React.useState("");
  const [frequency, setFrequency] = React.useState("");
  const [instructions, setInstructions] = React.useState("");

  const frequencyList = ["SELECT", "Once", "Daily", "Weekly", "Monthly", "Yearly"];

  function addNewTask() {
    fetch("/api/add-task", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ task_name, frequency, instructions }),
    })
      .then((response) => response.json())
      .then((jsonResponse) => {
        props.setSchedule([...props.schedule, jsonResponse.taskAdded]);
        setTask("");
        setFrequency("");
        setInstructions("");
      });
  }

  return (
    <>
      <h2>Add New Task</h2>
      <label htmlFor="taskInput">Task Name</label>
      <input
        value={task_name}
        onChange={(event) => setTask(event.target.value)}
        id="taskInput"
      />
      <br />
      <label htmlFor="frequencyInput">Frequency</label>

      <select
        onChange={(event) => setFrequency(event.target.value)}
        id="frequencyInput"
      >
        {frequencyList.map((frequency) => (
          <option>{frequency}</option>
        ))}
      </select>

      <br />
      <label htmlFor="taskInstructions">Instructions</label>
      <input
        value={instructions}
        onChange={(event) => setInstructions(event.target.value)}
        id="taskInstructions"
      />
      <br />
      <button onClick={addNewTask}>Add</button>
    </>
  );
}

function TodaysScheduleList() {
  // TO-DO - view today's schedule
  // can use FullCalendar list view
}

function MarkTaskComplete() {
  // TO-DO
}

function AddNoteToCalendar() {
  // TO-DO
}

function AddEventOccurrence() {
  // TO-DO
}
