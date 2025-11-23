const btn = document.getElementById('btn');
const msgEl = document.getElementById('msg');
const res = document.getElementById('result');
const label = document.getElementById('label');
const score = document.getElementById('score');

btn.addEventListener('click', async () => {
  const message = msgEl.value.trim();
  if (!message) return;

  label.textContent = 'Classifying...';
  res.classList.remove('hidden');
  try {
    const r = await fetch('http://localhost:8000/predict', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({message})
    });
    const data = await r.json();
    label.textContent = data.label === 'spam' ? '🚫 Spam' : '✅ Not Spam';
    score.textContent = ` (prob=${data.score.toFixed(3)})`;
  } catch {
    label.textContent = 'Error contacting API.';
  }
});
