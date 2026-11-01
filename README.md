# PWMSim

PWMSim simulates switching power converters in the browser. Open an example,
draw a circuit, or import an LTspice `.asc` schematic or a SPICE netlist, press
Run, and read the waveforms. The simulator is compiled to WebAssembly and runs
on your machine — your circuit never reaches our servers. It is free to use, with no
account and no caps.

- **App:** <https://app.pwmsim.com>
- **Site:** <https://pwmsim.com>
- **Examples:** <https://pwmsim.com/examples/>
- **Quickstart:** <https://pwmsim.com/quickstart/>
- **What it does and does not do:** <https://pwmsim.com/boundaries/>

## Click in samples below to open a circuit

Seventeen converters from [LTspicePowerSim](https://github.com/kosokno/LTspicePowerSim) (MIT), each redrawn with PWMSim's own controllers instead of the LTspice workarounds the decks use to build theirs. A title opens that circuit in the app, with no account; the file name links to the project file in [examples/](examples/).

- **[Synchronous Buck — PI Regulation](https://app.pwmsim.com/#open=https%3A%2F%2Fgithub.com%2Fpwmsim%2Fpwmsim%2Fblob%2FHEAD%2Fexamples%2Fpowersim-buck-vm.pwmsim)** ([`powersim-buck-vm.pwmsim`](examples/powersim-buck-vm.pwmsim)): LTspicePowerSim's BUCK_VM, a 5 V to 1 V synchronous buck at 2 MHz, with its Type III compensator, PWM block and dead-time generator replaced by the native PI switch and its complement.
- **[Boost — PI Regulation](https://app.pwmsim.com/#open=https%3A%2F%2Fgithub.com%2Fpwmsim%2Fpwmsim%2Fblob%2FHEAD%2Fexamples%2Fpowersim-boost-vm.pwmsim)** ([`powersim-boost-vm.pwmsim`](examples/powersim-boost-vm.pwmsim)): LTspicePowerSim's BOOST_VM, 2.5 V to 3.3 V at 1 MHz, with its Type II compensator and PWM block replaced by the native PI switch.
- **[Buck — Peak Current Mode with PI Loop](https://app.pwmsim.com/#open=https%3A%2F%2Fgithub.com%2Fpwmsim%2Fpwmsim%2Fblob%2FHEAD%2Fexamples%2Fpowersim-buck-pcm.pwmsim)** ([`powersim-buck-pcm.pwmsim`](examples/powersim-buck-pcm.pwmsim)): LTspicePowerSim's BUCK_PCM, 5 V to 1 V at 1 MHz: its comparator, latch, slope generator and Type II compensator become one native part, a peak-current switch whose command is a PI on the output.
- **[Boost — Peak Current Mode with PI Loop](https://app.pwmsim.com/#open=https%3A%2F%2Fgithub.com%2Fpwmsim%2Fpwmsim%2Fblob%2FHEAD%2Fexamples%2Fpowersim-boost-pcm.pwmsim)** ([`powersim-boost-pcm.pwmsim`](examples/powersim-boost-pcm.pwmsim)): LTspicePowerSim's BOOST_PCM, 3 V to 5 V at 1 MHz, with its current-mode control loop as the native peak-current switch and its PI voltage loop.
- **[SEPIC — Peak Current Mode with PI Loop](https://app.pwmsim.com/#open=https%3A%2F%2Fgithub.com%2Fpwmsim%2Fpwmsim%2Fblob%2FHEAD%2Fexamples%2Fpowersim-sepic-pcm.pwmsim)** ([`powersim-sepic-pcm.pwmsim`](examples/powersim-sepic-pcm.pwmsim)): LTspicePowerSim's SEPIC_PCM, 3 V to 5 V at 500 kHz, with its current-mode control loop as the native peak-current switch and its PI voltage loop.
- **[Dual Active Bridge — Phase Shift](https://app.pwmsim.com/#open=https%3A%2F%2Fgithub.com%2Fpwmsim%2Fpwmsim%2Fblob%2FHEAD%2Fexamples%2Fpowersim-dab.pwmsim)** ([`powersim-dab.pwmsim`](examples/powersim-dab.pwmsim)): LTspicePowerSim's DAB_Openloop, a 400 V bridge driving a 350 V bus at 150 kHz with the secondary 45° behind, its phase-shift block, dead-time generators and gate drivers replaced by native PWM switches and their complements.
- **[CLLC Resonant Converter — Fixed Phases](https://app.pwmsim.com/#open=https%3A%2F%2Fgithub.com%2Fpwmsim%2Fpwmsim%2Fblob%2FHEAD%2Fexamples%2Fpowersim-cllc.pwmsim)** ([`powersim-cllc.pwmsim`](examples/powersim-cllc.pwmsim)): LTspicePowerSim's CLLC_Openloop, two resonant tanks between 400 V and a 100 Ω load at 150 kHz, its phase-shift block, dead-time generators and gate drivers replaced by native PWM switches and their complements.
- **[2:1 Switched-Capacitor Ladder](https://app.pwmsim.com/#open=https%3A%2F%2Fgithub.com%2Fpwmsim%2Fpwmsim%2Fblob%2FHEAD%2Fexamples%2Fpowersim-sc-ladder.pwmsim)** ([`powersim-sc-ladder.pwmsim`](examples/powersim-sc-ladder.pwmsim)): LTspicePowerSim's SCC_Ladder_2to1_openloop, halving 10 V at 50 kHz with one flying capacitor, its clock, dead-time generator and gate drivers replaced by two native PWM switches and their complements.
- **[Three-Level Buck — Peak Current Mode](https://app.pwmsim.com/#open=https%3A%2F%2Fgithub.com%2Fpwmsim%2Fpwmsim%2Fblob%2FHEAD%2Fexamples%2Fpowersim-buck-3lv.pwmsim)** ([`powersim-buck-3lv.pwmsim`](examples/powersim-buck-3lv.pwmsim)): LTspicePowerSim's BUCK_3LV, a flying-capacitor buck from 10 V to 1 V whose one 2 MHz peak-current loop alternates between two switch pairs: here two current-mode PI switches clocked half a period apart.
- **[Four-Phase Buck — Peak Current Mode](https://app.pwmsim.com/#open=https%3A%2F%2Fgithub.com%2Fpwmsim%2Fpwmsim%2Fblob%2FHEAD%2Fexamples%2Fpowersim-buck-pcm-4ph.pwmsim)** ([`powersim-buck-pcm-4ph.pwmsim`](examples/powersim-buck-pcm-4ph.pwmsim)): LTspicePowerSim's BUCK_PCM_4ph, 5 V to 1 V at 4 A from four 2 MHz phases a quarter period apart, each a current-mode PI switch; the four PIs compute one command, as the deck's one compensator does.
- **[Active-Clamp Forward — PI Regulation](https://app.pwmsim.com/#open=https%3A%2F%2Fgithub.com%2Fpwmsim%2Fpwmsim%2Fblob%2FHEAD%2Fexamples%2Fpowersim-forward-active-clamp.pwmsim)** ([`powersim-forward-active-clamp.pwmsim`](examples/powersim-forward-active-clamp.pwmsim)): LTspicePowerSim's FORWARD_ACTIVECLAMP, 200 V to 12 V at 3 A and 250 kHz, with its peak-current loop, latch, slope generator, dead-time block and gate drivers replaced by the native PI switch and the clamp switch as its complement.
- **[Active-Clamp Flyback — PI Regulation](https://app.pwmsim.com/#open=https%3A%2F%2Fgithub.com%2Fpwmsim%2Fpwmsim%2Fblob%2FHEAD%2Fexamples%2Fpowersim-flyback-active-clamp.pwmsim)** ([`powersim-flyback-active-clamp.pwmsim`](examples/powersim-flyback-active-clamp.pwmsim)): LTspicePowerSim's FLYBACK_ACTIVECLAMP, 24 V to 5 V at 0.5 A and 180 kHz, with its phase-shift clock, peak-current latch, blanking, dead-time blocks and gate drivers replaced by the native PI switch and the clamp switch as its complement.
- **[Phase-Shifted Full Bridge — Fixed Phase](https://app.pwmsim.com/#open=https%3A%2F%2Fgithub.com%2Fpwmsim%2Fpwmsim%2Fblob%2FHEAD%2Fexamples%2Fpowersim-psfb.pwmsim)** ([`powersim-psfb.pwmsim`](examples/powersim-psfb.pwmsim)): LTspicePowerSim's PSFB, 400 V to 12 V at 12 A through a 20:1 transformer at 100 kHz, with its phase-shift block, dead-time generators and gate drivers replaced by phased PWM switches and their complements, held at the 110.6° the deck's loop settles to.
- **[LLC Resonant Converter — Fixed Frequency](https://app.pwmsim.com/#open=https%3A%2F%2Fgithub.com%2Fpwmsim%2Fpwmsim%2Fblob%2FHEAD%2Fexamples%2Fpowersim-llc.pwmsim)** ([`powersim-llc.pwmsim`](examples/powersim-llc.pwmsim)): LTspicePowerSim's LLC, 400 V to 400 V at 10 A through a 40 µH, 60 nF series tank, with its frequency loop, oscillator, dead-time generators and gate drivers replaced by PWM switches and their complements at the 117.3 kHz the deck's loop runs at.
- **[2:1 Resonant Switched-Capacitor Ladder — Fixed Phase](https://app.pwmsim.com/#open=https%3A%2F%2Fgithub.com%2Fpwmsim%2Fpwmsim%2Fblob%2FHEAD%2Fexamples%2Fpowersim-sc-resonant.pwmsim)** ([`powersim-sc-resonant.pwmsim`](examples/powersim-sc-resonant.pwmsim)): LTspicePowerSim's SCC_Ladder_2to1_PhaseShiftResonant, 10 V to 5 V at 0.25 A and 200 kHz with a 4.7 µH, 2.2 µF flying branch, its phase-shift block, dead-time generators and gate drivers replaced by PWM switches and their complements at the 41.7° the deck's loop settles to.
- **[Flyback — Peak Current Mode with PI Loop](https://app.pwmsim.com/#open=https%3A%2F%2Fgithub.com%2Fpwmsim%2Fpwmsim%2Fblob%2FHEAD%2Fexamples%2Fpowersim-flyback-pcm.pwmsim)** ([`powersim-flyback-pcm.pwmsim`](examples/powersim-flyback-pcm.pwmsim)): LTspicePowerSim's FLYBACK, 24 V to 5 V at 0.5 A through a 1:1 coupled inductor with an RCD clamp. The deck's zero-current detector, latch, slope generator and Type II compensator become one native peak-current switch whose command is a PI on the output, clocked at the 465 kHz the deck runs at.
- **[Four-Switch Buck-Boost — Analog Type III Loop](https://app.pwmsim.com/#open=https%3A%2F%2Fgithub.com%2Fpwmsim%2Fpwmsim%2Fblob%2FHEAD%2Fexamples%2Fpowersim-buck-boost-analog.pwmsim)** ([`powersim-buck-boost-analog.pwmsim`](examples/powersim-buck-boost-analog.pwmsim)): LTspicePowerSim's BUCK-BOOST_VM, 3.5 V to 3.3 V at 1 A and 1 MHz, with its controller drawn from native control parts instead of behavioural sources, logic gates and state machines: a transconductance Type III compensator, limiters for the two legs' duties, comparators against two sawtooths and delays for the dead time.

## What this repository is

This is the public home of PWMSim. **The application and its solver are closed
source and no source is published here.** What is here instead:

- **Issues** — bug reports, model requests, feature requests.
- **Discussions** — "can it do this circuit?", questions, and ideas before
  they become issues.
- **Release notes** — in [`releases/`](releases/).

The counterweight to closed source is no lock-in: your project files and
exported netlists are yours, in formats other tools open.

## Support

See [SUPPORT.md](SUPPORT.md) for
which channel fits which question, and use the contact form at
<https://pwmsim.com/contact/> for anything that does not belong in public.

## Reporting a bug

Open a [bug report](../../issues/new?template=bug_report.yml). **A reproducer
is required** — the netlist or a share link. A wrong-answer report that cannot
be reproduced cannot be confirmed, and an unconfirmed report cannot be fixed.
Also include what you expected versus what you observed and the measurement you
used to get it, the app version from the bottom of the Help menu, and your
browser and operating system.

Wrong results are taken as seriously as vulnerabilities: a confirmed wrong
answer inside a documented supported boundary gets a pinned public issue within
48 hours, a fix with a regression test or an explicit narrowing of the boundary
within one release, and a published post-mortem. That policy is at
<https://pwmsim.com/correctness/>.

## Requesting a device model

Open a [model request](../../issues/new?template=model_request.yml). Link the
publisher's page for the model and describe the fixture — operating conditions
and the reference values to compare against. **Do not attach or paste model
files:** publisher models carry their own licence terms and are not
redistributed here. A request is evaluated from a checksum-pinned copy of the
publisher's own artifact, and the result published is metadata and numeric
evidence, never vendor model text.

## Security

Vulnerabilities go privately through <https://pwmsim.com/contact/security/> or
GitHub private vulnerability reporting on this repository — never a public
issue. See [SECURITY.md](SECURITY.md).

## Licence and notice

The contents of this repository — issue templates, documentation and release
notes — are MIT licensed; see [LICENSE](LICENSE).

**The PWMSim application and solver are not covered by that licence.** They are
proprietary, distributed as build artifacts under the terms at
<https://pwmsim.com/terms/>, and no part of their source is published here or
anywhere else. The MIT grant in this repository extends only to the files in
this repository.
