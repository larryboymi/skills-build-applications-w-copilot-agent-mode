import React, { useState, useEffect, useCallback } from 'react';

// Example Codespace endpoint: https://$REACT_APP_CODESPACE_NAME-8000.app.github.dev/api/leaderboard/

function GenericTable({ items }) {
  if (!items || items.length === 0) return <div className="text-muted">No data available.</div>;
  const keys = Object.keys(items[0]);
  return (
    <div className="table-responsive table-wrap">
      <table className="table table-striped table-hover">
        <thead>
          <tr>
            {keys.map((k) => (
              <th key={k}>{k}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {items.map((it, i) => (
            <tr key={i}>
              {keys.map((k) => (
                <td key={k + i}>{typeof it[k] === 'object' ? JSON.stringify(it[k]) : String(it[k])}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

function Leaderboard() {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(false);
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  const base = codespace ? `https://${codespace}-8000.app.github.dev` : 'http://localhost:8000';
  const endpoint = `${base}/api/leaderboard/`;

  const fetchData = useCallback(() => {
    setLoading(true);
    console.log('Fetching leaderboard from', endpoint);
    fetch(endpoint)
      .then((r) => r.json())
      .then((data) => {
        console.log('Leaderboard raw data:', data);
        const list = data.results ?? data;
        setItems(Array.isArray(list) ? list : []);
      })
      .catch((err) => console.error('Leaderboard fetch error', err))
      .finally(() => setLoading(false));
  }, [endpoint]);

  useEffect(() => { fetchData(); }, [fetchData]);

  return (
    <div className="card card-custom">
      <div className="card-body">
        <h3 className="card-title card-title-small">Leaderboard</h3>
        <div className="d-flex justify-content-between align-items-center mb-2">
          <div className="endpoint">Endpoint: {endpoint}</div>
          <div>
            <button className="btn btn-sm btn-outline-secondary me-2" onClick={fetchData} disabled={loading}>{loading ? 'Loading...' : 'Refresh'}</button>
            <a className="btn btn-sm btn-link" href={endpoint} target="_blank" rel="noreferrer">Open endpoint</a>
          </div>
        </div>
        <GenericTable items={items} />
      </div>
    </div>
  );
}

export default Leaderboard;
