from dataclasses import dataclass


@dataclass
class PlaylistTrack:
    PlaylistId: int
    TrackId: int

    def __hash__(self):
        return hash(self.PlaylistId)
    def __eq__(self, other):
        return self.PlaylistId == other.PlaylistId
    def __str__(self):
        return f'{self.PlaylistId} - {self.TrackId}'