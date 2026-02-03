from unittest.mock import patch, MagicMock

from core.context import ReconContext
from modules.port_scan import PortScanModule


@patch("modules.port_scan.socket.socket")
def test_port_scan_detects_open_ports(mock_socket):
    mock_sock_instance = MagicMock()
    mock_sock_instance.connect_ex.side_effect = lambda addr: 0 if addr[1] == 80 else 1
    mock_socket.return_value.__enter__.return_value = mock_sock_instance

    context = ReconContext(target="example.com")
    context.ips.add("93.184.216.34")

    module = PortScanModule()
    module.run(context)

    assert "93.184.216.34" in context.open_ports
    assert 80 in context.open_ports["93.184.216.34"]


@patch("modules.port_scan.socket.socket")
def test_port_scan_handles_no_open_ports(mock_socket):
    mock_sock_instance = MagicMock()
    mock_sock_instance.connect_ex.return_value = 1
    mock_socket.return_value.__enter__.return_value = mock_sock_instance

    context = ReconContext(target="example.com")
    context.ips.add("93.184.216.34")

    module = PortScanModule()
    module.run(context)

    assert context.open_ports == {}
