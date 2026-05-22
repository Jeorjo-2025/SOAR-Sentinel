export default function ContactForm() {
  return (
    <div className="card contact-card">
      <h2>Ask Me About This SOAR Project</h2>
      <p>Recruiters and peers can leave questions or feedback here.</p>

      <form
        name="soar-contact"
        method="POST"
        data-netlify="true"
        netlify-honeypot="bot-field"
      >
        <input type="hidden" name="form-name" value="soar-contact" />

        <p className="hidden">
          <label>
            Don’t fill this out: <input name="bot-field" />
          </label>
        </p>

        <label>
          Name
          <input type="text" name="name" required />
        </label>

        <label>
          Email
          <input type="email" name="email" required />
        </label>

        <label>
          Message
          <textarea name="message" rows="4" required></textarea>
        </label>

        <button type="submit">Send</button>
      </form>
    </div>
  );
}
