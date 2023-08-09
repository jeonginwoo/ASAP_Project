const scribe_popup = document.getElementById('scribe_popup');

fetch('scribe-popup.html')
  .then(res => res.text())
  .then(data => scribe_popup.innerHTML = data);