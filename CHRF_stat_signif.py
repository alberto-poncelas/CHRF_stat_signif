from art import aggregators
from art.scores import Scores, Score
from art import significance_tests

from chrf3 import computeChrF
import sys


[namepy, baselines_file, system_file, references_file] = sys.argv



with open(system_file) as file_s:
    system = file_s.readlines()


with open(baselines_file) as file_b:
    baselines = file_b.readlines()


with open(references_file) as file_r:
    references = file_r.readlines()


baseline_scores=[]
for base_line, ref_line in zip(baselines, references):
	chrf3_score = computeChrF([ref_line.strip()],[base_line.strip()])
	baseline_scores.append(chrf3_score)



system_scores=[]
for sys_line, ref_line in zip(system, references):
	chrf3_score = computeChrF([ref_line.strip()],[sys_line.strip()])
	system_scores.append(chrf3_score)


sc_system=[]
sc_baseline=[]
for chrf3_score in baseline_scores:
	sc_system.append(Score([chrf3_score]))

for chrf3_score in system_scores:
	sc_baseline.append(Score([chrf3_score]))

sc_system_ar = Scores(sc_system)
sc_baseline_ar = Scores(sc_baseline)


test = significance_tests.ApproximateRandomizationTest( sc_system_ar, sc_baseline_ar, aggregators.average,trials=int(10000))
print ("\t Significance level:", test.run())




