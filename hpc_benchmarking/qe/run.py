# srun --partition=parallel --time=4:00:00 --ntasks=512 --cpus-per-task=1 --mem=32G --job-name=interactive_job --pty bash
# conda activate my_jarvis
# module load qe
from jarvis.tasks.qe.qe import QEjob
from jarvis.db.figshare import data, get_jid_data
from jarvis.core.atoms import Atoms
from jarvis.core.kpoints import Kpoints3D
from jarvis.analysis.structure.spacegroup import Spacegroup3D
import os
import time

prim_atoms = Atoms.from_dict(
    get_jid_data(jid="JVASP-816", dataset="dft_3d")["atoms"]
)
prim_atoms = Spacegroup3D(prim_atoms).refined_atoms.get_primitive_atoms
scells = [5] #[1, 2, 3, 4, 5, 6]

qe_cmd = "pw.x"
qe_cmd = "mpirun -np 512 pw.x"
kp = Kpoints3D(kpoints=[[1, 1, 1]])

relax = {
    "control": {
        "calculation": "'scf'",
        # "calculation":  "'vc-relax'",
        "restart_mode": "'from_scratch'",
        "prefix": "'RELAX'",
        "outdir": "'./'",
        "tstress": ".true.",
        "tprnfor": ".true.",
        "disk_io": "'nowf'",
        "wf_collect": ".true.",
        "pseudo_dir": None,
        "verbosity": "'high'",
        "nstep": 1,
    },
    "system": {
        "ibrav": 0,
        "nat": None,
        "ntyp": None,
        "ecutwfc": 45,
        "ecutrho": 250,
        "q2sigma": 1,
        "ecfixed": 44.5,
        "qcutz": 800,
        "occupations": "'smearing'",
        "degauss": 0.01,
        "lda_plus_u": ".false.",
    },
    "electrons": {
        "diagonalization": "'david'",
        "mixing_mode": "'local-TF'",
        "mixing_beta": 0.3,
        "conv_thr": "1d-9",
    },
    "ions": {"ion_dynamics": "'bfgs'"},
}
for s in scells:
    atoms=prim_atoms.make_supercell_matrix([s,s,s])
    print(atoms)
    cmd = "rm -rf RELAX *.json *.save *.in"
    os.system(cmd)
    cmd = "rm -rf RELAX *.json *.save *.in"
    os.system(cmd)
    t1 = time.time()
    qejob_relax = QEjob(
        atoms=atoms,
        input_params=relax,
        output_file="relax.out",
        qe_cmd=qe_cmd,
        jobname="relax",
        kpoints=kp,
        input_file="arelax.in",
        url=None,
        psp_dir=None,
        psp_temp_name=None,
    )

    info = qejob_relax.runjob()
    print(info)
    t2 = time.time()
    print("s,time", s, round(t2 - t1, 4))
