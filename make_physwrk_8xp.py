from pathlib import Path
from tivars.types import TIProgram

BASE = Path(__file__).resolve().parent

with (BASE / "PHYSICSWORK").open("r") as f:
    raw = f.read()

lines = []
for line in raw.splitlines():
    s = line.strip()
    if s.startswith(";") or not s:
        continue
    if s.startswith(":"):
        s = s[1:]
    if not s:
        continue
    lines.append(s)

source = "\n".join(lines)

label_fixes = [

    ("Lbl PM5A",  "Lbl QM"), ("Goto PM5A",  "Goto QM"), (",PM5A,",  ",QM,"), (",PM5A)",  ",QM)"),
    ("Lbl PM5B",  "Lbl QN"), ("Goto PM5B",  "Goto QN"), (",PM5B,",  ",QN,"), (",PM5B)",  ",QN)"),
    ("Lbl PM5C",  "Lbl QO"), ("Goto PM5C",  "Goto QO"), (",PM5C,",  ",QO,"), (",PM5C)",  ",QO)"),
    ("Lbl PM5D",  "Lbl QP"), ("Goto PM5D",  "Goto QP"), (",PM5D,",  ",QP,"), (",PM5D)",  ",QP)"),

    ("Lbl PM5",   "Lbl PY"), ("Goto PM5",   "Goto PY"), (",PM5,",   ",PY,"), (",PM5)",   ",PY)"),
    ("Lbl PM4",   "Lbl QK"), ("Goto PM4",   "Goto QK"), (",PM4,",   ",QK,"), (",PM4)",   ",QK)"),
    ("Lbl PM3",   "Lbl PX"), ("Goto PM3",   "Goto PX"), (",PM3,",   ",PX,"), (",PM3)",   ",PX)"),
    ("Lbl PM2",   "Lbl PU"), ("Goto PM2",   "Goto PU"), (",PM2,",   ",PU,"), (",PM2)",   ",PU)"),
    ("Lbl PM1",   "Lbl PW"), ("Goto PM1",   "Goto PW"), (",PM1,",   ",PW,"), (",PM1)",   ",PW)"),

    ("Lbl P1A",   "Lbl QA"), ("Goto P1A",   "Goto QA"), (",P1A,",   ",QA,"), (",P1A)",   ",QA)"),
    ("Lbl P1B",   "Lbl QB"), ("Goto P1B",   "Goto QB"), (",P1B,",   ",QB,"), (",P1B)",   ",QB)"),
    ("Lbl P1C",   "Lbl QC"), ("Goto P1C",   "Goto QC"), (",P1C,",   ",QC,"), (",P1C)",   ",QC)"),

    ("Lbl P2A",   "Lbl QD"), ("Goto P2A",   "Goto QD"), (",P2A,",   ",QD,"), (",P2A)",   ",QD)"),
    ("Lbl P2B",   "Lbl QE"), ("Goto P2B",   "Goto QE"), (",P2B,",   ",QE,"), (",P2B)",   ",QE)"),
    ("Lbl P2C",   "Lbl QF"), ("Goto P2C",   "Goto QF"), (",P2C,",   ",QF,"), (",P2C)",   ",QF)"),

    ("Lbl P3A",   "Lbl QG"), ("Goto P3A",   "Goto QG"), (",P3A,",   ",QG,"), (",P3A)",   ",QG)"),
    ("Lbl P3B",   "Lbl QH"), ("Goto P3B",   "Goto QH"), (",P3B,",   ",QH,"), (",P3B)",   ",QH)"),
    ("Lbl P3C",   "Lbl QI"), ("Goto P3C",   "Goto QI"), (",P3C,",   ",QI,"), (",P3C)",   ",QI)"),
    ("Lbl P3D",   "Lbl QJ"), ("Goto P3D",   "Goto QJ"), (",P3D,",   ",QJ,"), (",P3D)",   ",QJ)"),

    ("Lbl R1A",   "Lbl RA"), ("Goto R1A",   "Goto RA"), (",R1A,",   ",RA,"), (",R1A)",   ",RA)"),
    ("Lbl R1B",   "Lbl RB"), ("Goto R1B",   "Goto RB"), (",R1B,",   ",RB,"), (",R1B)",   ",RB)"),
    ("Lbl R1C",   "Lbl RC"), ("Goto R1C",   "Goto RC"), (",R1C,",   ",RC,"), (",R1C)",   ",RC)"),
    ("Lbl R1D",   "Lbl RD"), ("Goto R1D",   "Goto RD"), (",R1D,",   ",RD,"), (",R1D)",   ",RD)"),
    ("Lbl R1E",   "Lbl RE"), ("Goto R1E",   "Goto RE"), (",R1E,",   ",RE,"), (",R1E)",   ",RE)"),

    ("Lbl R2A",   "Lbl FA"), ("Goto R2A",   "Goto FA"), (",R2A,",   ",FA,"), (",R2A)",   ",FA)"),
    ("Lbl R2B",   "Lbl FB"), ("Goto R2B",   "Goto FB"), (",R2B,",   ",FB,"), (",R2B)",   ",FB)"),
    ("Lbl R2C",   "Lbl FC"), ("Goto R2C",   "Goto FC"), (",R2C,",   ",FC,"), (",R2C)",   ",FC)"),
    ("Lbl R2D",   "Lbl FD"), ("Goto R2D",   "Goto FD"), (",R2D,",   ",FD,"), (",R2D)",   ",FD)"),
    ("Lbl R2E",   "Lbl FE"), ("Goto R2E",   "Goto FE"), (",R2E,",   ",FE,"), (",R2E)",   ",FE)"),

    ("Lbl WC1",   "Lbl X1"), ("Goto WC1",   "Goto X1"), (",WC1,",   ",X1,"), (",WC1)",   ",X1)"),
    ("Lbl WC2",   "Lbl X2"), ("Goto WC2",   "Goto X2"), (",WC2,",   ",X2,"), (",WC2)",   ",X2)"),
    ("Lbl WC3",   "Lbl X3"), ("Goto WC3",   "Goto X3"), (",WC3,",   ",X3,"), (",WC3)",   ",X3)"),
    ("Lbl WC4",   "Lbl X4"), ("Goto WC4",   "Goto X4"), (",WC4,",   ",X4,"), (",WC4)",   ",X4)"),

    ("Lbl WD1",   "Lbl Y1"), ("Goto WD1",   "Goto Y1"), (",WD1,",   ",Y1,"), (",WD1)",   ",Y1)"),
    ("Lbl WD2",   "Lbl Y2"), ("Goto WD2",   "Goto Y2"), (",WD2,",   ",Y2,"), (",WD2)",   ",Y2)"),
    ("Lbl WD3",   "Lbl Y3"), ("Goto WD3",   "Goto Y3"), (",WD3,",   ",Y3,"), (",WD3)",   ",Y3)"),
    ("Lbl WD4",   "Lbl Y4"), ("Goto WD4",   "Goto Y4"), (",WD4,",   ",Y4,"), (",WD4)",   ",Y4)"),

    ("Lbl WE1",   "Lbl Z1"), ("Goto WE1",   "Goto Z1"), (",WE1,",   ",Z1,"), (",WE1)",   ",Z1)"),
    ("Lbl WE2",   "Lbl Z2"), ("Goto WE2",   "Goto Z2"), (",WE2,",   ",Z2,"), (",WE2)",   ",Z2)"),
    ("Lbl WE3",   "Lbl Z3"), ("Goto WE3",   "Goto Z3"), (",WE3,",   ",Z3,"), (",WE3)",   ",Z3)"),

    ("Lbl IFG",   "Lbl G1"), ("Goto IFG",   "Goto G1"), (",IFG,",   ",G1,"), (",IFG)",   ",G1)"),
    ("Lbl IFS",   "Lbl H1"), ("Goto IFS",   "Goto H1"), (",IFS,",   ",H1,"), (",IFS)",   ",H1)"),
    ("Lbl IFK",   "Lbl I1"), ("Goto IFK",   "Goto I1"), (",IFK,",   ",I1,"), (",IFK)",   ",I1)"),
    ("Lbl IFT",   "Lbl J1"), ("Goto IFT",   "Goto J1"), (",IFT,",   ",J1,"), (",IFT)",   ",J1)"),
    ("Lbl IFC",   "Lbl K1"), ("Goto IFC",   "Goto K1"), (",IFC,",   ",K1,"), (",IFC)",   ",K1)"),

    ("Lbl IG1",   "Lbl G2"), ("Goto IG1",   "Goto G2"), (",IG1,",   ",G2,"), (",IG1)",   ",G2)"),
    ("Lbl IG2",   "Lbl G3"), ("Goto IG2",   "Goto G3"), (",IG2,",   ",G3,"), (",IG2)",   ",G3)"),
    ("Lbl IG3",   "Lbl G4"), ("Goto IG3",   "Goto G4"), (",IG3,",   ",G4,"), (",IG3)",   ",G4)"),

    ("Lbl IS1",   "Lbl H2"), ("Goto IS1",   "Goto H2"), (",IS1,",   ",H2,"), (",IS1)",   ",H2)"),
    ("Lbl IS2",   "Lbl H3"), ("Goto IS2",   "Goto H3"), (",IS2,",   ",H3,"), (",IS2)",   ",H3)"),
    ("Lbl IS3",   "Lbl H4"), ("Goto IS3",   "Goto H4"), (",IS3,",   ",H4,"), (",IS3)",   ",H4)"),

    ("Lbl IK1",   "Lbl I2"), ("Goto IK1",   "Goto I2"), (",IK1,",   ",I2,"), (",IK1)",   ",I2)"),
    ("Lbl IK2",   "Lbl I3"), ("Goto IK2",   "Goto I3"), (",IK2,",   ",I3,"), (",IK2)",   ",I3)"),
    ("Lbl IK3",   "Lbl I4"), ("Goto IK3",   "Goto I4"), (",IK3,",   ",I4,"), (",IK3)",   ",I4)"),

    ("Lbl IT1",   "Lbl J2"), ("Goto IT1",   "Goto J2"), (",IT1,",   ",J2,"), (",IT1)",   ",J2)"),
    ("Lbl IT2",   "Lbl J3"), ("Goto IT2",   "Goto J3"), (",IT2,",   ",J3,"), (",IT2)",   ",J3)"),
    ("Lbl IT3",   "Lbl J4"), ("Goto IT3",   "Goto J4"), (",IT3,",   ",J4,"), (",IT3)",   ",J4)"),

    ("Lbl IC1",   "Lbl K2"), ("Goto IC1",   "Goto K2"), (",IC1,",   ",K2,"), (",IC1)",   ",K2)"),
    ("Lbl IC2",   "Lbl K3"), ("Goto IC2",   "Goto K3"), (",IC2,",   ",K3,"), (",IC2)",   ",K3)"),
    ("Lbl IC3",   "Lbl K4"), ("Goto IC3",   "Goto K4"), (",IC3,",   ",K4,"), (",IC3)",   ",K4)"),
    ("Lbl IC4",   "Lbl K5"), ("Goto IC4",   "Goto K5"), (",IC4,",   ",K5,"), (",IC4)",   ",K5)"),
    ("Lbl IC5",   "Lbl K6"), ("Goto IC5",   "Goto K6"), (",IC5,",   ",K6,"), (",IC5)",   ",K6)"),
]

for old, new in label_fixes:
    source = source.replace(old, new)

source = source.replace("cos^-1(", "cos-1(")

source = source.replace(
    "round(N,2-int(log(abs(N))))",
    "round(N/10^(int(log(abs(N+(N=0))))-2),0)*10^(int(log(abs(N+(N=0))))-2)")
source = source.replace(
    "round(W,2-int(log(abs(W))))",
    "round(W/10^(int(log(abs(W+(W=0))))-2),0)*10^(int(log(abs(W+(W=0))))-2)")
source = source.replace(
    "round(P,2-int(log(abs(P))))",
    "round(P/10^(int(log(abs(P+(P=0))))-2),0)*10^(int(log(abs(P+(P=0))))-2)")

source = source.replace("\nPause\n", "\nPause \n")

if source.endswith("\nPause"):
    source += " "

prog = TIProgram(name="PHYSWRK")
prog.load_string(source)
prog.save(str(BASE / "PHYSWRK.8xp"))

import os
size = os.path.getsize(BASE / "PHYSWRK.8xp")
print(f"Saved PHYSWRK.8xp  ({size:,} bytes)")
print("Transfer with TI Connect CE → calculator")
