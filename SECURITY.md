# Security policy

## Reporting a vulnerability

Report privately. **Do not open a public issue for an exploitable problem.**
Either route works:

- GitHub private vulnerability reporting on this repository — use the
  **Report a vulnerability** button under the Security tab; or
- the security report form at <https://pwmsim.com/contact/security/>, which
  posts to that origin and is relayed to a private inbox.

Expect an acknowledgment within a week. This is a part-time solo project;
severity, not politeness, sets the response speed. Please include a reproducer
and say plainly what an attacker gains. If you would like credit in the fix
note, say so.

There is no bug-bounty programme and no payment.

## Supported versions

The project is in technical beta. The current hosted release is supported.

## Threat model

These are the properties the product claims. A way to break one of them is a
security bug.

- **Netlists and expressions are untrusted input.** Behavioural expressions in
  an imported deck are validated before they are simulated. A netlist that can
  execute arbitrary code, escape that validation, or exhaust memory without
  bound is a security bug.
- **The application is client-side.** The simulator runs in the browser and
  circuits never leave it. Any path by which circuit content reaches the
  network from the hosted application is a security bug.
- **Share links travel in the URL fragment**, which browsers do not send to
  servers. Anything that puts circuit content somewhere a server can observe it
  is a security bug.
- **The published build is the released build.** Any way to serve a modified
  artifact from the published origins is a security bug.

## Wrong answers

A simulator's worst failure is a confidently wrong waveform, not a crash.
Confirmed wrong-answer reports inside a documented supported boundary are
handled with the same seriousness as vulnerabilities, under the
[correctness-incident policy](https://pwmsim.com/correctness/).

## Scope

In scope: the hosted application and its embeds, the site, and the DNS, mail
and hosting configuration for `pwmsim.com`.

Out of scope: automated scanner output with no demonstrated impact, missing
security headers on pages that carry no data, and reports that depend on the
user running a modified copy of the application.
