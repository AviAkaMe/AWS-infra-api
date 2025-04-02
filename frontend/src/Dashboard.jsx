import { useEffect, useState } from 'react'

function Dashboard() {
  const [summary, setSummary] = useState(null)
  const [error, setError] = useState(null)

  useEffect(() => {
    const fetchSummary = async () => {
      const accessKey = localStorage.getItem('aws_access_key_id')
      const region = localStorage.getItem('aws_region')

      try {
        const res = await fetch('http://localhost:5000/api/v1/dashboard/summary', {
          method: 'GET',
          headers: {
            'AWSAccessKeyId': accessKey,
            'AWSRegion': region,
          },
        })

        const data = await res.json()
        if (res.ok) {
          setSummary(data.summary)
        } else {
          setError(data.error || 'Failed to load summary')
        }
      } catch (err) {
        setError('Could not connect to backend')
      }
    }

    fetchSummary()
  }, [])

  if (error) return <div>❌ {error}</div>
  if (!summary) return <div>⏳ Loading dashboard...</div>

  return (
    <div style={{ padding: 40 }}>
      <h2>📊 AWS Infrastructure Summary</h2>

      <h3>Amazon ECS</h3>
      <ul>
        <li>Clusters: {summary.ecs.total_clusters}</li>
        <li>Services: {summary.ecs.total_services}</li>
        <li>Tasks Running: {summary.ecs.total_tasks}</li>
        <li>Unhealthy Services: {summary.ecs.unhealthy_services}</li>
      </ul>

      <h3>Amazon S3</h3>
      <p>{typeof summary.s3 === 'string' ? summary.s3 : '✓ Data available'}</p>

      <h3>Amazon EBS</h3>
      <p>{typeof summary.ebs === 'string' ? summary.ebs : '✓ Data available'}</p>

      <h3>Network</h3>
      <p>{typeof summary.network === 'string' ? summary.network : '✓ Data available'}</p>
    </div>
  )
}

export default Dashboard