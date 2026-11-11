(function () {
  function measureGoogle() {
    try {
      if (typeof gtag === 'function') gtag.apply(null, arguments);
    } catch (_) {
      // Advertising measurement must not interrupt contact actions.
    }
  }
  const form = document.querySelector('.contact-form');
  const status = document.getElementById('form-status');
  const button = form && form.querySelector('button[type="submit"]');
  const attributionKeys = ['utm_source','utm_medium','utm_campaign','utm_term','utm_content','gclid','gbraid','wbraid'];
  const params = new URLSearchParams(window.location.search);
  let attribution = {};
  try {
    attribution = JSON.parse(sessionStorage.getItem('glenhold_attribution') || '{}');
    attributionKeys.forEach(function(key) {
      if (params.has(key)) attribution[key] = params.get(key).slice(0, 500);
    });
    sessionStorage.setItem('glenhold_attribution', JSON.stringify(attribution));
  } catch (_) {
    attributionKeys.forEach(function(key) {
      if (params.has(key)) attribution[key] = params.get(key).slice(0, 500);
    });
  }
  attributionKeys.forEach(function(key) {
    if (!attribution[key]) return;
    const input = document.createElement('input');
    input.type = 'hidden'; input.name = key; input.value = attribution[key];
    if (form) form.appendChild(input);
  });
  document.querySelectorAll('a[href^="tel:"]').forEach(function(link) {
    link.addEventListener('click', function() {
      measureGoogle('event', 'phone_link_click', {event_category: 'engagement'});
    });
  });
  document.querySelectorAll('a[href^="https://calendar.app.google/"]').forEach(function(link) {
    link.addEventListener('click', function() {
      measureGoogle('event', 'consultation_booking_click', {event_category: 'engagement'});
    });
  });
  if (!form) return;
  form.addEventListener('submit', async function(event) {
    event.preventDefault();
    if (!form.reportValidity() || button.disabled) return;
    button.disabled = true;
    button.textContent = 'Sending...';
    status.textContent = '';
    try {
      const response = await fetch(form.action, {
        method: 'POST', body: new FormData(form), headers: {Accept: 'application/json'}
      });
      if (!response.ok) throw new Error('Unable to send');
      status.textContent = 'Thank you! Your message has been sent. Jack will reply within one business day.';
      status.style.color = 'var(--slate)';
      button.textContent = 'Message sent';
      measureGoogle('event', 'conversion', {
        send_to: 'AW-17998714201/jcT9CLryvoQcENmquoZD',
        transaction_id: window.crypto && window.crypto.randomUUID ? window.crypto.randomUUID() : String(Date.now())
      });
      try {
        oaiq("measure", "lead_created", {type: "customer_action"}, {opt_out: true});
      } catch (_) {
        // Measurement must never interrupt a successfully delivered inquiry.
      }
      form.reset();
    } catch (_) {
      status.textContent = 'Your message could not be sent. Please try again, call (805) 419-3451, or email jack@glenhold.com.';
      status.style.color = '#9b2525';
      button.disabled = false;
      button.textContent = 'Send Message →';
    }
  });
})();
