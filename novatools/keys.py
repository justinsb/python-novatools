from novatools import base


class Key(base.Resource):
    """
    An key is a cryptographic public/private key for a user
    """
    def __repr__(self):
        return "<Key: %s>" % self.name

    def delete(self):
        """
        Delete this key.
        """
        return self.manager.delete(self)


class KeyManager(base.ManagerWithFind):
    """
    Manage :class:`Key` resources.
    """
    resource_class = Key

    def get(self, key_id):
        """
        Get a key.

        :param image: The ID of the key to get.
        :rtype: :class:`Key`
        """
        return self._get("/keys/%s" % base.getid(key_id), "key")

    def list(self):
        """
        Get a list of all keys.

        :rtype: list of :class:`Key`
        """
        return self._list("/keys/detail", "keys")

    def create(self, key_name):
        """
        Create a new key

        :param key_name: An (arbitrary) name for the new key.
        :rtype: :class:`Key`
        """
        data = {"key": {"name": key_name}}
        return self._create("/keys", data, "key")

    def delete(self, key):
        """
        Delete a key

        :param key: The :class:`Key` (or its ID) to delete.
        """
        self._delete("/keys/%s" % base.getid(key))
