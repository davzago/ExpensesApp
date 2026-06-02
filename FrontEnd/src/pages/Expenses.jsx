import { useState } from 'react'
import './Expenses.css'

const initialExpenses = [
  { id: 1, title: 'Groceries', tag: 'Food', value: 85.50, timestamp: '2026-06-02 13:26', description: 'Weekly grocery run at the supermarket.' },
  { id: 2, title: 'Netflix', tag: 'Entertainment', value: 15.99, timestamp: '2026-06-01 15:00', description: 'Monthly subscription for the family plan.' },
  { id: 3, title: 'Gas', tag: 'Transport', value: 45.00, timestamp: '2026-05-30 11:10', description: 'Filled up the tank at Shell station.' },
  { id: 4, title: 'Gym Membership', tag: 'Health', value: 30.00, timestamp: '2026-06-01 07:30', description: 'Monthly fee for the premium plan.' },
  { id: 5, title: 'Books', tag: 'Education', value: 22.99, timestamp: '2026-05-28 08:45', description: 'Purchased a paperback from the local store.' },
]

const TAGS = ['Food', 'Transport', 'Entertainment', 'Health', 'Education', 'Utilities', 'Shopping', 'Other']

let nextId = 6

export default function Expenses() {
  const [expenses, setExpenses] = useState(initialExpenses)
  const [expandedId, setExpandedId] = useState(null)
  const [showForm, setShowForm] = useState(false)
  const now = () => new Date().toLocaleString('sv-SE', { timeZone: 'Europe/Rome' }).slice(0, 16)
  const [form, setForm] = useState({ title: '', tag: TAGS[0], value: '', timestamp: now(), description: '' })

  const toggleDescription = (id) => {
    setExpandedId((prev) => (prev === id ? null : id))
  }

  const handleChange = (e) => {
    setForm((prev) => ({ ...prev, [e.target.name]: e.target.value }))
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    if (!form.title.trim() || !form.value) return
    setExpenses((prev) => [
      ...prev,
      {
        id: nextId++,
        title: form.title.trim(),
        tag: form.tag,
        value: parseFloat(form.value),
        timestamp: form.timestamp,
        description: form.description.trim(),
      },
    ])
    setForm({ title: '', tag: TAGS[0], value: '', timestamp: now(), description: '' })
    setShowForm(false)
  }

  return (
    <div className="page expenses-page">
      <h1>Expenses</h1>
      <p>Track and manage your expenses here.</p>

      <div className="expenses-toolbar">
        <button className="add-btn" onClick={() => setShowForm((v) => !v)}>
          {showForm ? 'Cancel' : '+ Add Expense'}
        </button>
      </div>

      {showForm && (
        <form className="expense-form" onSubmit={handleSubmit}>
          <input
            name="title"
            placeholder="Title"
            value={form.title}
            onChange={handleChange}
            required
          />
          <select name="tag" value={form.tag} onChange={handleChange}>
            {TAGS.map((t) => (
              <option key={t} value={t}>{t}</option>
            ))}
          </select>
          <input
            name="timestamp"
            type="datetime-local"
            value={form.timestamp}
            onChange={handleChange}
            required
          />
          <input
            name="value"
            type="number"
            step="0.01"
            min="0"
            placeholder="0.00"
            value={form.value}
            onChange={handleChange}
            required
          />
          <textarea
            name="description"
            placeholder="Description (optional)"
            value={form.description}
            onChange={handleChange}
            rows={2}
          />
          <button type="submit" className="submit-btn">Save</button>
        </form>
      )}

      <table className="expenses-table">
        <thead>
          <tr>
            <th>Title</th>
            <th>Tag</th>
            <th>Value</th>
          </tr>
        </thead>
        <tbody>
          {expenses.flatMap((expense) => [
            <tr key={expense.id} className="expense-row" onClick={() => toggleDescription(expense.id)}>
              <td className="expense-title">{expense.title}</td>
              <td><span className="expense-tag">{expense.tag}</span></td>
              <td className="expense-value">{expense.value.toFixed(2)}€</td>
            </tr>,
            expandedId === expense.id ? (
              <tr key={`desc-${expense.id}`} className="expense-description">
                <td colSpan={2}><div className="desc-inner"><span className="desc-text">{expense.description}</span></div></td>
                <td><div className="desc-inner"><span className="desc-timestamp">{expense.timestamp}</span></div></td>
              </tr>
            ) : null,
          ])}
        </tbody>
      </table>
    </div>
  )
}
