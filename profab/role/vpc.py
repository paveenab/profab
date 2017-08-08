from profab.role import Role


class Configure(Role):
    """Allows a specific size to be chosen.
    """
    def vpc(self):
        """Return the size that was specified.
        """
        return self.parameter