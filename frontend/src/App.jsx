import { useEffect, useState } from 'react'
import './App.css'

function App() {
  const [toDos, setToDos] = useState([])

  useEffect(() => {
    fetchToDos()
  }, [])

  const fetchToDos = async () => {
    const response = await fetch('http://127.0.0.1:5000/todos')
    const data = await response.json()
    setToDos(data.todo)
    console.log(data.todo)
  }

  return (
    <>
     
    </>
  )
}

export default App
