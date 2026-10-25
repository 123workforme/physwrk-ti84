# PHYSWRK

A TI-84 Plus CE program that solves mechanical energy, work, and power problems step by step.

I wrote it while studying energy in physics, because a formula sheet shows the answer without showing the thinking. PHYSWRK asks which quantity you are solving for, collects the values you know, and then walks through the solution in four screens:

1. **Formula** – the physics principle being used
2. **Rearrange** – the equation solved for the unknown
3. **Plug in** – your numbers substituted, with each intermediate term shown
4. **Answer** – the result, rounded to three significant figures, with units

To program a formula so it can be solved for any of its variables, I first had to understand it in every direction.

## Example: roller coaster, find the speed at point B

```
STEP1:FORMULA        STEP2:REARRANGE      STEP3:PLUG IN         STEP4:ANSWER
MEA=MEB              vB=sqrt(2*(GhA       9.81*20+.5*3^2        vB (M/S)=
GhA+.5vA^2           +.5vA^2-GhB))          GhA=196.2           15
=GhB+.5vB^2                                 KEa=4.5
                                            GhB=88.29
                                            Q=112.41
```

(Inputs: hA = 20 m, vA = 3 m/s, hB = 9 m. The answer screen shows 15.)

## What it covers

**Energy problems**
- Roller coaster (conservation of mechanical energy), including a full solve and a guide
- Roller coaster with friction
- Spring launch and spring compression
- Pendulum
- Skier on a slope

**Work**
- Pushing or pulling an object at an angle
- Net work with friction
- Work from a change in speed or height
- Braking distance and coefficient of friction

**Power**
- Work over time, force times velocity, force times distance over time
- Climbing stairs and motor lifts

**Tools**
- Individual formulas: gravitational PE, spring PE, KE, total energy, conservation of energy
- Unit converter: length, mass, speed, time, energy and force

Every solver can find any variable in its equation, not only the usual unknown.

## Designing for a calculator

- **Two-character labels.** TI-BASIC only allows labels of one or two characters, which makes a program with dozens of menus hard to read. I wrote the source with descriptive labels (`P1A`, `WC1`, `IFG`), and the build script renames them to valid two-character labels automatically.
- **Bad inputs.** The program checks for a negative value under a square root, division by zero, and negative heights, and sends you back to the menu with a message instead of crashing.
- **Rounding.** The obvious way to round to three significant figures uses `log(abs(N))`, which fails when the answer is zero. The build script swaps in an expression that handles zero correctly.
- **A tiny screen.** Each step had to fit on the CE's home screen, so explanations are split across short lines and pages.
- **Limited variables.** TI-BASIC gives you single-letter variables, so the same letters are reused carefully across solvers.

## Install

**Option 1: use the prebuilt file**

1. Download `PHYSWRK.8xp` from this repository.
2. Send it to your calculator with [TI Connect CE](https://education.ti.com/en/products/computer-software/ti-connect-ce-sw).
3. On the calculator, press `prgm`, choose `PHYSWRK`, and press `enter`.

The program uses `toString(`, so it needs a TI-84 Plus CE with a recent operating system.

**Option 2: build it from source**

```bash
pip install tivars
python make_physwrk_8xp.py
```

This reads the readable source in `PHYSICSWORK`, strips comments and leading colons, fixes the labels and rounding expressions, and writes `PHYSWRK.8xp`.

## Files

| File | What it is |
| --- | --- |
| `PHYSICSWORK` | Readable TI-BASIC source with descriptive labels |
| `make_physwrk_8xp.py` | Build script that converts the source into a calculator file |
| `PHYSWRK.8xp` | Ready-to-install program |

## Notes

Gravity is set to 9.81 m/s², and the calculator is switched to degree mode for problems with angles.
