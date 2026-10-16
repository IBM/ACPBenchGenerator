from setuptools import setup

setup(
   name='ACPBenchGenerator',
   packages=['PDDL2NL'],
   package_dir={'':'src'},
   install_requires=[
      "ibm-generative-ai==2.1.1",
      "tarski[clingo]==0.8.2",
      "kstar-planner>=1.4.1",
      "forbiditerative>=1.0.13",
      "python-dotenv",
      "tqdm",
      "numpy",
      "python-dateutil",
      "lark",
      "jsonlines",
      "inflect",
      "pddl==0.4.2"
   ],
)