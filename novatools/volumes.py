from novatools import base


class Volume(base.Resource):
    """
    An volume is a persistent block-storage area
    """
    def __repr__(self):
        return "<Volume: %s>" % self.name

    def delete(self):
        """
        Delete this volume.
        """
        return self.manager.delete(self)


class VolumeManager(base.ManagerWithFind):
    """
    Manage :class:`Volume` resources.
    """
    resource_class = Volume

    def get(self, id):
        """
        Get a volume.

        :param id: The ID of the volume to get.
        :rtype: :class:`Volume`
        """
        return self._get("/volumes/%s" % base.getid(id), "volume")

    def list(self):
        """
        Get a list of all volumes.

        :rtype: list of :class:`Volume`
        """
        return self._list("/volumes/detail", "volumes")

    def create(self, volume_size):
        """
        Create a new volume

        :param volume_size: The size in GB for the new volume
        :rtype: :class:`Volume`
        """
        data = {"volume":{"size": volume_size}}
        return self._create("/volumes", data, "volume")

    def delete(self, volume):
        """
        Delete a volume

        :param volume: The :class:`Volume` (or its ID) to delete.
        """
        self._delete("/volumes/%s" % base.getid(volume))
