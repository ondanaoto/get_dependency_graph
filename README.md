# get-dependent-graph
1. do the following:
```
git clone ~~
cd mathlib
lake exe cache get
lake build
lake exe graph
rye sync
```
2. use the script like the following:
```
rye run python get_dependency.py --start_node  Mathlib.InformationTheory.Hamming
```
