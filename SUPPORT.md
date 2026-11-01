# Support

Public first, wherever the subject allows it. An answered question in
Discussions is searchable and helps the next person; the same answer in an
inbox helps one.

## Which channel

| You have | Where it goes |
|---|---|
| A wrong or suspicious result | [Bug report](../../issues/new?template=bug_report.yml) — a reproducer netlist or share link is **required** |
| A crash, a hang, or a broken import | [Bug report](../../issues/new?template=bug_report.yml) |
| "Can it do this circuit?" | [Discussions](../../discussions) — the most useful question you can ask |
| A device model you need | [Model request](../../issues/new?template=model_request.yml) — publisher link only, never model files |
| A feature idea | [Discussions](../../discussions) first, so it can be argued about in public, then a [feature request](../../issues/new?template=feature_request.yml) |
| A security vulnerability | Privately — the [security report form](https://pwmsim.com/contact/security/) or private vulnerability reporting. See [SECURITY.md](SECURITY.md). Never a public issue. |
| Licensing, commercial, press, anything else | The [contact form](https://pwmsim.com/contact/) |

## What makes a bug report actionable

1. **A reproducer.** The netlist, or a share link. Without one a wrong-answer
   report cannot be confirmed, and an unconfirmed report cannot be fixed.
2. **Expected versus observed**, with the number and the measurement you used
   to get it — "the ripple reads 63 mV; volt-second balance says 9 mV" beats
   "the waveform looks wrong".
3. **The app version**, shown at the bottom of the app's Help menu.
4. **Browser and operating system.**

Reproducers are treated as your material. They are used to fix the defect you
reported, and become a regression test only with your explicit agreement.

## What is not supported

No SLA beyond the line at the top. No private roadmap commitments, and no
guarantee that a request gets built. What stays yours either way: project files
and exported netlists, in formats other tools open.

## Reporting a wrong answer

Confirmed wrong results inside a documented supported boundary are handled
under the published
[correctness-incident policy](https://pwmsim.com/correctness/) — pinned public
issue, fix or explicit boundary change within one release, published
post-mortem. Showing that PWMSim gives a wrong number is a contribution, not
an attack.
