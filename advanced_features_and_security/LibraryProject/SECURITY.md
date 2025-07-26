# Security Measures Implemented
- DEBUG set to False in production.
- Browser headers: XSS filter, X-Frame-Options, and Content-Type-NoSniff.
- CSRF protection on all forms.
- ORM used to prevent SQL injection.
- Content Security Policy (CSP) to limit external resources.
- Cookies are secure (HTTPS-only).
- Tested manually:
  - Verified CSRF token presence.
  - Attempted XSS payloads were blocked.
  - SQL injection attempts failed.

# HTTPS Security Implementation

- **SECURE_SSL_REDIRECT**: Forces all HTTP traffic to redirect to HTTPS.
- **HSTS (HTTP Strict Transport Security)**: Instructs browsers to only use HTTPS for one year.
- **Secure Cookies**: Ensures session and CSRF cookies are only sent over HTTPS.
- **Clickjacking Protection**: `X_FRAME_OPTIONS = 'DENY'`.
- **Content Sniffing Protection**: `SECURE_CONTENT_TYPE_NOSNIFF = True`.
- **XSS Protection**: `SECURE_BROWSER_XSS_FILTER = True`.

## Deployment

- SSL certificates installed using Let's Encrypt.
- Nginx configured to redirect HTTP to HTTPS.
- Gunicorn runs behind Nginx with HTTPS enabled.

## Review

✔ Tested HTTP → HTTPS redirection.  
✔ Verified cookies are `Secure`.  
✔ Checked headers with browser dev tools.  
⚠ Ensure production uses HTTPS; local dev should keep settings disabled.
