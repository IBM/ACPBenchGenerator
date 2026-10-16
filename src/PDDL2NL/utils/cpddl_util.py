import os
from subprocess import PIPE, Popen
import sys
from .logging_util import logger
import re 
import itertools


if sys.version_info.major < 3:
    print("Require Python 3.6 or above")
    sys.exit()
lmg_kwargs = {"stdout": PIPE,
            "stderr": PIPE}
if sys.version_info.minor >= 7:
    lmg_kwargs['text']=True
else:
    lmg_kwargs['universal_newlines']=True


def cpddl_path():
    return os.environ.get("CPDDL_PATH", "./bin/pddl")

def call_cppdl_lmgs(domain_file, problem_file):
    process = Popen([cpddl_path(),"--report-lmg",domain_file,problem_file], **lmg_kwargs)
    stdout, stderr = process.communicate()
    if process.wait() != 0 or len(str(stderr))>0:
        logger.log("There were some errors")
        logger.log("============================")
        logger.log("returncode: ", process.wait())
        logger.log("ERROR:")
        logger.log(stderr)
        logger.log("OUTPUT: ")
        logger.log(stdout)
        logger.log("============================")
        return False
    return str(stdout).split("\n")

def call_cppdl_normalization(domain_file, problem_file):
    process = Popen([cpddl_path(),"--pddl-compile-in-lmg", "--pddl-stop", domain_file,problem_file], **lmg_kwargs)
    stdout, stderr = process.communicate()
    if process.wait() != 0 or len(str(stderr))>0:
        logger.log("There were some errors")
        logger.log("============================")
        logger.log("returncode: ", process.wait())
        logger.log("ERROR:")
        logger.log(stderr)
        logger.log("OUTPUT: ")
        logger.log(stdout)
        logger.log("============================")
        return False
    return str(stdout).split("\n")


def get_LMGs_with_counting_variables(domain_file, problem_file, verbose=True):
    """Gets LMGs from CPDDL."""
    output = call_cppdl_lmgs(domain_file, problem_file)
    regexp = re.compile(r'C.:')
    lifted_mutex_groups = []
    for line in output:
        if line == '' or not line.startswith("M:") or not (regexp.search(line)):
            continue
        lifted_mutex_groups.append([ i.split() for i in line.split("{")[-1].replace("}","").split(",")])
    return lifted_mutex_groups

def get_actions_with_mutex_preconditions(domain_file, problem_file, verbose=True):
    """Gets lifted action that have mutually exclusive precondition from CPDDL."""
    output = call_cppdl_normalization(domain_file, problem_file)
    regexp = re.compile(r'Compile-in LMG: Found mutex condition for action')
    mutex_actions, LMGs = [], []
    for line in output:
        if line == '' or not (regexp.search(line)):
            continue
        action = re.findall(r'\'(.*?)\'', line)[0]
        lmg = re.findall(r'{(.*?)}', line)[0]
        mutex_actions.append(action)
        LMGs.append([ i.split() for i in lmg.split(",")])
    return mutex_actions, LMGs
