from lib.AreaStatus import AreaStatus


class Area:
    def __init__(self, name, neighbors, alpha_id, status=AreaStatus.WHITE):
        self.name = name
        self.neighbors = neighbors
        self.resources = {}
        self.alpha_id = alpha_id
        self.status = status

    '''def __str__(self):
        return "test"'''

    def __repr__(self):
        return '\nname: ' + self.name + '\talpha_id: ' + str(self.alpha_id)
