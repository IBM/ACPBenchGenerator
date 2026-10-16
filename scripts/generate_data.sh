#!/usr/bin/bash 
# $1 - experiments folder (e.g. generated/reachability/2024-04-17 )
# $2 - type (bool or mcq)
# $3 - task (applicability, progression, reachability, validation)

type=$2
task=$3
folder=$1
mkdir -p $folder/{training,test}-$type

numplans=20
if [ "$task" = "validation" ]; then numplans=200; fi

python ./scripts/generate_questions.py --domain train --task $task --question-type $type --sample-size 20 --num-plans $numplans --merge
mv *-training.json* $folder/training-$type/
mv training.json $folder/training-$type.json
mv training.json.gz $folder/training-$type.json.gz

python ./scripts/generate_questions.py --domain train --instance-choice test --task $task --question-type $type --sample-size 20 --num-plans $numplans --merge
mv *-test.json* $folder/test-$type/
mv test.json $folder/test-$type.json
mv test.json.gz $folder/test-$type.json.gz

python ./scripts/generate_questions.py --domain test --task $task --question-type $type --sample-size 20 --num-plans $numplans --merge
mv *-test.json* $folder/test-$type/
mv test.json $folder/test-gen-$type.json
mv test.json.gz $folder/test-gen-$type.json.gz
