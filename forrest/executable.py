from sumatra.programs import Executable, version_in_command_line_output
from sumatra.core import component, run


@component
class GAMSExecutable(Executable):
    name = "GAMS"
    executable_names = ('gams',)
    file_extensions = ('.gms',)
    default_executable_name = 'gams'
    requires_script = False

    def _get_version(self):
        returncode, output, err = run("gams file_that_doesnt_exist.gms lo=3", shell=True)
        return version_in_command_line_output(command_line_output=output + err)
