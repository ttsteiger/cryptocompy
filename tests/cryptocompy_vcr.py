import vcr

cryptocompy_vcr = vcr.VCR(
    cassette_library_dir='tests/cassettes',
    record_mode='none'
)
