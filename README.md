# Install dependencies
```
uv pip install -r pyproject.toml
```

# Run
See [matmul/README.md](matmul/README.md) for short description of what matmul is.

See [pow.py](pow.py): example implementation of `pow()` for matrices with a thin wrapper around `matmul.Matrix()`.
```
memray run pow.py                   # generates a binary with alloc info
memray flamegraph <generated-bin>   # generates html page with visualizations
```

# Analyze!
Analyze the html-page with visualizations. Think on why the memory ramps up so much.
See the [pow_no_cached](pow_no_cached.py) version, build the same flamegraph and understand. What has happended.

Try running with `--native` both `pow.py` and `pow_no_cached.py`.

# Hint
`@functools.cache()` caches **all** the arguments to function. What are the arguments to `matpow()`?
See the solution in [pow_fixed.py](pow_fixed.py)