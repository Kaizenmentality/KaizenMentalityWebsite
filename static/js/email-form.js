const form = document.getElementById('email-form');
const message = document.getElementById('email-form-message');

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const email = document.getElementById('email').value;

  // Replace with your actual Notion API endpoint
  const notionApiUrl = 'YOUR_NOTION_API_ENDPOINT';

  try {
    const response = await fetch(notionApiUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ email })
    });

    if (response.ok) {
      message.textContent = 'Thank you for subscribing!';
    } else {
      message.textContent = 'Something went wrong. Please try again later.';
    }
  } catch (error) {
    message.textContent = 'Something went wrong. Please try again later.';
  }
});