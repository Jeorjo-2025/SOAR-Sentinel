// src/components/ContactForm.jsx
function ContactForm() {
  return (
    <form
      name="contact"
      method="POST"
      data-netlify="true"
      data-netlify-honeypot="bot-field"
    >
      <input type="hidden" name="form-name" value="contact" />

      <div hidden>
        <input name="bot-field" />
      </div>

      <label>
        Your Name:
        <input type="text" name="name" required />
      </label>

      <label>
        Your Email:
        <input type="email" name="email" required />
      </label>

      <label>
        Message:
        <textarea name="message" required></textarea>
      </label>

      <button type="submit">Send Message</button>
    </form>
  );
}

export default ContactForm;
