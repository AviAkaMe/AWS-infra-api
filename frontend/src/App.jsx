import { useState } from 'react'
import { useNavigate } from 'react-router-dom'

function App() {
  const [accessKey, setAccessKey] = useState('')
  const [secretKey, setSecretKey] = useState('')
  const [region, setRegion] = useState('us-west-2')
  const [error, setError] = useState(null)
  const navigate = useNavigate()

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError(null)

    try {
      const res = await fetch('http://localhost:5000/api/v1/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          aws_access_key_id: accessKey,
          aws_secret_access_key: secretKey,
          aws_region: region,
        }),
      })

      if (res.ok) {
        localStorage.setItem('aws_access_key_id', accessKey)
        localStorage.setItem('aws_region', region)
        navigate('/dashboard')
      } else {
        setError(data.error || 'Login failed')
      }
    } catch (err) {
      setError('Failed to reach backend')
    }
  }

  return (
    <div style={{ padding: 40 }}>
      <h2>🔐 Enter AWS Credentials</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" placeholder="Access Key" value={accessKey} onChange={(e) => setAccessKey(e.target.value)} /><br /><br />
        <input type="password" placeholder="Secret Key" value={secretKey} onChange={(e) => setSecretKey(e.target.value)} /><br /><br />
        <input type="text" placeholder="Region" value={region} onChange={(e) => setRegion(e.target.value)} /><br /><br />
        <button type="submit">Connect</button>
      </form>
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  )
}

export default App