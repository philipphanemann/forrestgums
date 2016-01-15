"""This module contains all extensions of sumatra.records.Record necessary for GAMS."""


def extend_sumatra_record_with_gams_metadata(record):
    record.gams = 'jo'
    return record
