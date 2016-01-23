"""This module contains all extensions of Django.records.Record necessary for GAMS."""

from sumatra.programs import version_in_command_line_output


def extend_django_record_with_gams_metadata(record):
    """Reads meta data from GAMS listing and ammends the sumatra record with it."""
    record.solver = 'unknown'
    record.solver_version = 'unknown'
    sumatra_record = record.to_sumatra()
    listing_data_key = sumatra_record.output_data[0]
    listing = sumatra_record.datastore.get_data_item(listing_data_key).content.decode('utf-8')
    for line in listing.splitlines():
        if line.strip().startswith('SOLVER '):
            record.solver = [word for word in line.split(' ') if word][1]
    if record.solver != 'unknown':
        for line in listing.splitlines():
            if record.solver.lower() in line.lower() and 'version' in line.lower():
                record.solver_version = version_in_command_line_output(line)
    if record.solver.lower() == 'cplex':
        for line in listing.splitlines():
            if line.lower().startswith('cplex') and len(line.split(' ')) == 2:
                record.solver_version = line.split(' ')[1]
    elif record.solver.lower() == 'conopt':
        for line in listing.splitlines():
            if record.solver.lower() in line.lower().replace(' ', '') and 'version' in line.lower():
                record.solver_version = line.split('version')[-1].strip()
    elif record.solver.lower() == 'xpress':
        for line in listing.splitlines():
            if line.startswith('Xpress-Optimizer'):
                record.solver_version = [word for word in line.split(' ') if word.startswith('v')][0][1:]
    return record
