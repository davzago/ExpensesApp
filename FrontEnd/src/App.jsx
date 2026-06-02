import { Routes, Route, Navigate } from 'react-router-dom'
import Sidebar from './components/Sidebar'
import Expenses from './pages/Expenses'
import Profile from './pages/Profile'
import Graphs from './pages/Graphs'
import './App.css'

function App() {
  return (
    <div className="app-layout">
      <Sidebar />
      <main className="main-content">
        <Routes>
          <Route path="/" element={<Expenses />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/graphs" element={<Graphs />} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </main>
    </div>
  )
}

export default App
