function ContactForm() {
  return (
    <div
      style={{
        maxWidth: "500px",
        margin: "40px auto",
        padding: "20px",
        background: "#1e1e1e",
        borderRadius: "8px",
        color: "white",
      }}
    >
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

        <div style={{ marginBottom: "15px" }}>
          <label style={{ display: "block", marginBottom: "5px" }}>
            Your Name:
          </label>
          <input
            type="text"
            name="name"
            required
            style={{
              width: "100%",
              padding: "10px",
              borderRadius: "5px",
              border: "1px solid #555",
              background: "#2a2a2a",
              color: "white",
            }}
          />
        </div>

        <div style={{ marginBottom: "15px" }}>
          <label style={{ display: "block", marginBottom: "5px" }}>
            Your Email:
          </label>
          <input
            type="email"
            name="email"
            required
            style={{
              width: "100%",
              padding: "10px",
              borderRadius: "5px",
              border: "1px solid #555",
              background: "#2a2a2a",
              color: "white",
            }}
          />
        </div>

        <div style={{ marginBottom: "15px" }}>
          <label style={{ display: "block", marginBottom: "5px" }}>
            Message:
          </label>
          <textarea
            name="message"
            required
            rows="5"
            style={{
              width: "100%",
              padding: "10px",
              borderRadius: "5px",
              border: "1px solid #555",
              background: "#2a2a2a",
              color: "white",
            }}
          ></textarea>
        </div>

        <button
          type="submit"
          style={{
            width: "100%",
            padding: "12px",
            background: "#4CAF50",
            border: "none",
            borderRadius: "5px",
            color: "white",
            fontSize: "16px",
            cursor: "pointer",
          }}
        >
          Send Message
        </button>
      </form>
    </div>
  );
}

export default ContactForm;
