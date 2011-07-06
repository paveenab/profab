"""Use an EIP on an instance. This is best used when a server is first
started otherwise there might be connection problems during the
session.
"""
from profab import _logger
from profab.role import Role


class Configure(Role):
    """Assign an EIP to the server.
    """
    def configure(self):
        """Add the EIP to the server just after it has booted.
        """
        _logger.info('Associating IP number %s with server %s',
            self.parameter, self.server)
        self.server.cnx.associate_address(
            self.server.instance.id, self.parameter)
        self.server.eip = self.parameter
