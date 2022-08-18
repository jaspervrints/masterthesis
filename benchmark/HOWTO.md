# Benchmark

to use this benchmark tool edit `main.js` with correct path variables:

* path: path of query to execute
* path_comunica: path were comunica source is located both version which uses wasm and original
* path_dataset: path of dataset
* path_query_file: path of query file

to call benchmark run `node main.js {WASM} {name}`

results will be saved to output folder as `benchmark_{name}[_{wasm}]`