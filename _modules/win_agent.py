from __future__ import absolute_import
import psutil
import os

PROGRAM_DIR = "C:\\Program Files\\TacticalAgent"


def get_services():
    return [svc.as_dict() for svc in psutil.win_service_iter()]


def run_python_script(filename, timeout):
    python_bin = os.path.join("c:\\salt\\bin", "python.exe")
    file_path = os.path.join("c:\\windows\\temp", filename)
    __salt__["cp.get_file"](
        "salt://scripts/userdefined/{0}".format(filename), file_path
    )
    return __salt__["cmd.run_all"](
        "{0} {1}".format(python_bin, file_path), timeout=timeout
    )


def uninstall_agent():
    remove_exe = os.path.join(PROGRAM_DIR, "unins000.exe")
    __salt__["cmd.run_bg"]([remove_exe, "/VERYSILENT", "/SUPPRESSMSGBOXES"])
    return "ok"


def update_salt():
    tacrmm = os.path.join(PROGRAM_DIR, "tacticalrmm.exe")
    __salt__["cmd.run_bg"]([tacrmm, "-m", "updatesalt"])
    return "ok"


def run_manual_checks():
    tacrmm = os.path.join(PROGRAM_DIR, "tacticalrmm.exe")
    __salt__["cmd.run_bg"]([tacrmm, "-m", "runchecks"])
    return "ok"