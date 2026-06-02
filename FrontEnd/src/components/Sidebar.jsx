import { NavLink } from 'react-router-dom'
import './Sidebar.css'

const links = [
  { to: '/', label: 'Expenses' },
  { to: '/profile', label: 'Profile' },
  { to: '/graphs', label: 'Graphs' },
]

export default function Sidebar() {
  return (
    <nav className="sidebar">
      <div className="sidebar-title">Menu</div>
      <ul>
        {links.map(({ to, label }) => (
          <li key={to}>
            <NavLink
              to={to}
              end={to === '/'}
              className={({ isActive }) => (isActive ? 'active' : '')}
            >
              {label}
            </NavLink>
          </li>
        ))}
      </ul>
    </nav>
  )
}
