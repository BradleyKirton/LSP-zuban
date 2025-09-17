from lsp_utils.pip_client_handler import PipClientHandler


class ZubanLsp(PipClientHandler):
    package_name = __package__
    requirements_txt_path = "requirements.txt"
    server_filename = "zuban"


def plugin_loaded() -> None:
    ZubanLsp.setup()


def plugin_unloaded() -> None:
    ZubanLsp.cleanup()
