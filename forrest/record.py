"""This module contains all extensions of sumatra.records.Record necessary for GAMS."""

# --- Executing XPRESS: elapsed 0:00:00.061


def extend_sumatra_record_with_gams_metadata(record):
    record.solver = 'unknown'
    for line in record.stdout_stderr.splitlines():
        if line.strip().startswith('SOLVER '):
            record.solver = [word for word in line.split(' ') if word][1]
    return record
