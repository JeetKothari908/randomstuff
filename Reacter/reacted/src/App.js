import './App.css';
import TodoList from './TodoList'
import React, { usestate} from 'react';
function App() {
  return (
    <>
       <TodoList /> 
       <input type="text" />
       <button> Add Todo </button>
       <button> Clear Complete</button>
       <div> 0 left to do</div>
    </>

  )
}

export default App;
